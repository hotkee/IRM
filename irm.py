import os

import tensorflow as tf
from flask import Flask
from flask_restful import Api

from resources.classifier_api import ClassifierAPI
from common import config

# Build app
app = Flask(__name__)
api = Api(app)

# Add resources
api.add_resource(ClassifierAPI, config.IMAGENET_CLASSIFIER_API)


@app.before_first_request
def create_graph():
    """
    Creates a graph from saved GraphDef file and returns a saver.
    """

    # Creates graph from saved graph_def.pb.
    with tf.gfile.FastGFile(os.path.join(config.MODEL_DIR, 'classify_image_graph_def.pb'), 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())

        # Sets graph as default graph
        # Return variable ignored
        tf.import_graph_def(graph_def, name='')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
