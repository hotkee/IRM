import os

# Required Files:
#
# classify_image_graph_def.pb:
#   Binary representation of the GraphDef protocol buffer.
#
# imagenet_synset_to_human_label_map.txt:
#   Map from synset ID to a human readable string.
#
# imagenet_2012_challenge_label_map_proto.pbtxt:
#   Text representation of a protocol buffer mapping a label to synset ID.

# Relative path to directory which contains:
#   classify_image_graph_def.pb
#   imagenet_synset_to_human_label_map.txt
#   imagenet_2012_challenge_label_map_proto.pbtxt

RELATIVE_MODEL_DIR = 'models'

# Absolute path to models
MODEL_DIR = os.path.join(os.path.dirname(__file__), os.pardir, RELATIVE_MODEL_DIR)

# Classification model path
CLASSIFIED_MODEL_PATH = os.path.join(MODEL_DIR, 'classify_image_graph_def.pb')

# Label path
LABEL_PATH = os.path.join(MODEL_DIR, 'imagenet_2012_challenge_label_map_proto.pbtxt')

# Label association path
UID_PATH = os.path.join(MODEL_DIR, 'imagenet_synset_to_human_label_map.txt')

# Classifier API path
IMAGENET_CLASSIFIER_API = '/team-gitmo/services/imagenet/classify'

# Display this many predictions
NUM_TOP_PREDICTIONS = 1

# pylint: disable=line-too-long
DATA_URL = 'http://download.tensorflow.org/models/image/imagenet/inception-2015-12-05.tgz'
# pylint: enable=line-too-long
