# Generated by Django 5.1.1 on 2024-10-10 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0001_initial'),
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='categories',
            field=models.ManyToManyField(related_name='tasks', to='Category.categorymodel'),
        ),
    ]
