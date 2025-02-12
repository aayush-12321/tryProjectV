# Generated by Django 5.0.2 on 2025-01-22 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0013_alter_rating_rate_type_alter_rating_rated_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='interests',
            field=models.TextField(blank=True, help_text="Skills or areas you'd like to learn (separated by commas)", max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=models.TextField(blank=True, help_text='List of skills you can share (separated by commas)', max_length=500, null=True),
        ),
    ]
