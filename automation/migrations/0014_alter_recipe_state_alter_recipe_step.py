# Generated by Django 4.0.5 on 2022-06-13 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0013_recipe_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='state',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='step',
            field=models.IntegerField(default=0),
        ),
    ]
