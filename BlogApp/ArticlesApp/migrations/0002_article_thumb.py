# Generated by Django 2.1.4 on 2019-05-25 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArticlesApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
