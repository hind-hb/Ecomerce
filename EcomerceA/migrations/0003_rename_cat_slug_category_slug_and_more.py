# Generated by Django 4.0.6 on 2022-07-20 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EcomerceA', '0002_rename_slug_category_cat_slug_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='cat_slug',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='pro_slug',
            new_name='slug',
        ),
    ]
