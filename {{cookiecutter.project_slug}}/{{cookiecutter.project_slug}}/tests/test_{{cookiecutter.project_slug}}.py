import unittest

from main import app


class {{cookiecutter.project_slug.replace('_', ' ').title().replace(' ', '')}}TestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Hello World!', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
