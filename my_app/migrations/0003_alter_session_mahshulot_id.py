# Generated by Django 5.0.6 on 2024-06-11 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_mahshulot_session_mahshulot_id_delete_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='mahshulot_id',
            field=models.ManyToManyField(blank=True, related_name='sessions', to='my_app.mahshulot'),
        ),
    ]