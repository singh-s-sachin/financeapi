# Generated by Django 2.2.2 on 2019-07-26 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190726_0606'),
    ]

    operations = [
        migrations.CreateModel(
            name='create_fd',
            fields=[
                ('mobile', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('amount', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=5)),
                ('maturity', models.CharField(max_length=10)),
            ],
        ),
    ]