from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=30)
    int = models.IntegerField()

class Article(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    publish_date = models.DateField(u'发表时间', auto_now_add=True, editable=True)
    update_date = models.DateTimeField(u'更新时间', auto_now_add=True, null=True)
    def __str__(self):
        return self.title