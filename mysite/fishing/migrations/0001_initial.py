# Generated by Django 4.2.10 on 2024-02-11 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('english', models.CharField(max_length=30)),
                ('chinese', models.CharField(max_length=30)),
            ],
        ),
    ]
