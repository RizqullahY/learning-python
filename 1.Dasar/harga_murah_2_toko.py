input={

    'indoramet':{
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

for entry in item_to_buy:
    harga_indo = input['indoramet'][entry]
    harga_alfa = input['alfaramet'][entry]

    if harga_indo < harga_alfa:
        item_dibeli = harga_indo * item_to_buy[entry]

    else:
       
        item_dibeli = harga_alfa * item_to_buy[entry]
    total_belanja_murah += item_dibeli 
    
print(total_belanja_murah)
