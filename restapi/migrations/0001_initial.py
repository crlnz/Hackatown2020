# Generated by Django 3.0 on 2020-01-18 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LUT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('before_image', models.ImageField(upload_to='')),
                ('after_image', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=200)),
                ('lut_file', models.FileField(upload_to='')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Searcher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('profile_image', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ('last_name',),
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('profile_image', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ('last_name',),
            },
        ),
    ]
