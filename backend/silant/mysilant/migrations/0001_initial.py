# Generated by Django 5.1.4 on 2025-01-02 11:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0004_alter_manager_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='guide_engine_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Справочник Модель двигателя',
                'verbose_name_plural': 'Справочник Модель двигателя',
            },
        ),
        migrations.CreateModel(
            name='guide_failure_node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Справочник Узел отказа',
                'verbose_name_plural': 'Справочник Узел отказа',
            },
        ),
        migrations.CreateModel(
            name='guide_model_controlled_bridge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Справочник Модель управляемого моста',
                'verbose_name_plural': 'Справочник Модель управляемого моста',
            },
        ),
        migrations.CreateModel(
            name='guide_model_drive_bridge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Справочник Модель ведущего моста',
            },
        ),
        migrations.CreateModel(
            name='guide_recovery_method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Справочник Способ восстановления',
                'verbose_name_plural': 'Справочник Способ восстановления',
            },
        ),
        migrations.CreateModel(
            name='guide_technique_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Справочник Модель техники',
                'verbose_name_plural': 'Справочник Модель техники',
            },
        ),
        migrations.CreateModel(
            name='guide_transmission_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Справочник Модель трансмиссии',
                'verbose_name_plural': 'Справочник Модель трансмиссии',
            },
        ),
        migrations.CreateModel(
            name='guide_types_of_maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Справочник Виды ТО',
                'verbose_name_plural': 'Справочник Виды ТО',
            },
        ),
        migrations.CreateModel(
            name='machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factory_number', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='Заводской номер')),
                ('engine_number', models.CharField(max_length=20, verbose_name='Номер двигателя')),
                ('transmission_number', models.CharField(max_length=50, verbose_name='Номер трансмиссии')),
                ('number_drive_bridge', models.CharField(max_length=50, verbose_name='Номер ведущего моста')),
                ('number_controlled_bridge', models.CharField(max_length=50, verbose_name='Номер управляемого моста')),
                ('delivery_date_number', models.TextField(max_length=50, verbose_name='Договор поставки №, дата')),
                ('date_shipment_factory', models.DateField(verbose_name='Дата отгрузки с завода')),
                ('endpoint_client', models.TextField(max_length=50, verbose_name='Грузополучатель (конечный потребитель)')),
                ('delivery_address', models.TextField(max_length=250, verbose_name='Адрес поставки (эксплуатации)')),
                ('Equipment', models.TextField(max_length=300, verbose_name='Комплектация (доп. опции)')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.client', verbose_name='Клиент')),
                ('engine_model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mysilant.guide_engine_model', verbose_name='Модель двигателя')),
                ('model_controlled_bridge', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mysilant.guide_model_controlled_bridge', verbose_name='Модель управляемого моста')),
                ('model_drive_bridge', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mysilant.guide_model_drive_bridge', verbose_name='Модель ведущего моста')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.service_company', verbose_name='Сервисная компания')),
                ('technique_model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mysilant.guide_technique_model', verbose_name='Модель техники')),
                ('transmission_model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mysilant.guide_transmission_model', verbose_name='Модель трансмиссии')),
            ],
            options={
                'verbose_name': 'Машина',
                'verbose_name_plural': 'Машины',
                'ordering': ['date_shipment_factory'],
            },
        ),
        migrations.CreateModel(
            name='maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_maintenance', models.DateField(verbose_name='Дата проведения ТО')),
                ('Operating_time', models.IntegerField(verbose_name='Наработка, м/час')),
                ('Order_number', models.TextField(max_length=50, verbose_name='№ заказ-наряда')),
                ('Order_date', models.DateField(verbose_name='Дата заказ-наряда')),
                ('maintenance_company', models.TextField(max_length=50, verbose_name='Организация, проводившая ТО')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mysilant.machine', verbose_name='Машина')),
                ('service_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.service_company', verbose_name='Сервисная компания')),
                ('types_of_maintenance', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mysilant.guide_types_of_maintenance', verbose_name='Вид ТО')),
            ],
            options={
                'verbose_name': 'ТО',
                'verbose_name_plural': 'ТО',
                'ordering': ['date_of_maintenance'],
            },
        ),
        migrations.CreateModel(
            name='reclamation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_of_refusal', models.DateField(verbose_name='Дата отказа')),
                ('Operating_time', models.IntegerField(verbose_name='Наработка, м/час')),
                ('failure_description', models.TextField(max_length=200, verbose_name='Описание отказа')),
                ('Spare_parts_used', models.TextField(max_length=200, verbose_name='Используемые запасные части')),
                ('date_of_recovery', models.DateField(verbose_name='Дата восстановления')),
                ('Equipment_downtime', models.IntegerField(verbose_name='Время простоя техники')),
                ('failure_node', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mysilant.guide_failure_node', verbose_name='Узел отказа')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mysilant.machine', verbose_name='Машина')),
                ('recovery_method', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mysilant.guide_recovery_method', verbose_name='Способ восстановления')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.service_company', verbose_name='Сервисная компания')),
            ],
            options={
                'verbose_name': 'Рекламации',
                'verbose_name_plural': 'Рекламации',
                'ordering': ['Date_of_refusal'],
            },
        ),
    ]
