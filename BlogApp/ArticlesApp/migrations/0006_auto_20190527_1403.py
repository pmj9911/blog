# Generated by Django 2.1.4 on 2019-05-27 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArticlesApp', '0005_auto_20190527_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='images/default.png', upload_to='images/'),
        ),
    ]