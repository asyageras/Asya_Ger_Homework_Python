from smartphone import Smartphone

catalog = [
    Smartphone("Apple iPhone", "17", "+79123578622"),
    Smartphone("Samsung Galaxy", "S26", "+79657865143"),
    Smartphone("Honor", "8 Pro", "+79225458951"),
    Smartphone("Huawei", "Pura 80 Ultra", "+79191213146"),
    Smartphone("Xiaomi", "17T", "+79649432768")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
