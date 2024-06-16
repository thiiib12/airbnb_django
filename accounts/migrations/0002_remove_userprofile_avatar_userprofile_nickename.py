# Generated by Django 5.0.6 on 2024-06-16 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='avatar',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='nickename',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
