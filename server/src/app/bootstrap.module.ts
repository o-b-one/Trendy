import { ServerModule } from "@sugoi/server"
import { IndexModule } from "../modules/index/index.module";
import { ProcessorModule } from "../modules/processor/processor.module";

@ServerModule({
    modules:[IndexModule, ProcessorModule],
    controllers:[],
    services:[]

})
export class BootstrapModule{}