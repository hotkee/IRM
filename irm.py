"""
Simple image classification with Inception.

Run image classification with Inception trained on ImageNet 2012 Challenge data
set.

This program creates a graph from a saved GraphDef protocol buffer,
and runs inference on an input JPEG image. It outputs human readable
strings of the top 5 predictions along with their probabilities.

https://tensorflow.org/tutorials/image_recognition/
"""

import os

import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify

from common import config
from common.node_lookup import NodeLookup
from common.prediction import Prediction
from resources import utilities

# Build app
app = Flask(__name__)

# Creates graph from saved graph_def.pb.
with tf.gfile.FastGFile(config.MODEL_PATH, 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')

sess = tf.Session()
softmax = sess.graph.get_tensor_by_name('softmax:0')

# Creates node ID --> English string lookup.
node_lookup = NodeLookup()

# Allowable extensions
allowed_ext = {'jpg', 'jpeg'}


@app.route(config.IMAGE_CLASSIFIER_API, methods=['POST'])
def post():
    """
    Post method for uploading files and running classification on file

    Returns:
        Classification result in JSON
        See common.prediction object for example
    """

    upload = request.files['file']
    if upload and utilities.allowed_file(upload.filename):
        try:
            # Read and process file
            image_data = upload.stream.read()
            predictions = sess.run(softmax, {'DecodeJpeg/contents:0': image_data})
            predictions = np.squeeze(predictions)

            # Create json response
            top_k = predictions.argsort()[-config.NUM_TOP_PREDICTIONS:][::-1]
            human_string = node_lookup.id_to_string(top_k[0])
            score = predictions[top_k[0]]
            return jsonify(Prediction(human_string, score).jsonify())
        except:
            return jsonify({'error': 'error occured while processing file'}), 500
    else:
        return jsonify({'error': 'uploaded file must be in jpg/jpeg format and not null'}), 400


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 2475))
    app.run(host='0.0.0.0', port=port, debug=True)
