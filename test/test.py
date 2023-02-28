import requests

url = 'http://localhost:5000/trips'

data = [
    {
        "region": "Hamburg",
        "origin_coord": "POINT (10.07299025213017 53.62044974829032)",
        "destination_coord": "POINT (9.789197601249002 53.46315765148751)",
        "datetime": "2018-05-15 09:13:36",
        "datasource": "bad_diesel_vehicles"
    },
    {
        "region": "Hamburg",
        "origin_coord": "POINT (9.910278201788232 53.58386264717827)",
        "destination_coord": "POINT (10.02557919725378 53.4120717767391)",
        "datetime": "2018-05-13 13:09:19",
        "datasource": "funny_car"
    },
    {
        "region": "Turin",
        "origin_coord": "POINT (7.560785081962462 45.01901608530191)",
        "destination_coord": "POINT (7.583568695710608 45.10526898076209)",
        "datetime": "2018-05-06 00:00:44",
        "datasource": "cheap_mobile"
    },
    {
        "region": "Turin",
        "origin_coord": "POINT (7.702418079996892 45.05754972796922)",
        "destination_coord": "POINT (7.623229346744799 44.99969774086024)",
        "datetime": "2018-05-14 02:07:30",
        "datasource": "cheap_mobile"
    }
]

for trip in data:
    response = requests.post(url, json=trip)
    print(response.status_code, response.json())
