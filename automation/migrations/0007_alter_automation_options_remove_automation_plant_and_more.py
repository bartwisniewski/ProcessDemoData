# Generated by Django 4.0.5 on 2022-06-09 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0006_alter_automation_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='automation',
            options={'ordering': ['row', 'col']},
        ),
        migrations.RemoveField(
            model_name='automation',
            name='plant',
        ),
        migrations.AddField(
            model_name='pipe',
            name='plant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pipes', to='automation.plant'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pump',
            name='plant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pumps', to='automation.plant'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tank',
            name='plant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tanks', to='automation.plant'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valve',
            name='plant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='valves', to='automation.plant'),
            preserve_default=False,
        ),
    ]
