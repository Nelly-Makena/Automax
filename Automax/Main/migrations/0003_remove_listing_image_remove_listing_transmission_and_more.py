# Generated by Django 5.1.1 on 2024-10-26 06:49

import Main.utils
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_listing_image_listing_transmission_listing_brand_and_more'),
        ('Users', '0004_alter_profile_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='Image',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='Transmission',
        ),
        migrations.AlterField(
            model_name='listing',
            name='location',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Users.location'),
        ),
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(blank=True, default='images/default-photo.png', null=True, upload_to=Main.utils.user_listing_path),
        ),
        migrations.AddField(
            model_name='listing',
            name='transmission',
            field=models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], default='Manual', max_length=24),
        ),
    ]
