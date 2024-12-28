input={

    'indomaramet':{
        'ayam':30000,
        'sayur':15000,
        'buah':20000,
        'ikan':22000
    },
    'alfaramet':{
        'ayam':25000,
        'sayur':12000,
        'buah':30000,
        'ikan':25000
    }
}

item_to_buy = {
        'ayam': 2,
        'sayur': 1,
        'ikan': 1
    }

total_belanja_murah = 0

for item_yang_akan_dibeli in item_to_buy:
    harga_termurah = 0
    harga_indo = input['indomaramet'][item_yang_akan_dibeli]
    harga_alfa = input['alfaramet'][item_yang_akan_dibeli]

    if harga_indo < harga_alfa:
        harga_termurah = harga_indo 
    else:
       
        harga_termurah = harga_alfa 
    total_belanja_murah += harga_termurah * item_to_buy[item_yang_akan_dibeli]
print(total_belanja_murah)
    