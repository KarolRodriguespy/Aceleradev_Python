# Generated by Django 3.0.8 on 2020-07-17 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_remove_event_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='environment',
            field=models.CharField(choices=[('produção', 'produção'), ('homologação', 'homologação'), ('dev', 'dev')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
