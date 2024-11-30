# Generated by Django 5.1.1 on 2024-11-30 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Label name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
