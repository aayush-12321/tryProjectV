# Generated by Django 5.0.2 on 2025-01-12 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_alter_post_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='posted',
            field=models.DateField(auto_now_add=True),
        ),
    ]