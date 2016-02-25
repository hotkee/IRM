import unittest

import tpc


class TestClassifierAPI(unittest.TestCase):
    def setUp(self):
        self.app = tpc.app.test_client()

    def test_full_classification_upload(self):
        files = {'file': (open('../images/cropped_panda.jpg', 'rb'), '21T03NAPE7L._AA75_.jpg')}
        response = self.app.post('/tpc/v1.0/imagenet/classification', data=files)
        print response


if __name__ == '__main__':
    unittest.main()
