# Generated by Django 4.2.7 on 2023-11-15 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodata',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='biodata',
            name='nin',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='biodata',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
