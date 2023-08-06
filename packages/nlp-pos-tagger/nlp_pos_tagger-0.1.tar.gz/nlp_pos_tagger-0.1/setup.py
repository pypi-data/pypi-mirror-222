from setuptools import setup, find_packages

setup(
    name='nlp_pos_tagger',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'nltk',
    ],
    author='Your Name',
    author_email='your@email.com',
    description='A simple NLP library for POS tagging',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your_username/nlp_pos_tagger',
)
