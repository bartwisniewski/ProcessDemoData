# Generated by Django 4.0.5 on 2022-06-09 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0003_alter_automation_connections'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automation',
            name='connections',
            field=models.JSONField(default=dict),
        ),
    ]
