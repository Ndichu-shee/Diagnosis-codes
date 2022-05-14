# Generated by Django 4.0.4 on 2022-05-14 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosiscodes',
            name='icd_code',
            field=models.CharField(choices=[('icd_9', 'ICD_9 2008'), ('icd_10', 'ICD_10 2015'), ('icd_11', 'ICD_11 2022')], default='icd_10', max_length=255),
        ),
    ]