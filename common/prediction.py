class Prediction(object):
    """
    Prediction wrapper for predictions returned from TensorFlow
    """

    def __init__(self, prediction, confidence):
        """
        Constructor with prediction and associated confidence

        Returns:
            PredictionObject
        """

        self.prediction = prediction
        self.confidence = confidence

    def get_prediction(self):
        """
        Get prediction

        Returns:
            Prediction String
        """

        return self.prediction

    def get_score(self):
        """
        Get score

        Returns:
            Confidence Float
        """

        return self.confidence

    def jsonify(self):
        """
        Jsonify object

        Returns:
            Jsonified object
        """

        return {'prediction': self.prediction, 'confidence': float(self.confidence)}