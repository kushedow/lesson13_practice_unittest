import unittest
import task


class TestCountMethods(unittest.TestCase):

    def test_count_users(self):
        task.app.config['TESTING'] = True
        app = task.app.test_client()
        result = app.get('/count-users')
        self.assertEqual(result.status_code, 200, 'Проверьте, что адрес "count-users" доступен')

if __name__ == '__main__':
    unittest.main()
