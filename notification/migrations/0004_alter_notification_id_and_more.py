# Generated by Django 5.0.2 on 2024-11-23 05:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_auto_20220214_1319'),
        ('post', '0009_remove_post_picture_postimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notification_types',
            field=models.IntegerField(choices=[(1, 'Like'), (2, 'Comment'), (3, 'Follow'), (4, 'New Post')], default=1),
        ),
        migrations.AlterField(
            model_name='notification',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_post', to='post.post'),
        ),
    ]