# Generated by Django 4.1.1 on 2022-10-09 13:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0005_alter_tag_tag_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_creation_date',
            field=models.DateTimeField(auto_created=True, blank=True, default=datetime.datetime(2022, 10, 9, 13, 19, 37, 774846, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
