# Generated by Django 4.2.7 on 2023-11-19 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('pin', models.CharField(max_length=90)),
            ],
        ),
    ]
