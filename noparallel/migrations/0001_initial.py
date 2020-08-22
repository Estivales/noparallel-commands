# Generated by Django 3.1 on 2020-08-22 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommandHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command', models.CharField(max_length=250)),
                ('started_at', models.DateTimeField(auto_now_add=True)),
                ('done_at', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
    ]
