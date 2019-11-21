import { ServerModule } from "@sugoi/server"
import { IndexController } from "./controllers/index.controller";
import { IndexService } from "./services/index.service";

@ServerModule({
    modules:[],
    controllers:[IndexController],
    services:[IndexService]
})
export class IndexModule{}