# Generated by Django 3.1.1 on 2020-09-28 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
