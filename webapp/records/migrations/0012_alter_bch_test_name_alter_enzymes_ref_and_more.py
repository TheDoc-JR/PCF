# Generated by Django 4.1 on 2022-09-06 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0011_alter_bch_ref_alter_bch_test_units'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bch',
            name='test_name',
            field=models.CharField(choices=[('Glucose', 'Glucose'), ('Creatinine', 'Creatinine'), ('Uric acid', 'Uric acid')], default='', max_length=80, verbose_name='Test name'),
        ),
        migrations.AlterField(
            model_name='enzymes',
            name='ref',
            field=models.CharField(choices=[('(5-40)', '(5-40)'), ('(5-41)', '(5-41)'), ('(<60)', '(<60)')], default='', max_length=200, verbose_name='Reference values'),
        ),
        migrations.AlterField(
            model_name='enzymes',
            name='test_name',
            field=models.CharField(choices=[('AST', 'AST'), ('ALT', 'ALT'), ('Gamma-GT', 'Gamma-GT')], default='', max_length=80, verbose_name='Test name'),
        ),
        migrations.AlterField(
            model_name='enzymes',
            name='test_units',
            field=models.CharField(choices=[('UI/L', 'UI/L')], default='UI/L', max_length=200, verbose_name='Units'),
        ),
    ]