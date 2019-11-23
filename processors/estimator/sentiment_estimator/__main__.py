import sys
from classes import estimator

lang = 'en'
text = None

if(len(sys.argv) > 1):
    text = sys.argv[1]
if(len(sys.argv) > 2):
    lang= sys.argv[2]

estimator = estimator.Estimator(lang)
print(estimator.estimate(text))