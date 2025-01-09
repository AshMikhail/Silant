from django.db import models
from django.contrib.auth.models import User


class baseCompany(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(unique=True, verbose_name='Название')
    Сlient = 'Клиент'
    Service_organization = 'Сервисная компания'
    Manager = 'Менеджер'
    CATEGORY_CHOICES = (
        (Сlient, 'Клиент'),
        (Service_organization, 'Сервисная компания'),
        (Manager, 'Менеджер'),
    )
    сategory = models.CharField(max_length=21, verbose_name='Категория', choices=CATEGORY_CHOICES, default=Сlient)


class client(baseCompany):
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class service_company(baseCompany):
    description = models.TextField(blank=True, verbose_name='Описание')
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Сервисная компания'
        verbose_name_plural = 'Сервисные компании'


class manager(baseCompany):
    pass
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'