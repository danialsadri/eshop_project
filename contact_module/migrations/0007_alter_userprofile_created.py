# Generated by Django 5.0 on 2024-01-07 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0006_alter_userprofile_created_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد'),
        ),
    ]
