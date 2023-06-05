from django.db import models


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
    provider = models.ForeignKey('network_links.Network', on_delete=models.SET_NULL, null=True, blank=True)
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Звено торговой сети'
        verbose_name_plural = 'Звенья торговой сети'

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    '''Создание модели Продукция'''
    trading = models.ForeignKey(Network, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=200, null=True, blank=True)
    model = models.CharField(max_length=200, null=True, blank=True)
    release_date = models.DateField()

    class Meta:
        verbose_name = "Продукция"
        verbose_name_plural = "Продукция"

    def __str__(self):
        return self.title


class Contacts(models.Model):
    '''Создание модели Контакты'''
    trading = models.ForeignKey(Network, on_delete=models.CASCADE, related_name='contacts')
    email = models.EmailField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    street = models.CharField(max_length=200, null=True, blank=True)
    number_house = models.IntegerField()

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f'{self.country}, {self.city}'
