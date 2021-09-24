import unittest


class StatMixin:
    def send_stat(self, result):
        if result.wasSuccessful():
            pass


class SkyProTestCase(StatMixin, unittest.TestCase):
    def run(self, *args, **kwargs):
        result = super().run(*args, **kwargs)
        self.send_stat(result)
        return result
