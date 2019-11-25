import sys
from src.classes import estimator

lang = 'en'
file_path = './mock/article.txt'
text = None
topics = ''

if(len(sys.argv) > 1):
    file_path = sys.argv[1]
if(len(sys.argv) > 2):
    lang = sys.argv[2]


with open(file_path,'r') as reader:
    text = reader.read()

estimator = estimator.Estimator(lang)
print(estimator.estimate(text))