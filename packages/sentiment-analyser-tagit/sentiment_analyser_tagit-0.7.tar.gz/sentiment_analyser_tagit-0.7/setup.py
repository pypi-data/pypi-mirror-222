from setuptools import setup, find_packages
  
setup(
    name='sentiment_analyser_tagit',
    version='0.7',
    description='A sentiment analysis tool for Tagit. Solely for internal use.',
    author='Adithya Narayanan',
    author_email='adithya.narayanan01@gmail.com',
    packages=find_packages("Sentiment analysis"),
    install_requires=[
        'app_store_scraper',
        'fpdf',
        'datetime',
        'llama_index',
        'openai'
    ],
)