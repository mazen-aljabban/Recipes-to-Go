# Generated by Django 4.1.5 on 2023-01-29 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_chef_options_rename_birth_data_chef_birth_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chef',
            options={'ordering': ['user__first_name', 'user__last_name']},
        ),
    ]
