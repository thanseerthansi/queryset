# Generated by Django 4.0.4 on 2022-05-11 08:50

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('selectedrelated', '0003_banking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
            ],
            managers=[
                ('students', django.db.models.manager.Manager()),
            ],
        ),
    ]
