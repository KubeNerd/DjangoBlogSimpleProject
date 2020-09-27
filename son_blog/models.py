from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import  RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = RichTextField()
    content = RichTextUploadingField()
    author  = models.ForeignKey(User, on_delete=models.PROTECT)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Post'
