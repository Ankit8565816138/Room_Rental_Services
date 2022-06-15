# Generated by Django 4.0 on 2022-01-15 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0005_rename_contact_contact_us'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=20, null=True, unique=True)),
                ('price', models.CharField(max_length=30, null=True)),
                ('r_type', models.CharField(max_length=40, null=True)),
                ('r_image', models.FileField(null=True, upload_to='')),
                ('status', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]