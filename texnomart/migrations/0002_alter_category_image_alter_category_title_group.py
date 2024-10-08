# Generated by Django 5.0.2 on 2024-08-25 23:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texnomart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/category/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=120, unique=True),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=120, unique=True)),
                ('slug', models.SlugField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/group/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='texnomart.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
