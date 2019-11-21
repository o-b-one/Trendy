import { Injectable } from "@sugoi/server";
import * as NLP from "natural";


@Injectable()
export class ProcessorService {
    private analyzer = new NLP.SentimentAnalyzer('English', NLP.ProterStemmer, "afinn");
    private sentenceTokenizer = new NLP.SentenceTokenizer();
    private wordTokenizer = new NLP.WordTokenizer();
    // private sentenceAnalyzer = new NLP.SentenceAnalyzer();

    constructor(){
    }


    async estimateEmotion(text:string, subject?: string): Promise<number>{
        // todo: Check emotion per subject for understand the Subject of the emotion.
        let estimation = 0, unnutral = 0;
        const sentences = this.sentenceTokenizer.tokenize(text);
        if( sentences.length === 0 ){
            return estimation;
        }
        // // const corpus = new NLP.Corpus(text, 1, NLP.Sentence);
        // // console.log(corpus)

        try{
        console.log('text',text);
            console.log("sentences", sentences);
            await Promise.all(
                sentences.map( async sentence => {
                    const tokens: string[] = this.wordTokenizer.tokenize(sentence);
                    // const analyzer = await new Promise(res => new NLP.SentenceAnalyzer(pos,res));
                    // console.log(analyzer);
                    const tokenEstimation = this.analyzer.getSentiment(tokens);
                    console.log(sentence,tokens,tokenEstimation);
                    estimation += tokenEstimation;
                    if(tokenEstimation !== 0){
                        unnutral++;
                    }
                })
            );
        }catch(e){
            console.error(e);
            throw e;
        }
        return estimation / (unnutral || 1);
    }


}