# Generated by Django 4.1.3 on 2024-06-28 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group6', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='group6.faq'),
        ),
    ]
