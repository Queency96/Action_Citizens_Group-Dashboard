# Generated by Django 5.2 on 2025-04-09 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0002_user_state_user_ward'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fullname',
            field=models.CharField(default=False, max_length=200),
        ),
    ]
