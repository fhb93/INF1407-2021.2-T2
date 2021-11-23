# Generated by Django 3.2.6 on 2021-11-23 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211123_0657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bio',
            name='id',
        ),
        migrations.RemoveField(
            model_name='review',
            name='id',
        ),
        migrations.AddField(
            model_name='bio',
            name='bio_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='review',
            name='review_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]