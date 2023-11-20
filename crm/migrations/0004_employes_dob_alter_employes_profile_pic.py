# Generated by Django 4.2 on 2023-11-19 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_rename_images_employes_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='employes',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employes',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]