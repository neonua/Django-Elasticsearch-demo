from django.db import models
from django_elasticsearch.models import EsIndexable
# Create your models here.
from elastic.search import DocumentIndex

RATE_CHOICE = (
    ('1', 'Bad'),
    ('5', 'Good'),
)


class Document(models.Model):
    title = models.CharField('Title', max_length=64, null=False, blank=False)
    description = models.CharField('Description', max_length=256, null=True, blank=True)
    text = models.TextField('Text', null=True, blank=False)
    rate = models.CharField(max_length=1, choices=RATE_CHOICE)
    added_date = models.DateTimeField('Add date', auto_now_add=True)
    published_date = models.DateTimeField('Published date', auto_now=True)

    def indexing(self):
        obj = DocumentIndex(
            meta={'id': self.id},
            title=self.title,
            description=self.description,
            text=self.text,
            rate=self.rate
        )
        obj.save()
        return obj.to_dict(include_meta=True)

    def __str__(self):
        return self.title
