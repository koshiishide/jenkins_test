import unittest
import app


class TestFlaskHello(unittest.TestCase):

    def setUp(self):
        self.app = flaskhello.app.test_client()

    def test_get(self):
        response = self.app.get('/')
        assert response.status_code == 200
        assert response.data == 'Hello, World!'


if __name__ == '__main__':
    unittest.main()