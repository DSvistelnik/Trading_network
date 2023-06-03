from django.db import models


class Product(models.Model):
    '''Создание модели Продукция'''
    title = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    release_date = models.DateField()

    class Meta:
        verbose_name = "Продукция"
        verbose_name_plural = "Продукция"

    def __str__(self):
        return self.title


class Contacts(models.Model):
    '''Создание модели Контакты'''
    email = models.EmailField(max_length=100)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    number_house = models.IntegerField()

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f'{self.country}, {self.city}'


class Network(models.Model):
    """Создание модели Сети, в которую входят 3 звена:
    Завод, Розничная сеть, Индивидуальный предприниматель
    """
    class Link(models.IntegerChoices):
        Factory = 0
        Retail = 1
        Individual = 2

    name = models.CharField(max_length=200)
    link = models.PositiveIntegerField(choices=Link.choices)
    contacts = models.ForeignKey('network_links.Contacts', on_delete=models.SET_NULL, null=True, blank=True)
    provider = models.ForeignKey('network_links.Network', on_delete=models.SET_NULL, null=True, blank=True)
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ManyToManyField('network_links.Product')
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Звено сети'
        verbose_name_plural = 'Звенья сети'

    def __str__(self):
        return f'{self.name}'

