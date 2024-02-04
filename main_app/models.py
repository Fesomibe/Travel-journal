from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Journal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=350)
    date = models.DateField('Date')
    content = models.TextField(default='')
    location = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})  # Use 'pk' instead of 'journal_id'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    journal = models.ForeignKey('Journal', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.created_at}'