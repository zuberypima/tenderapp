# Generated by Django 4.2 on 2023-05-21 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0008_remove_reqirelist_inputs_alter_reqirelist_rqired_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reqired',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('clentinputs', models.CharField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name='vendorCapacity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendorinputs', models.CharField(max_length=2500)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tender.reqired')),
            ],
        ),
    ]