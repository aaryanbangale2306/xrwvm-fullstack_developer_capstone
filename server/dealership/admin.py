from django.contrib import admin
from .models import DealerReview, Dealer, CarMake, CarModel

admin.site.register(DealerReview)
admin.site.register(Dealer)
admin.site.register(CarMake)
admin.site.register(CarModel)