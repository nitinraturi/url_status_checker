# Generated by Django 3.1.1 on 2020-09-11 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlschecker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='status_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]