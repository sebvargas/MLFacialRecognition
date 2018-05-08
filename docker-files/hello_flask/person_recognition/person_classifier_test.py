import os
from person_classifier import classify_person
from operator import itemgetter

results = classify_person('tmp/output_graph.pb', 'tmp/output_labels.txt', 'Mul', 'final_result', 128, 128, 'test/left_profile.jpg')

print results
print


print max(results, key=itemgetter(1))
