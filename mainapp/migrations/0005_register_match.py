# Generated by Django 3.1.7 on 2021-03-30 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20210330_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register_Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temail', models.CharField(max_length=40)),
                ('match_name', models.CharField(max_length=30)),
            ],
        ),
    ]
