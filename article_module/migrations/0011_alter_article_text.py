# Generated by Django 5.0 on 2024-01-17 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0010_alter_article_options_alter_article_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(max_length=5000, verbose_name='متن مقاله'),
        ),
    ]
