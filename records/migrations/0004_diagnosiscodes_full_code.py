# Generated by Django 4.0.4 on 2022-04-28 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_alter_diagnosiscodes_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosiscodes',
            name='full_code',
            field=models.CharField(default='code', max_length=10),
            preserve_default=False,
        ),
    ]
