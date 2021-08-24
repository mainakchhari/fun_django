# Generated by Django 3.2.6 on 2021-08-22 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ngo',
            fields=[
                ('name', models.CharField(max_length=25)),
                ('registration_no', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]