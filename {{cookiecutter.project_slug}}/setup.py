from setuptools import setup, find_packages

setup(
    name='{{cookiecutter.project_slug}}',
    long_description='{{cookiecutter.project_short_description }}',
    version='{{cookiecutter.version}}',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)