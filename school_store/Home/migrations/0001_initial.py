# Generated by Django 4.1.7 on 2023-02-19 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=250, unique=True)),
                ('links', models.CharField(max_length=500, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.departments')),
            ],
        ),
    ]
