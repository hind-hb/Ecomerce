# Generated by Django 4.0.6 on 2022-07-30 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcomerceA', '0008_product_trending'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='trending',
            field=models.BooleanField(default=False, help_text='0 = default, 1 = Hidden'),
        ),
    ]
