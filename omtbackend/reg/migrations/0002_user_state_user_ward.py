# Generated by Django 5.2 on 2025-04-08 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(default=False, max_length=254),
        ),
        migrations.AddField(
            model_name='user',
            name='ward',
            field=models.EmailField(default=False, max_length=254),
        ),
    ]
