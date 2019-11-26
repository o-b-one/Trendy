import re
import spacy
import pandas as pd
from src.classes import entity, sentiment_estimator



TRASHOLD = .25


FILTERED_LABELS = [
    'ORDINAL',
    'QUANTITY',
    'MONEY',
    'PERCENT',
    'TIME',
    'DATE',
    'CARDINAL',
    'LANGUAGE',
    'LOC'
]

class Estimator:
    languages_dictionary = {
        'en': 'English'
    }
    def __init__(self, lang = 'en', analyze_algo = 'afinn'):
        self.lang = self.languages_dictionary[lang]
        self.analyze_algo = analyze_algo
        self.nlp = spacy.load('en_core_web_sm')
        self.sentiment_estimator = sentiment_estimator.SentimentEstimator()
    
    # def lemmatize_stemming(self,text):
        # token = WordNetLemmatizer().lemmatize(text, pos='v')
        # print(token)
        # return stemmer.stem(token)


    def build_pipeline(self):
        self.nlp.add_pipe(self.nlp.create_pipe('sentencizer'))

    
    def analyze_paragraph(self, paragraph, topics_dictionary):
        text = (paragraph)
        doc = self.nlp(text)
        paragraph_topics = {}
        # Analyze syntax
        #print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
        #print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

        # Find named entities, phrases and concepts
        
        filtered_entities = {entity.text.lower() for entity in doc.ents if entity.label_ not in FILTERED_LABELS }
        total_entities = len(filtered_entities)
        
        for doc_entity in doc.ents:
            entity_text = doc_entity.text.lower()
            if entity_text not in topics_dictionary:
                topics_dictionary[entity_text] = entity.Entity(entity_text, doc_entity.label_, doc_entity.label, total_entities)
            if entity_text not in paragraph_topics:
                paragraph_topics[entity_text] = entity.Entity(entity_text, doc_entity.label_, doc_entity.label, total_entities)
                topics_dictionary[entity_text].add_to_total(total_entities)

            if topics_dictionary[entity_text].label not in FILTERED_LABELS:
                topics_dictionary[entity_text].increment()
                paragraph_topics[entity_text].increment()
        
        sentiment, accuracy = self.sentiment_estimator.estimate(paragraph)
        return Estimator.sort_topics(Estimator.normalize_results(paragraph_topics)), sentiment, accuracy


       

    # Return estimation 
    # @param {string} text
    # @return {[topic: String]: Float}
    def estimate(self, text):
        topics_dictionary = {}

        # Get paragraphs from text
        paragraphs = [match.group(0) for match in re.finditer('(.)+\n*|\n(.)+/g', text)]
        print(len(paragraphs))

        paragraphs_results = []
        for paragraph in paragraphs:
            paragraph_topics, sentiment, accuracy = self.analyze_paragraph(paragraph, topics_dictionary)
            paragraphs_results.append((paragraph_topics,sentiment, accuracy))

        topics_list = Estimator.normalize_results(topics_dictionary)
        Estimator.sort_topics(topics_list)
        print(pd.DataFrame(paragraphs_results, columns=['Results', 'Sentiment', 'Accuracy']))
        return topics_list[:5]


    @staticmethod
    def sort_topics(topics_tuple):
        topics_tuple.sort(key = lambda topic: topic[5], reverse = True)
        return topics_tuple

    @staticmethod
    def normalize_results(topics_dictionary):
        return [topics_dictionary[topic].to_tuple() for topic in topics_dictionary if topics_dictionary[topic].get_ratio() >= TRASHOLD]    
   