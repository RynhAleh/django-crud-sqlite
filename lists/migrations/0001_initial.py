# Generated by Django 5.1.2 on 2024-10-14 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('patronymic', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=50)),
                ('works', models.BooleanField(default=True)),
            ],
        ),
    ]
