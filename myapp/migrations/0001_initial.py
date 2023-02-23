# Generated by Django 4.1.2 on 2022-12-04 04:52

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=191)),
                ('price', models.TextField(max_length=50)),
                ('description', models.TextField(max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=myapp.models.filepath)),
            ],
        ),
    ]
