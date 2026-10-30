import json
from pathlib import Path
from dealership.models import CarMake, CarModel, Dealer

CAR_MAKES = [
    {"name": "NISSAN", "description": "Great cars. Japanese technology",
     "country": "Japan", "founded_year": 1933},
    {"name": "Mercedes", "description": "Great cars. German technology",
     "country": "Germany", "founded_year": 1926},
    {"name": "Audi", "description": "Great cars. German technology",
     "country": "Germany", "founded_year": 1909},
    {"name": "Kia", "description": "Great cars. Korean technology",
     "country": "South Korea", "founded_year": 1944},
    {"name": "Toyota", "description": "Great cars. Japanese technology",
     "country": "Japan", "founded_year": 1937},
]

# (make name, model name, type, year, dealer id)
CAR_MODELS = [
    ("NISSAN", "Pathfinder", "SUV", 2023, 1),
    ("NISSAN", "Qashqai", "SUV", 2023, 2),
    ("NISSAN", "XTRAIL", "SUV", 2023, 3),
    ("Mercedes", "A-Class", "SUV", 2023, 4),
    ("Mercedes", "C-Class", "SUV", 2023, 5),
    ("Mercedes", "E-Class", "SUV", 2023, 6),
    ("Audi", "A4", "Sedan", 2023, 7),
    ("Audi", "A5", "Sedan", 2023, 8),
    ("Audi", "A6", "Sedan", 2023, 9),
    ("Kia", "Sorrento", "SUV", 2023, 10),
    ("Kia", "Carnival", "SUV", 2023, 11),
    ("Kia", "Cerato", "Sedan", 2023, 12),
    ("Toyota", "Corolla", "Sedan", 2023, 13),
    ("Toyota", "Camry", "Sedan", 2023, 14),
    ("Toyota", "Kluger", "SUV", 2023, 15),
]


def populate_cars():
    if CarModel.objects.count() >= 15:
        return

    makes = {}
    for make_data in CAR_MAKES:
        make_obj, _ = CarMake.objects.get_or_create(
            name=make_data["name"],
            defaults=make_data
        )
        makes[make_data["name"]] = make_obj

    for make_name, name, car_type, year, dealer_id in CAR_MODELS:
        CarModel.objects.get_or_create(
            name=name,
            car_make=makes[make_name],
            defaults={
                "type": car_type,
                "year": year,
                "dealer_id": dealer_id,
            }
        )


def populate_dealers():
    if Dealer.objects.count() >= 50:
        return

    data_file = Path(__file__).resolve().parent.parent / "database" / "data" / "dealerships.json"
    if not data_file.exists():
        return

    with open(data_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    dealers_list = data.get("dealerships", data if isinstance(data, list) else [])
    for d in dealers_list:
        Dealer.objects.update_or_create(
            id=d["id"],
            defaults={
                "city": d.get("city", ""),
                "state": d.get("state", ""),
                "st": d.get("st", ""),
                "address": d.get("address", ""),
                "zip": str(d.get("zip", "")),
                "latitude": float(d.get("lat", d.get("latitude", 0.0))),
                "longitude": float(d.get("long", d.get("longitude", 0.0))),
                "short_name": d.get("short_name", ""),
                "full_name": d.get("full_name", ""),
            }
        )


def initiate():
    populate_cars()
    populate_dealers()
