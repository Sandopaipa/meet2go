# Generated by Django 4.1.1 on 2022-10-31 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0016_alter_tag_tag_creation_date'),
        ('user_profile', '0004_profile_followers_alter_profile_follows'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileTagList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.profile')),
                ('tag', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='tags.tag')),
            ],
        ),
    ]