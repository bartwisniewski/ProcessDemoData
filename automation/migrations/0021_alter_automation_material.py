# Generated by Django 4.0.5 on 2022-06-20 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0020_automation_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automation',
            name='material',
            field=models.JSONField(default=[0, 0, 0]),
        ),
    ]
