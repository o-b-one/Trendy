import { defaultErrorHandler, express, HttpServer } from "@sugoi/server";
import * as bodyParser from 'body-parser';
import * as compression from 'compression';
import * as path from "path";
import { paths } from "../config/paths";
import { BootstrapModule } from "./bootstrap.module";
import { Authorization } from "./classes/authorization.class"
import { MongoModel } from "@sugoi/mongodb";
import { services } from "../config/services";

const DEVELOPMENT = process.env['isDev']  as any;
const TESTING = process.env['isTest']  as any;
const PROD = process.env['isProd']  as any;

const setDBs = function (app) {
    MongoModel.setConnection(services.MONGODB).catch(console.error);
};


const server: HttpServer = HttpServer.init(BootstrapModule, "/", Authorization)
    .setStatic(paths.staticDir) // set static file directory path
    .setMiddlewares((app) => {
        app.disable('x-powered-by');
        app.set('etag', 'strong');
        app.set('host', process.env.HOST || '0.0.0.0');
        app.use(express.json());
        app.use(compression());

        setDBs(app);
    })
    .setErrorHandlers((app) => {
        app.use((req, res, next) => {
            // Set fallback to send the web app index file
            return res.sendFile(path.resolve(paths.index))
        });
        // The value which will returns to the client in case of an exception
        app.use(console.error);
        app.use(defaultErrorHandler(DEVELOPMENT || TESTING));
    });

export {server};
