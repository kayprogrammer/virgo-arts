# Generated by Django 3.1.5 on 2021-12-22 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0003_auto_20211222_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='description',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='art',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
