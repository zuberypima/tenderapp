# Generated by Django 4.2 on 2023-05-21 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0005_reqirelist'),
    ]

    operations = [
        migrations.AddField(
            model_name='reqirelist',
            name='rqired',
            field=models.ForeignKey(default=2152023, on_delete=django.db.models.deletion.CASCADE, related_name='correct_choices', to='tender.tenderrequireiment'),
            preserve_default=False,
        ),
    ]
