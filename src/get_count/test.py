from utils import SkyProTestCase

from .task import app


class TestCountMethods(SkyProTestCase):

    def setUp(self):
        self.app = app.test_client()
        self.result = self.app.get('/count-users', follow_redirects=True)

    def test_avail(self):
        self.assertEqual(self.result.status_code, 200, 'Проверьте, что адрес "count-users" доступен')

    def test_value(self):
        self.assertEqual(self.result.json.get("count"), 4, 'Проверьте, что количество пользователей возвращается верно')
