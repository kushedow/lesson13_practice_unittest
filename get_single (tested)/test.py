import unittest

import task


class TestDoubleMethods(unittest.TestCase):

    def setUp(self):
        self.app = task.app.test_client()
        self.result = self.app.get('/users/1', follow_redirects=True)


    def test_foo_page_is_available(self):
        self.assertEqual(
            self.result.status_code, 200,
            'Проверьте, что адрес "/users/1" доступен')

    def test_foo_page_returns_json(self):
        self.assertTrue(
            self.result.is_json,
            ('Проверьте что при запросе на страницу "/users/1"'
             ' данные возвращаются в формате json'))

    def test_foo_page_result_is_dict(self):
        self.assertTrue(
            isinstance(self.result.json, dict),
            ('Проверьте что при запросе на страницу "/users/1"'
             'возвращаемые данные являются словарем'))


    def test_returns_correct_value(self):
        data = self.result.json
        self.assertEqual(data.get('name'), "Alice", 'Проверьте что имя пользователя возвращается корректно')
        self.assertEqual(data.get('age'), 16, 'Проверьте что возраст пользователя возвращается корректно')
        self.assertEqual(data.get('location'), "Moscow", 'Проверьте что местоположение пользователя возвращается корректно')


class Test404Methods(unittest.TestCase):

    def setUp(self):
        self.app = task.app.test_client()
        self.result = self.app.get('/users/0', follow_redirects=True)


    def test_404(self):
         self.assertEqual(
            self.result.status_code, 404, ('При несуществующем пользователе должна падать 404')
         )
