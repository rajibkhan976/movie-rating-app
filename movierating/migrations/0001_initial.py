# Generated by Django 5.0.3 on 2024-04-04 06:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('genre', models.CharField(max_length=150, null=True)),
                ('rating', models.CharField(max_length=150, null=True)),
                ('release_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=24)),
                ('password', models.CharField(max_length=8)),
                ('email', models.EmailField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.FloatField()),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ids', to='movierating.movie')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movierating.user')),
            ],
        ),
    ]
