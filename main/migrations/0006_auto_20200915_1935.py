# Generated by Django 3.1.1 on 2020-09-15 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200915_1903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='date',
            new_name='bo_date',
        ),
        migrations.AddField(
            model_name='item',
            name='re_date',
            field=models.TextField(default='hoge$#@#$', null=True),
        ),
    ]