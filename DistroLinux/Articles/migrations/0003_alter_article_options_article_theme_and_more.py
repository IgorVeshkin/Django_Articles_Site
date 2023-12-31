# Generated by Django 4.1.1 on 2022-09-09 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0002_article_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-creation_time']},
        ),
        migrations.AddField(
            model_name='article',
            name='theme',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='static/images/uploaded/%Y/%m/%d/'),
        ),
    ]
