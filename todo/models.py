from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodoItem(models.Model):
    todo_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    title = models.TextField(max_length=100)
    desc = models.TextField()
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
