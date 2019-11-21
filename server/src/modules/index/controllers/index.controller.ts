import {
    Controller,
    HttpGet,
    RequestParam,
    Authorized
 } from "@sugoi/server";
import { IndexService } from "../services/index.service";

@Controller('/index')
@Authorized()
export class IndexController {

    constructor(
        private indexService:IndexService
    ){
    }


    @HttpGet("/:payload?")
    async index(@RequestParam("payload") payload:string){
        const responseMsg = "index is ready!";
        return payload
                ? `${responseMsg} got payload ${payload}`
                : `${responseMsg}`;
    }

}