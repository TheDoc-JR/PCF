# Generated by Django 4.1 on 2022-09-03 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cbc',
            name='test_units',
            field=models.CharField(max_length=200),
        ),
    ]