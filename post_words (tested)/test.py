import unittest

import task

class TestPostWordsMethods(unittest.TestCase):

    def setUp(self):
        self.app = task.app.test_client()
        self.words = self.app.post('/', json={"word": "one"})
        self.words = self.app.post('/', json={"word": "two"})

    def test_foo_page_is_available(self):
        self.assertEqual(
            self.words.status_code, 200,
            'Проверьте, что адрес "/" доступен и поддерживает POST запросы')

    def test_foo_page_returns_json(self):
        self.assertTrue(
            self.words.is_json,
            ('Проверьте что при запросе на страницу "/"'
             ' данные возвращаются в формате json'))

    def test_foo_page_result_is_dict(self):
        self.assertTrue(
            isinstance(self.words.json, list),
            ('Проверьте что при запросе на страницу "/"'
             'возвращаемые данные являются словарем'))

    def test_foo_page_returns_correct_key(self):
        self.assertTrue(
            "one" in self.words.json and "two" in self.words.json,
            ('Проверьте что при обращении на страницу "/foo"'
             'в возращаемом списке лежат правильные слова'))

