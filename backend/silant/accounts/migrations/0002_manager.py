# Generated by Django 5.1.4 on 2025-01-02 11:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='manager',
            fields=[
                ('basecompany_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.basecompany')),
            ],
            bases=('accounts.basecompany',),
        ),
    ]
