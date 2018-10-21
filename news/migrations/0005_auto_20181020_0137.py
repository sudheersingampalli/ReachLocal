# Generated by Django 2.0.3 on 2018-10-19 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20181020_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='published_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='source_name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
