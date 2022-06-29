# Generated by Django 4.0.5 on 2022-06-09 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Automation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('row', models.IntegerField()),
                ('col', models.IntegerField()),
                ('connections', models.JSONField(default=[0, 0, 0, 0])),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auto_objects', to='automation.plant')),
            ],
            options={
                'ordering': ['plant'],
            },
        ),
        migrations.CreateModel(
            name='Pipe',
            fields=[
                ('automation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='automation.automation')),
                ('dim', models.IntegerField(default=60)),
            ],
            bases=('automation.automation',),
        ),
        migrations.CreateModel(
            name='Pump',
            fields=[
                ('automation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='automation.automation')),
                ('on', models.BooleanField(default=False)),
                ('end', models.IntegerField(default=1)),
                ('speed', models.FloatField(default=0.0)),
            ],
            bases=('automation.automation',),
        ),
        migrations.CreateModel(
            name='Tank',
            fields=[
                ('automation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='automation.automation')),
                ('height', models.FloatField(default=10.0)),
                ('volume', models.FloatField(default=10.0)),
                ('fill', models.FloatField(default=0.0)),
            ],
            bases=('automation.automation',),
        ),
        migrations.CreateModel(
            name='Valve',
            fields=[
                ('automation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='automation.automation')),
                ('open', models.BooleanField(default=False)),
            ],
            bases=('automation.automation',),
        ),
    ]