import random
from datetime import datetime, timedelta
from elasticsearch import Elasticsearch
from faker import Faker

es = Elasticsearch(
    'http://localhost:9200',
    basic_auth=('elastic', 'REPLACE ME'),
)

# Faker instance to generate random data
fake = Faker()

# Loop to create 1000 records
for i in range(1000):
    # Generate random data for document
    author = fake.name()
    text = fake.text()
    # You can adjust the days and seconds parameters to get the range of timestamps you need
    random_time = datetime.now() - timedelta(days=random.randint(0, 365), seconds=random.randint(0, 86400))
    
    # Create document
    doc = {
        'author': author,
        'text': text,
        'timestamp': random_time,
    }
    
    # Index document in Elasticsearch
    resp = es.index(index="test-index", document=doc)

# Maybe add some success message
print("1000 records successfully created.")