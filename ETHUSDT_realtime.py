import requests
import time

# URL API биржи
url = 'https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT'

# Начальное значение цены ETHUSDT
prev_price = None

# Бесконечный цикл
while True:
    # Отправляем GET-запрос к API биржи
    response = requests.get(url)
    
    # Получаем текущую цену ETHUSDT
    current_price = float(response.json()['price'])
    
    # Если это первая итерация цикла
    if prev_price is None:
        # Присваиваем начальное значение цены
        prev_price = current_price
    else:
        # Вычисляем относительное изменение цены
        price_change = (current_price - prev_price) / prev_price
        
          # Если относительное изменение цены > 0.01%
        if abs(price_change) > 0.0001:
            print(f'Price changed by {price_change*100:.2f}% over the last 1 second')


  # Если относительное изменение цены превышает 1%
        #if abs(price_change) > 0.01:   
            #print(f'Price changed by {price_change*100:.2f}% over the last 60 minutes')
                    
        # Обновляем значение предыдущей цены
        prev_price = current_price
    
    # Задержка между запросами в 1 секунду для теста
    time.sleep(1)
    # Задержка между запросами в 60 минут как по тз
    # time.sleep(3600)