# Generated by Django 4.0.6 on 2022-07-11 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetailedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('studentId', models.IntegerField()),
                ('gender', models.CharField(max_length=6)),
                ('roomtype', models.CharField(max_length=100)),
                ('room_choosing_status', models.CharField(max_length=3)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MRoom4mw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ManyToManyField(to='berlApp.detaileduser')),
            ],
        ),
        migrations.CreateModel(
            name='MRoom3mw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ManyToManyField(to='berlApp.detaileduser')),
            ],
        ),
        migrations.CreateModel(
            name='MRoom2mw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ManyToManyField(to='berlApp.detaileduser')),
            ],
        ),
        migrations.CreateModel(
            name='MRoom1mw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ManyToManyField(to='berlApp.detaileduser')),
            ],
        ),
    ]
