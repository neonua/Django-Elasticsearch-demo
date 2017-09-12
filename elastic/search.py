from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Keyword, Search, tokenizer, analyzer, Q
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

# creating connection with ES
connections.create_connection(hosts=['127.0.0.1:9200'], timeout=20)

# simple analyzed. We describe the tokenyzers and filters
# trigram and nGram search are partial word structure
# https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-tokenizers.html
my_analyzer = analyzer('my_analyzer',
                       filter=['lowercase', 'standard', 'snowball'],
                       tokenizer=tokenizer('standard'),
                       char_filter=["html_strip"])


class DocumentIndex(DocType):
    '''
    Mapping DocType model-like wrapper around model Document
    '''
    title = Text(analyzer=my_analyzer)
    description = Text(analyzer=my_analyzer)
    text = Text(analyzer=my_analyzer)
    added_date = Date()
    published_date = Date()

    def is_published(self):
        return self.title

    class Meta:
        '''
        name of index in ES
        '''
        index = 'document'


def bulk_indexing():
    '''
    Bulk indexing of data
    '''
    # create index document
    DocumentIndex.init()
    es = Elasticsearch()
    # index all data in database
    bulk(client=es, actions=(b.indexing() for b in models.Document.objects.all().iterator()))


def search(text):
    '''
    https://elasticsearch-dsl.readthedocs.io/en/latest/search_dsl.html#the-search-object
    '''
    s = Search().query('multi_match', query=text, fields=['text', 'title^3', 'description^2'])
    response = s.execute()
    return response
