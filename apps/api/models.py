from django.db import models
from apps.users.models import User

# Create your models here.

class Board(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    contents = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    class Meta:
        db_table = 'board'
    