# Generated by Django 4.1.5 on 2023-01-31 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_chef_id_alter_chef_user_ingredient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='user',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='chef',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.chef'),
        ),
    ]
