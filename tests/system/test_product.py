from unittest import TestCase

from mypage2 import app
class ProductTest(TestCase):
    def test_welcome(self):
        with welcome.test_client() as c:
            resp = c.get('/api/products')
            self.assertEqual(resp.status_code,200)
            self.asserEqual(json.loads(resp.get_data()) , [{

            }])