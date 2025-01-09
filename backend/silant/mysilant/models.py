from django.db import models
from accounts.models import client, service_company

class guide_types_of_maintenance(models.Model):
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Справочник Виды ТО'
        verbose_name_plural = 'Справочник Виды ТО'

class guide_recovery_method(models.Model):
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Справочник Способ восстановления'
        verbose_name_plural = 'Справочник Способ восстановления'

class guide_failure_node(models.Model):
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Справочник Узел отказа'
        verbose_name_plural = 'Справочник Узел отказа'

class guide_technique_model(models.Model):
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Справочник Модель техники'
        verbose_name_plural = 'Справочник Модель техники'

class guide_engine_model(models.Model):
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Справочник Модель двигателя'
        verbose_name_plural = 'Справочник Модель двигателя'

class guide_transmission_model(models.Model):
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Справочник Модель трансмиссии'
        verbose_name_plural = 'Справочник Модель трансмиссии'

class guide_model_drive_bridge(models.Model):
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Справочник Модель ведущего моста'
    verbose_name_plural = 'Справочник Модель ведущего моста'

class guide_model_controlled_bridge(models.Model):
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Справочник Модель управляемого моста'
        verbose_name_plural = 'Справочник Модель управляемого моста'

class machine(models.Model):
    factory_number = models.CharField(max_length=20, unique=True, db_index=True, verbose_name='Заводской номер')
    technique_model = models.ForeignKey(guide_technique_model, on_delete=models.PROTECT, verbose_name='Модель техники')
    engine_model = models.ForeignKey(guide_engine_model, on_delete=models.PROTECT, verbose_name='Модель двигателя')
    engine_number = models.CharField(max_length=20, verbose_name='Номер двигателя')
    transmission_model = models.ForeignKey(guide_transmission_model, on_delete=models.PROTECT, verbose_name='Модель трансмиссии')
    transmission_number = models.CharField(max_length=50, verbose_name='Номер трансмиссии')
    model_drive_bridge = models.ForeignKey(guide_model_drive_bridge, on_delete=models.PROTECT, verbose_name='Модель ведущего моста')
    number_drive_bridge = models.CharField(max_length=50, verbose_name='Номер ведущего моста')
    model_controlled_bridge = models.ForeignKey(guide_model_controlled_bridge, on_delete=models.PROTECT, verbose_name='Модель управляемого моста')
    number_controlled_bridge = models.CharField(max_length=50, verbose_name='Номер управляемого моста')
    delivery_date_number = models.TextField(max_length=50, verbose_name='Договор поставки №, дата')
    date_shipment_factory = models.DateField(verbose_name='Дата отгрузки с завода')
    endpoint_client = models.TextField(max_length=50, verbose_name='Грузополучатель (конечный потребитель)')
    delivery_address = models.TextField(max_length=250, verbose_name='Адрес поставки (эксплуатации)')
    Equipment = models.TextField(max_length=300, verbose_name='Комплектация (доп. опции)')
    client = models.ForeignKey(client, on_delete=models.PROTECT, verbose_name='Клиент')
    service_company = models.ForeignKey(service_company, on_delete=models.PROTECT, verbose_name='Сервисная компания')

    def __str__(self):
        return f'{self.factory_number}'

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
        ordering = ['date_shipment_factory']

class maintenance(models.Model):
    types_of_maintenance = models.ForeignKey(guide_types_of_maintenance, on_delete=models.PROTECT, verbose_name='Вид ТО')
    date_of_maintenance = models.DateField(verbose_name='Дата проведения ТО')
    Operating_time = models.IntegerField(verbose_name='Наработка, м/час')
    Order_number = models.TextField(max_length=50, verbose_name='№ заказ-наряда')
    Order_date = models.DateField(verbose_name='Дата заказ-наряда')
    maintenance_company = models.TextField(max_length=50, verbose_name='Организация, проводившая ТО')
    machine = models.ForeignKey(machine, on_delete=models.PROTECT, verbose_name='Машина')
    service_company = models.ForeignKey(service_company, null=True, blank = True, on_delete=models.PROTECT, verbose_name='Сервисная компания')

    def __str__(self):
        return f'{self.machine, self.types_of_maintenance}'

    class Meta:
        verbose_name = 'ТО'
        verbose_name_plural = 'ТО'
        ordering = ['date_of_maintenance']


class reclamation(models.Model):
    Date_of_refusal = models.DateField(verbose_name='Дата отказа')
    Operating_time = models.IntegerField(verbose_name='Наработка, м/час')
    failure_node = models.ForeignKey(guide_failure_node, on_delete=models.PROTECT, verbose_name='Узел отказа')
    failure_description = models.TextField(max_length=200, verbose_name='Описание отказа')
    recovery_method = models.ForeignKey(guide_recovery_method, on_delete=models.PROTECT, verbose_name='Способ восстановления')
    Spare_parts_used = models.TextField(max_length=200, verbose_name='Используемые запасные части')
    date_of_recovery = models.DateField(verbose_name='Дата восстановления')
    Equipment_downtime = models.IntegerField(verbose_name='Время простоя техники')
    machine = models.ForeignKey(machine, on_delete=models.PROTECT, verbose_name='Машина')
    service_company = models.ForeignKey(service_company, on_delete=models.PROTECT, verbose_name='Сервисная компания')

    def __str__(self):
        return f'{self.machine, self.failure_node}'

    class Meta:
        verbose_name = 'Рекламации'
        verbose_name_plural = 'Рекламации'
        ordering = ['Date_of_refusal']
