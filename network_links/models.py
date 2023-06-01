from django.db import models


class Product(models.Model):
    '''Создание модели Продукция'''
    title = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    release_date = models.DateField()

    class Meta:
        verbose_name = "Продукция"
        verbose_name_plural = "Продукции"

    def __str__(self):
        return self.title


class Factory(models.Model):
    '''Создание модели Завод'''
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    number_house = models.IntegerField()
    product = models.ManyToManyField(Product)

    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"

    def __str__(self):
        return self.name


class Retail(models.Model):
    '''Создание модели Розничная сеть'''
    name = models.CharField(max_length=200)
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    number_house = models.IntegerField()
    product = models.ManyToManyField(Product)
    provider = models.ForeignKey(Factory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Розничная сеть"
        verbose_name_plural = "Розничные сети"

    def __str__(self):
        return self.name


class Individual(models.Model):
    '''Создание модели Индивидуальный предприниматель'''
    name = models.CharField(max_length=200)
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    number_house = models.IntegerField()
    product = models.ManyToManyField(Product)
    provider = models.ForeignKey(Factory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Индивидуальный предприниматель"
        verbose_name_plural = "Индивидуальные предприниматели"

    def __str__(self):
        return self.name

