# Generated by Django 5.0.6 on 2024-06-11 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mahshulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='mahshulot_id',
            field=models.ManyToManyField(related_name='mahshulot', to='my_app.mahshulot'),
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
