# Generated by Django 4.2.1 on 2023-06-28 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_login', '0005_userprofile_describtion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='create_date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='describtion',
            new_name='description',
        ),
    ]