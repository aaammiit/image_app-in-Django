from django.db import models
from django import forms

# Create your models here.

class Image(models.Model):
    image=models.ImageField(upload_to='images')
    image_name=models.CharField(max_length=100)
    image_desc=models.CharField(max_length=10000)


class IForm(forms.ModelForm):
    class Meta:
        model=Image
        fields='__all__'
