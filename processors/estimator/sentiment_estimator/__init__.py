import sys
from classes import estimator


text = sys.argv[1]
if(len(sys.argv) > 2):
    lang= sys.argv[2]

estimator = Estimator(lang)
print(estimator.estimate(text))