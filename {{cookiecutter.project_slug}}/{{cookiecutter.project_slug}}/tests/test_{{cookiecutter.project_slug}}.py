import unittest

import {{cookiecutter.project_slug}}


class {{cookiecutter.project_slug.replace('_', ' ').title().replace(' ', '')}}TestCase(unittest.TestCase):

    def setUp(self):
        {{cookiecutter.project_slug}}.app.testing = True
        self.app = {{cookiecutter.project_slug}}.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to {{cookiecutter.project_slug}}', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
