# Generated by Django 3.1 on 2020-10-18 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AqiData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('pm_25', models.PositiveIntegerField()),
                ('pm_10', models.PositiveIntegerField()),
            ],
        ),
    ]
