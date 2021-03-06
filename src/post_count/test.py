from utils import SkyProTestCase

from .task import app, status


class TestDoubleMethods(SkyProTestCase):

    def setUp(self):
        self.app = app.test_client()

        self.result = self.app.post('/count/', follow_redirects=True, data={})
        self.result = self.app.post('/count/', follow_redirects=True, data={})

    def test_foo_page_is_available(self):
        self.assertEqual(
            self.result.status_code, 200,
            'Проверьте, что адрес "/count" доступен')

    def test_foo_page_returns_json(self):
        self.assertTrue(
            self.result.is_json,
            ('Проверьте что при запросе на страницу "/count"'
             ' данные возвращаются в формате json'))

    def test_foo_page_result_is_dict(self):
        self.assertTrue(
            isinstance(self.result.json, dict),
            ('Проверьте что при запросе на страницу "/count"'
             'возвращаемые данные являются словарем'))

    def test_foo_page_returns_correct_key(self):
        self.assertTrue(
            "count" in self.result.json.keys(),
            ('Проверьте что при обращении на страницу "/count"'
             'в возвращаемом словаре есть ключ count'))

    def test_foo_page_returns_correct_value(self):
        self.assertEqual(
            self.result.json.get('count'), status.get("count"),
            'Проверьте что запросы считаются верно')
