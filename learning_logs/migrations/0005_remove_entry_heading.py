# Generated by Django 4.2.6 on 2023-11-25 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0004_entry_heading'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='heading',
        ),
    ]
