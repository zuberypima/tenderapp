# Generated by Django 4.2 on 2023-05-21 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0010_reqiredcontent_reqiredinput_vendorinput_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reqiredinput',
            name='clentinputs',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='vendorinput',
            name='vendorinputs',
            field=models.CharField(max_length=250),
        ),
    ]
