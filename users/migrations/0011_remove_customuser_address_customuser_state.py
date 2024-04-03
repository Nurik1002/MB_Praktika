# Generated by Django 5.0.3 on 2024-04-03 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='address',
        ),
        migrations.AddField(
            model_name='customuser',
            name='state',
            field=models.TextField(blank=True, max_length=100, verbose_name='State'),
        ),
    ]
