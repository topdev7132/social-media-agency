# Generated by Django 2.2.9 on 2020-02-15 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200215_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetailpage',
            name='summary',
            field=models.CharField(default='Input the summary...', help_text='Overwrites the default title', max_length=300),
        ),
    ]
