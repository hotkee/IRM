import unittest

import IRM


class TestClassifierAPI(unittest.TestCase):
    def setUp(self):
        self.app = IRM.app.test_client()

    def test_full_classification_upload(self):
        files = {'file': (open('../images/cropped_panda.jpg', 'rb'), '21T03NAPE7L._AA75_.jpg')}
        response = self.app.post('/team-gitmo/services/image/classify', data=files)
        assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
