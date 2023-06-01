from django.http import JsonResponse

from django.views import View
from django.views.generic import DetailView

from network_links.models import Product, Factory, Retail, Individual


class ProductView(View):
    '''Представление для Продукции'''
    def get(self, request):
        products = Product.objects.all()

        response = []
        for product in products:
            response.append({
                "id": product.id,
                "title": product.title,
                "model": product.model
            })

        return JsonResponse(response, safe=False)


class ProductDetailView(DetailView):
    '''Представление для Продукции по id'''
    model = Product

    def get(self, request, *args, **kwargs):
        product = self.get_object()

        return JsonResponse({
            "title": product.title,
            "model": product.model
        })


class FactoryView(View):
    '''Представление для Завода'''
    def get(self, request):
        products = Factory.objects.all()

        response = []
        for product in products:
            response.append({
                "id": product.id,
                "name": product.name
            })

        return JsonResponse(response, safe=False)


class FactoryDetailView(DetailView):
    '''Представление для Завода по id'''
    model = Factory

    def get(self, request, *args, **kwargs):
        product = self.get_object()

        return JsonResponse({
            "name": product.name,
            "country": product.country,
            "city": product.city
        })


class RetailView(View):
    '''Представление для Розничной сети'''
    def get(self, request):
        products = Retail.objects.all()

        response = []
        for product in products:
            response.append({
                "id": product.id,
                "name": product.name
            })

        return JsonResponse(response, safe=False)


class RetailDetailView(DetailView):
    '''Представление для Розничной сети по id'''
    model = Retail

    def get(self, request, *args, **kwargs):
        product = self.get_object()

        return JsonResponse({
            "name": product.name,
            "country": product.country,
            "city": product.city
        })


class IndividualView(View):
    '''Представление для ИП'''
    def get(self, request):
        products = Individual.objects.all()

        response = []
        for product in products:
            response.append({
                "id": product.id,
                "name": product.name
            })

        return JsonResponse(response, safe=False)


class IndividualDetailView(DetailView):
    '''Представление для ИП по id'''
    model = Individual

    def get(self, request, *args, **kwargs):
        product = self.get_object()

        return JsonResponse({
            "name": product.name,
            "country": product.country,
            "city": product.city
        })
