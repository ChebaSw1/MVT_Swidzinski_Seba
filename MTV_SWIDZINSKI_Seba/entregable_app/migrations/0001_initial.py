# Generated by Django 4.0.5 on 2022-06-15 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('anios', models.CharField(max_length=30)),
                ('parentesco', models.CharField(max_length=30)),
                ('cumpleanios', models.CharField(max_length=30)),
            ],
        ),
    ]