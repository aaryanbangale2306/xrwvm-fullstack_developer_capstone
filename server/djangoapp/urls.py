from django.contrib import admin
from django.urls import path
from .views import (
    home, login_user, logout_user, register_user,
    get_dealer_reviews, get_all_dealers, get_dealer_by_id,
    get_dealers_by_state, get_cars, get_all_car_makes,
    analyze_review, review_dealer
)

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),

    # Authentication
    path("djangoapp/login", login_user),
    path("djangoapp/logout", logout_user),
    path("djangoapp/register", register_user),
    path("djangoapp/registration", register_user),
    path("register", register_user),

    # Dealership endpoints
    path("fetchDealers", get_all_dealers),
    path("fetchDealers/", get_all_dealers),
    path("djangoapp/fetchDealers", get_all_dealers),
    path("djangoapp/get_dealers", get_all_dealers),
    path("dealer/<int:dealer_id>", get_dealer_by_id),
    path("djangoapp/dealer/<int:dealer_id>", get_dealer_by_id),
    path("fetchDealers/<str:state>", get_dealers_by_state),
    path("djangoapp/get_dealers/<str:state>", get_dealers_by_state),

    # Reviews
    path("dealer/<int:dealer_id>/reviews", get_dealer_reviews),
    path("djangoapp/reviews/dealer/<int:dealer_id>", get_dealer_reviews),
    path("analyze/<str:review_text>", analyze_review),
    path("dealer/<int:dealer_id>/review", review_dealer),

    # Cars & Makes/Models
    path("djangoapp/get_cars", get_cars),
    path("get_cars", get_cars),
    path("carmakes", get_all_car_makes),
]