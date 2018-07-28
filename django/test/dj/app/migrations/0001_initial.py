# Generated by Django 2.0.7 on 2018-07-27 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='taskmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('completion_date', models.DateTimeField()),
                ('priority', models.CharField(choices=[('high', 'highpriority'), ('noraml', 'normalpriority'), ('low', 'lowpriority')], max_length=200)),
                ('is_complete', models.BooleanField(default=False)),
            ],
        ),
    ]