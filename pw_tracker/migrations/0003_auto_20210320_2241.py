# Generated by Django 3.1.7 on 2021-03-20 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pw_tracker', '0002_auto_20210320_2229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracker',
            old_name='owner',
            new_name='user',
        ),
    ]
