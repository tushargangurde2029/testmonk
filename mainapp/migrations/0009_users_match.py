# Generated by Django 3.2 on 2021-05-07 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20210331_0018'),
    ]

    operations = [
        migrations.CreateModel(
            name='users_match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(default='Hello', max_length=30)),
                ('mobile_number', models.CharField(max_length=12)),
                ('payment', models.CharField(default='no', max_length=30)),
            ],
        ),
    ]
