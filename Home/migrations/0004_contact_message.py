# Generated by Django 4.1 on 2022-08-29 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_rename_adress_contact_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]