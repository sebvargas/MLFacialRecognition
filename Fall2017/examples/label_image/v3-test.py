import os
from label_image import classify

classify('tmp/output_graph.pb', 'tmp/output_labels.txt', 'Mul', 'final_result', 128, 128, 'test/left_profile.jpg')

