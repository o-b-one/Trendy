import { ServerModule } from "@sugoi/server"
import { ProcessorController } from "./controllers/processor.controller";
import { ProcessorService } from "./services/processor.service";

@ServerModule({
    modules:[],
    controllers:[ProcessorController],
    services:[ProcessorService]
})
export class ProcessorModule{}