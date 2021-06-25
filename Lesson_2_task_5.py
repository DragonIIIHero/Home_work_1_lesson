numbers = [47.2, 38.1, 20, 12, 32.11, 90, 60, 15.01, 20.93, 1.01]
price_r = []
price_kk = []
price_text = []
price = []
number = []

for i in numbers:
    r = int(i)
    price_r.append(r)
    kk = i - r
    kk = int(kk*100)
    price_kk.append(kk)
    price_text = f"{r} руб {kk:02d} коп"
    price.append(price_text)
print(id(price), price)

price.sort()
print(id(price), price)

price_desc = []
price_desc.extend(price)
price_desc.sort(reverse=True)
print(id(price_desc), price_desc)


