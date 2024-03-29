# Generated by Django 4.0.5 on 2022-06-22 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0022_alter_automation_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reactor',
            fields=[
                ('automation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='automation.automation')),
                ('height', models.FloatField(default=10.0)),
                ('volume', models.FloatField(default=10.0)),
                ('fill', models.FloatField(default=0.0)),
                ('fill_m3', models.FloatField(default=0.0)),
                ('set_temperature', models.FloatField(default=21.0)),
                ('set_pressure', models.FloatField(default=1.0)),
                ('temperature_control', models.BooleanField(default=False)),
                ('pressure_control', models.BooleanField(default=False)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactors', to='automation.plant')),
            ],
            bases=('automation.automation',),
        ),
    ]
