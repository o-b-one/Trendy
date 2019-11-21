import {
    Controller,
    RequestBody,
    HttpPost
 } from "@sugoi/server";
import { ProcessorService } from "../services/processor.service";

@Controller('/processor')
export class ProcessorController {

    constructor(
        private processorService:ProcessorService
    ){
    }


    @HttpPost("/emotion")
    async index(@RequestBody() body:{text: string}){
        const estimation = await this.processorService.estimateEmotion(body.text, 'Apple');
        return {estimation};
    }

}