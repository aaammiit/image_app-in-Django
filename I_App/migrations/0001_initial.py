# Generated by Django 5.0.3 on 2024-03-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('image_name', models.CharField(max_length=100)),
                ('image_desc', models.CharField(max_length=100)),
            ],
        ),
    ]
