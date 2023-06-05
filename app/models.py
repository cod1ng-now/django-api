from django.db import models
from users.models import CustomUser
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    author= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = RichTextField()
    creates = models.DateTimeField(auto_now_add=True)
    updates = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return  "/"+str(self.id)+ "/"

    class Meta:
        ordering = ["-id"]