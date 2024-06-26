# Generated by Django 5.0 on 2024-01-17 02:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0009_alter_articlecomment_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-create_date'], 'verbose_name': 'مقاله', 'verbose_name_plural': 'مقالات'},
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده'),
        ),
        migrations.AlterField(
            model_name='article',
            name='short_description',
            field=models.TextField(max_length=500, verbose_name='توضیحات کوتاه'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=500, verbose_name='عنوان در url'),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(max_length=500000, verbose_name='متن مقاله'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=500, verbose_name='عنوان مقاله'),
        ),
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['slug'], name='article_mod_slug_3cbc1a_idx'),
        ),
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['-create_date'], name='article_mod_create__16fc37_idx'),
        ),
    ]
