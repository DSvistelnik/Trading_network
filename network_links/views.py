from django.http import JsonResponse

from django.views import View
from django.views.generic import DetailView

from network_links.models import Product, Network


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


class NetworkView(View):
    '''Представление для Сети'''
    def get(self, request):
        products = Network.objects.all()

        response = []
        for product in products:
            response.append({
                "id": product.id,
                "name": product.name,
                "link": product.link
            })

        return JsonResponse(response, safe=False)


class NetworkDetailView(DetailView):
    '''Представление для Завода по id'''
    model = Network

    def get(self, request, *args, **kwargs):
        product = self.get_object()

        return JsonResponse({
            "name": product.name,
            "country": product.country,
            "city": product.city
        })


