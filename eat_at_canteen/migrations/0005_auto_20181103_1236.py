# Generated by Django 2.0.7 on 2018-11-03 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eat_at_canteen', '0004_auto_20181103_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Add_a_Review',
            new_name='Review',
        ),
    ]
