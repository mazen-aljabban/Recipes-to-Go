# Generated by Django 4.1.5 on 2023-02-01 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_recipe_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='featured_collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.collection'),
        ),
        migrations.AddField(
            model_name='collection',
            name='featured_recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.recipe'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='collections', to='core.category'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='collection',
            field=models.ManyToManyField(blank=True, related_name='recipes', to='core.collection'),
        ),
    ]
