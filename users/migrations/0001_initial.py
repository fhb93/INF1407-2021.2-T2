# Generated by Django 3.2.6 on 2021-11-27 23:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(default=None, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=3000)),
                ('content', models.TextField(max_length=150)),
                ('author', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('bio_id', models.AutoField(default=None, editable=False, primary_key=True, serialize=False)),
                ('content', models.TextField(max_length=150)),
                ('author', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
