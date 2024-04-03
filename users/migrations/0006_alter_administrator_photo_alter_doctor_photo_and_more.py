# Generated by Django 5.0.3 on 2024-04-02 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_administrator_photo_alter_doctor_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='admin', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='doctor', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='user', verbose_name='Photo'),
        ),
    ]
