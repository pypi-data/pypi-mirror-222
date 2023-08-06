from setuptools import setup
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='censoredzz',
    version='1.0.4',
    description='Python package for censoring profane words in Nepali-(Roman) text',
    author='Kuber Budhathoki',
    author_email='koobear99@gmail.com',
    url='https://github.com/12-Twelvve/pypi_censored_text',
    packages=['censoredzz'],
    package_data={
        'censoredzz': ['models/rf_model.pkl', 'models/vocabulary.pkl'],
    },
    install_requires=[
        'regex',
        'sklearn',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
) 