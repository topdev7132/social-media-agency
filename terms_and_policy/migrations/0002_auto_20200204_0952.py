# Generated by Django 2.2.9 on 2020-02-04 09:52

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('terms_and_policy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='termsandpolicypage',
            name='custom_title',
            field=wagtail.core.fields.RichTextField(default='Input here...'),
        ),
    ]
