# Generated by Django 4.1.1 on 2022-10-03 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Articles', '0009_additionaluserinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionaluserinfo',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
