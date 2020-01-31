from django.db import models

# Create your models here.


class Entry(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    related_link_name = models.CharField(max_length=200, blank=True)
    posted_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

        def summery(self):
            if len(self.content) > 100:
                return self.content[:100] + '...'
            return self.content
