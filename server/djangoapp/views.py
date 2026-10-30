import json
import logging
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from dealership.models import Dealer, DealerReview, CarMake, CarModel
from .populate import populate_cars, populate_dealers

logger = logging.getLogger(__name__)


def home(request):
    return render(request, "index.html")


@csrf_exempt
def login_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except Exception:
            data = request.POST

        username = data.get("userName") or data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"userName": user.username, "status": "Authenticated"})

        return JsonResponse({"userName": "", "error": "Authentication Failed"}, status=401)

    return JsonResponse({"error": "POST request required"}, status=405)


def logout_user(request):
    logout(request)
    return JsonResponse({"userName": ""})


@csrf_exempt
def register_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except Exception:
            data = request.POST

        username = data.get("userName") or data.get("username")
        password = data.get("password")
        first_name = data.get("firstName") or data.get("first_name", "")
        last_name = data.get("lastName") or data.get("last_name", "")
        email = data.get("email", "")

        if not username or not password:
            return JsonResponse({"error": "Username and password required"}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({
                "userName": username,
                "error": "Already Registered"
            })

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            email=email
        )
        login(request, user)
        return JsonResponse({
            "userName": user.username,
            "status": "Authenticated"
        })

    return JsonResponse({"error": "POST request required"}, status=405)


def get_all_dealers(request):
    if request.method == "GET":
        if Dealer.objects.count() < 50:
            populate_dealers()

        dealers = Dealer.objects.all().order_by("id")
        data = []
        for dealer in dealers:
            data.append({
                "id": dealer.id,
                "city": dealer.city,
                "state": dealer.state,
                "st": dealer.st,
                "address": dealer.address,
                "zip": dealer.zip,
                "lat": dealer.latitude,
                "latitude": dealer.latitude,
                "long": dealer.longitude,
                "longitude": dealer.longitude,
                "short_name": dealer.short_name,
                "full_name": dealer.full_name
            })

        return JsonResponse(data, safe=False)

    return JsonResponse({"error": "GET request required"}, status=405)


def get_dealer_by_id(request, dealer_id):
    if request.method == "GET":
        if Dealer.objects.count() < 50:
            populate_dealers()

        try:
            dealer = Dealer.objects.get(id=dealer_id)
            data = {
                "id": dealer.id,
                "city": dealer.city,
                "state": dealer.state,
                "st": dealer.st,
                "address": dealer.address,
                "zip": dealer.zip,
                "lat": dealer.latitude,
                "latitude": dealer.latitude,
                "long": dealer.longitude,
                "longitude": dealer.longitude,
                "short_name": dealer.short_name,
                "full_name": dealer.full_name
            }
            return JsonResponse(data)
        except Dealer.DoesNotExist:
            return JsonResponse({"error": "Dealer not found"}, status=404)

    return JsonResponse({"error": "GET request required"}, status=405)


def get_dealers_by_state(request, state):
    if Dealer.objects.count() < 50:
        populate_dealers()

    dealers = Dealer.objects.filter(state__iexact=state)
    if not dealers.exists():
        dealers = Dealer.objects.filter(st__iexact=state)

    if "text/html" in request.headers.get("Accept", ""):
        return render(
            request,
            "state_dealers.html",
            {
                "dealers": dealers,
                "state": state
            }
        )

    if request.method == "GET":
        data = []
        for dealer in dealers:
            data.append({
                "id": dealer.id,
                "city": dealer.city,
                "state": dealer.state,
                "st": dealer.st,
                "address": dealer.address,
                "zip": dealer.zip,
                "lat": dealer.latitude,
                "latitude": dealer.latitude,
                "long": dealer.longitude,
                "longitude": dealer.longitude,
                "short_name": dealer.short_name,
                "full_name": dealer.full_name
            })
        return JsonResponse(data, safe=False)

    return JsonResponse({"error": "GET request required"}, status=405)


def get_dealer_reviews(request, dealer_id):
    try:
        dealer = Dealer.objects.get(id=dealer_id)
    except Dealer.DoesNotExist:
        return JsonResponse({"error": "Dealer not found"}, status=404)

    reviews = DealerReview.objects.filter(dealer_id=dealer_id)

    if "text/html" in request.headers.get("Accept", ""):
        return render(
            request,
            "dealer_reviews.html",
            {
                "dealer": dealer,
                "reviews": reviews
            }
        )

    if request.method == "GET":
        data = []
        for review in reviews:
            data.append({
                "id": review.id,
                "dealer_id": review.dealer_id,
                "dealership": review.dealership,
                "name": review.name,
                "purchase": review.purchase,
                "review": review.review,
                "purchase_date": review.purchase_date,
                "car_make": review.car_make,
                "car_model": review.car_model,
                "car_year": review.car_year,
                "sentiment": review.sentiment
            })
        return JsonResponse(data, safe=False)

    return JsonResponse({"error": "GET request required"}, status=405)


def get_cars(request):
    if request.method == "GET":
        if CarModel.objects.count() < 15:
            populate_cars()

        car_models = CarModel.objects.select_related("car_make").all().order_by("id")
        cars = []
        for cm in car_models:
            cars.append({
                "make": cm.car_make.name,
                "model": cm.name,
                "CarMake": cm.car_make.name,
                "CarModel": cm.name,
                "type": cm.type,
                "year": cm.year,
                "dealer_id": cm.dealer_id,
            })
        return JsonResponse({"CarModels": cars})

    return JsonResponse({"error": "GET request required"}, status=405)


def get_all_car_makes(request):
    return get_cars(request)


def analyze_review(request, review_text):
    if request.method == "GET":
        sentiment = "Positive"
        return JsonResponse({
            "review": review_text,
            "sentiment": sentiment
        })
    return JsonResponse({"error": "GET request required"}, status=405)


def review_dealer(request, dealer_id):
    try:
        dealer = Dealer.objects.get(id=dealer_id)
    except Dealer.DoesNotExist:
        return JsonResponse({"error": "Dealer not found"}, status=404)

    if request.method == "POST":
        DealerReview.objects.create(
            dealer_id=dealer.id,
            dealership=dealer.full_name,
            name=request.POST.get("name"),
            purchase=True if request.POST.get("purchase") else False,
            review=request.POST.get("review"),
            purchase_date=request.POST.get("purchase_date"),
            car_make=request.POST.get("car_make"),
            car_model=request.POST.get("car_model"),
            car_year=int(request.POST.get("car_year", 2023)),
            sentiment="Positive"
        )
        return redirect(f"/dealer/{dealer.id}/reviews")

    return render(
        request,
        "review_dealer.html",
        {
            "dealer": dealer
        }
    )