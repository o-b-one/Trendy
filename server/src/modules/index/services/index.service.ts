import { Injectable } from "@sugoi/server";
import { SocketOn, SocketHandler } from "@sugoi/socket";

@Injectable()
export class IndexService {

    constructor(){
    }

    @SocketOn("message")
    static socketEventHandler(socket,message){
        SocketHandler.getHandler().getServer().emit("new-message", message)
    }

}