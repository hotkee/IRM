from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
from flask_restful import request, Resource

from common import config
from common.node_lookup import NodeLookup
from common.prediction import Prediction

"""
Simple image classification with Inception.

Run image classification with Inception trained on ImageNet 2012 Challenge data
set.

This program creates a graph from a saved GraphDef protocol buffer,
and runs inference on an input JPEG image. It outputs human readable
strings of the top 5 predictions along with their probabilities.

https://tensorflow.org/tutorials/image_recognition/
"""


class ClassifierAPI(Resource):

    def __init__(self):
        super(ClassifierAPI, self).__init__()

        # Creates node ID --> English string lookup.
        self.node_lookup = NodeLookup()

        # Allowable extensions
        self.allowed_ext = {'jpg', 'jpeg'}

    def post(self):
        """
        Post method for uploading files and running classification on file

        Returns:
            Classification result in JSON

            i.e
            {
                'prediction': ${classification result},
                'confidence': ${score}
            }
        """
        f = request.files['file']
        if f and self.allowed_file(f.filename):
            try:
                return self.run_inference_on_image(f.stream), 200
            except:
                return {'error': 'error occured while processing file'}, 500
        else:
            return {'error': 'uploaded file must be in jpg/jpeg format and not null'}, 400

    def allowed_file(self, filename):
        """
        Determines if filename is allowed
        Args:
            filename: filename of uploaded file

        Returns:
            True if filename is allowed
            False otherwise

        """
        return '.' in filename and filename.rsplit('.', 1)[1] in self.allowed_ext

    def run_inference_on_image(self, image):
        """
        Runs inference on an uploaded image.

        Args:
          image: Uploaded image.

        Returns:
          Nothing
        """

        image_data = image.read()

        with tf.Session() as sess:
            # Some useful tensors:
            # 'softmax:0': A tensor containing the normalized prediction across
            #   1000 labels.
            # 'pool_3:0': A tensor containing the next-to-last layer containing 2048
            #   float description of the image.
            # 'DecodeJpeg/contents:0': A tensor containing a string providing JPEG
            #   encoding of the image.
            # Runs the softmax tensor by feeding the image_data as input to the graph.
            softmax_tensor = sess.graph.get_tensor_by_name('softmax:0')
            predictions = sess.run(softmax_tensor,
                                   {'DecodeJpeg/contents:0': image_data})
            predictions = np.squeeze(predictions)

            # Create json response
            top_k = predictions.argsort()[-config.NUM_TOP_PREDICTIONS:][::-1]
            for node_id in top_k:
                human_string = self.node_lookup.id_to_string(node_id)
                score = predictions[node_id]
                return Prediction(human_string, score).jsonify()
