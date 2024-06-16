# Generated by Django 5.0.6 on 2024-06-16 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_userprofile_avatar_userprofile_nickename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='nickename',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]