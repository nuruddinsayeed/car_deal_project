from cars.models import Car
from django.shortcuts import render
from .models import Team


def get_teams_info():
    return Team.objects.all()


def index(request):
    """Renders Home page"""

    teams = get_teams_info()

    # get all available fiels from our ddatabase to suggest search
    available_models = Car.objects.values_list(
        'model', flat=True).distinct('model')
    available_states = Car.objects.values_list(
        'state', flat=True).distinct('state')
    available_years = Car.objects.values_list(
        'year', flat=True).order_by('year').distinct('year')
    available_body_styles = Car.objects.values_list(
        'body_style', flat=True).distinct('body_style')

    data = {
        "teams": get_teams_info(),
        "featured_cars": Car.objects.order_by(
            '-created_date').filter(is_featured=True),
        "latest_cars": Car.objects.order_by('-created_date')[:6],
        "available_models": available_models,
        "available_states": available_states,
        "available_years": available_years,
        "available_body_styles": available_body_styles,
    }

    return render(request, "pages/index.html", data)


def about(request):
    "Renders About page"
    data = {"teams": get_teams_info()}

    return render(request, "pages/about.html", data)


def services(request):
    "Renders services page"

    return render(request, "pages/services.html")


def contact(request):
    "Renders contact page"

    return render(request, "pages/contact.html")
