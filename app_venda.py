#!/usr/bin/env python3
import requests
from pprint import pprint

url = "http://127.0.0.1:8080"

vendas = [
    {"cliente_id": 1},
    {"cliente_id": 2},
    {"cliente_id": 2},
    {"cliente_id": 4}
]



for venda in vendas:  
    requests.post(f"{url}/venda", json=venda)

r = requests.get(f"{url}/venda")
pprint(r.json())