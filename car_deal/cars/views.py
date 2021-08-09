from cars.models import Car
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Car


class CarsView(ListView):
    """Renders Cars page"""

    template_name = "cars/cars.html"
    model = Car
    paginate_by = 2
    context_object_name = 'cars'
    ordering = ['-created_date']


class CarDetailView(DetailView):
    """Renders Single Car's Detail view Page"""

    template_name = "cars/car.html"
    model = Car
    context_object_name = 'car'


class CarSearchResult(ListView):
    """Renders Search result of cars"""

    template_name = "cars/search.html"
    # model = Car
    # paginate_by = 3
    context_object_name = 'cars'

    def get_queryset(self):
        """Overriding get queryset method"""

        cars = Car.objects.all().order_by('-created_date')

        keyword = self.request.GET.get('keyword')
        if keyword:
            cars = cars.filter(description__icontains=keyword)

        if 'model' in self.request.GET:
            model = self.request.GET.get('model')
            if model:
                cars = cars.filter(model__iexact=model)

        if 'state' in self.request.GET:
            state = self.request.GET.get('state')
            if state:
                cars = cars.filter(state__iexact=state)

        if 'year' in self.request.GET:
            year = self.request.GET.get('year')
            if year:
                cars = cars.filter(year__iexact=year)

        if 'body_style' in self.request.GET:
            body_style = self.request.GET.get('body_style')
            if body_style:
                cars = cars.filter(body_style__iexact=body_style)

        if 'min_price' in self.request.GET:
            min_price = self.request.GET.get('min_price')
            max_price = self.request.GET.get('max_price')

            if max_price:
                # here get = greater_that_or_equal lte = less_that_or_equal
                cars = cars.filter(price__gte=min_price)

        return cars
