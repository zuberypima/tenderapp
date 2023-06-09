# Generated by Django 4.2 on 2023-05-21 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idNo', models.CharField(max_length=255)),
                ('orgName', models.CharField(max_length=255)),
                ('orgCategory', models.CharField(choices=[('Private', 'Private'), ('Public', 'Public'), ('Government', 'Government')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CreateCond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condDetails', models.CharField(max_length=255)),
                ('condValue', models.CharField(max_length=255)),
                ('clientDetails', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='procoficer.clientdetail')),
            ],
        ),
    ]
