# Generated by Django 4.1.7 on 2023-04-03 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_alter_users_password'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='UserSystem',
        ),
    ]
