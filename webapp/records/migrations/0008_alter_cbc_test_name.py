# Generated by Django 4.1 on 2022-09-06 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0007_alter_bch_ref_alter_cbc_ref_alter_cbc_test_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cbc',
            name='test_name',
            field=models.CharField(choices=[('RED BLOOD CELLS', 'Red Blood Cells'), ('HEMOGLOBIN', 'Hemoglobin'), ('HEMATOCRIT', 'Hematocrit')], default='TEST NAME', max_length=80, verbose_name='Test name'),
        ),
    ]