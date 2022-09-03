# Generated by Django 3.1.4 on 2022-08-29 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_auto_20220829_2319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=20)),
                ('about', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=100)),
            ],
        ),
    ]