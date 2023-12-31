# Generated by Django 4.2.3 on 2023-07-12 13:51

from django.db import migrations, models
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('customerId', models.IntegerField(default=0)),
                ('type', models.CharField(default='AAA', max_length=255)),
                ('amount', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
