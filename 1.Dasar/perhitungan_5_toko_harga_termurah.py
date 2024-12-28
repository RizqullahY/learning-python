input = {
    "Indoramet":{
        "Ayam": 30000,
        "Sayur": 15000,
        "Buah": 20000,
        "Ikan": 22000
    },
    "Alfaramet":{
        "Ayam": 25000,
        "Sayur": 12000,
        "Buah": 30000,
        "Ikan": 25000
    },
    "MarketKeluarga":{
        "Ayam": 22000,
        "Sayur": 8000,
        "Buah": 25000,
        "Ikan": 28000
    },
    "Pahlawan":{
        "Ayam": 24000,
        "Sayur": 18000,
        "Buah": 12500,
        "Ikan": 11000  
    },
    "Jayen":{
        "Ayam": 10000,
        "Sayur": 5000,
        "Buah": 15000,
        "Ikan": 2000  
    }
}

items_to_buy = {
    "Ayam":2,
    "Sayur":1,
    "Ikan":1,
    "Buah":3
}


sum = 0     # index dimulai dari 0

for entry in items_to_buy.keys():       # membuat loop bernama 'entry' didalam data items_to_buy keys berisi nama benda
    
    cheapest_price = 9999999            # membuat sebuah value yang besar guna menyeleksi yang kecil

    for toko in input.keys():           # membuat loop bernama 'toko' didalam data input keys yang berisi nama toko tersebut
        
        harga_toko = input[toko][entry]     
        
        print(input[toko][entry])       # menampilkan semua harga dari masing masing item
        
        if harga_toko < cheapest_price:     # jika harga lebih kecil dari cheapest_price
            cheapest_price = harga_toko     # maka harga akan menyesuaikan 

    print(f"Harga Termurah Untuk {entry}, Adalah {cheapest_price}")

    harga_beli = cheapest_price * items_to_buy[entry]   # harga beli = harga termurah tadi dikali
    sum += harga_beli

    print('-----------------------------')

print()
print(f'Total Harga Termurah :{sum}')
