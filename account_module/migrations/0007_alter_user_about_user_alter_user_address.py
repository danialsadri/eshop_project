# Generated by Django 5.0 on 2024-01-10 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0006_alter_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='about_user',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='درباره شخص'),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='آدرس'),
        ),
    ]