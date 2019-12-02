import ktrain
from ktrain import text

from sklearn.datasets import fetch_20newsgroups


class SentimentEstimator:

    def __init__(self, language = 'english'):
        self.train(language)

    def train(self, language):
        categories = ['alt.atheism', 'soc.religion.christian','comp.graphics', 'sci.med']
        train_b = fetch_20newsgroups(subset='train',categories=categories, shuffle=True, random_state=42)
        test_b = fetch_20newsgroups(subset='test',categories=categories, shuffle=True, random_state=42)
        print('size of training set: %s' % (len(train_b['data'])))
        print('size of validation set: %s' % (len(test_b['data'])))
        print('classes: %s' % (train_b.target_names))

        x_train = train_b.data
        y_train = train_b.target
        x_test = test_b.data
        y_test = test_b.target
        (x_train,  y_train), (x_test, y_test), preproc = text.texts_from_array(x_train=x_train, y_train=y_train, 
       x_test=x_test, y_test=y_test,class_names=train_b.target_names,preprocess_mode='bert',maxlen=350,max_features=35000)

        model = text.text_classifier('bert', train_data=(x_train, y_train), preproc=preproc)
        learner = ktrain.get_learner(model, train_data=(x_train, y_train), batch_size=6)
        learner.fit_onecycle(2e-5, 4)
        learner.validate(val_data=(x_test, y_test), class_names=train_b.target_names)
        self.predictor = ktrain.get_predictor(learner.model, preproc)
        

    def estimate(self, text):
       print('predict', self.predictor.predict([text]))
       return sentiment, accuracy
