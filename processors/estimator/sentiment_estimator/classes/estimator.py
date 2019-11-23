import spacy
from classes import entity

class Estimator:
    languages_dictionary = {
        'en': 'English'
    }
    def __init__(self, lang = 'en', analyze_algo = 'afinn'):
        self.lang = self.languages_dictionary[lang]
        self.analyze_algo = analyze_algo
        self.topics_nlp = spacy.load('en_core_web_sm')
    
    # def lemmatize_stemming(self,text):
        # token = WordNetLemmatizer().lemmatize(text, pos='v')
        # print(token)
        # return stemmer.stem(token)

    # Return estimation 
    # @param {string} text
    # @return {[topic: String]: Float}
    def estimate(self, text):
        text = (text)
        
        doc = self.topics_nlp(text)
        # Analyze syntax
        print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
        print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
        # Find named entities, phrases and concepts
        topics_dictionary = {}
        for doc_entity in doc.ents:
            entity_text = doc_entity.text.lower()
            if entity_text not in topics_dictionary:
                topics_dictionary[entity_text] = entity.Entity(entity_text, doc_entity.label_, len(doc.ents))
            topics_dictionary[entity_text].increment()
        topics_list = [topics_dictionary[topic].to_tuple() for topic in topics_dictionary]
        topics_list.sort(key = lambda topic: topic[2], reverse=True)
        print(topics_list)
        return topics_list[:5]

