# Generated by Django 4.1.1 on 2022-10-31 20:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0015_alter_tag_tag_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_creation_date',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2022, 10, 31, 23, 54, 16, 584091)),
        ),
    ]
