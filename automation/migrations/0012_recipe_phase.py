# Generated by Django 4.0.5 on 2022-06-13 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0011_alter_pid_actuator_alter_pid_measurement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('step', models.IntegerField()),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='automation.plant')),
            ],
            options={
                'ordering': ['plant'],
            },
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase_num', models.IntegerField()),
                ('index', models.IntegerField()),
                ('parameters', models.JSONField()),
                ('end_cond', models.IntegerField(default=0)),
                ('in_background', models.BooleanField(default=False)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phases', to='automation.recipe')),
            ],
            options={
                'ordering': ['recipe'],
            },
        ),
    ]
