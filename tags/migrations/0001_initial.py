# Generated by Django 4.1.1 on 2022-09-19 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tag_name', models.CharField(max_length=32, unique=True)),
            ],
        ),
    ]
