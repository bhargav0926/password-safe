# Generated by Django 5.0.7 on 2024-07-16 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NoteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainuser', models.CharField(default=True, max_length=20, unique=True)),
                ('mainpass', models.CharField(blank=True, max_length=20, null=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user',
                'ordering': ['mainuser'],
            },
        ),
    ]
