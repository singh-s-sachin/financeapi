# Generated by Django 2.2.2 on 2019-07-26 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='tid',
            field=models.CharField(max_length=150),
        ),
    ]