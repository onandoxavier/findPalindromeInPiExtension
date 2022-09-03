import math
import requests
import time
from datetime import datetime

start_time = datetime.now()
find = False
uri = f'https://api.pi.delivery/v1/pi?'
url_param1 = 'start'
url_param2 = 'numberOfDigits'
primeList = [2, 3, 5]
batch = 1000
palindrome_size = 21
limit_request = 1000000000
interval_request = 1

#i = 1
#i = 852
#i = 2258
#i = 5345
#i = 5801
#i = 6038
#i = 6114
#i = 6230
#i = 6230000
#i = 6319500 #6320000
#i = 6491500 #6492000
#i = 6722000 #6723500 -> interval = 2 - batch = 500 - 599000 numeros no total de 1h01
#i = 7320500 #7321000 -> interval = 1 - batch = 500 - 413000 numeros no total de 0h20
#i = 7733000 #7733500 -> interval = 1 - batch = 1000 - 370000 numeros no total de 0:08
#i = 8102000 #8103000 -> interval = 1 - batch = 1000 - 565000 numeros no total de 0:14
#i = 8666000 #8667000 -> interval = 1 - batch = 1000 - 895000 numeros no total de 0:21
#i = 9560000 #9561000 -> interval = 1 - batch = 1000 - 785000 numeros no total de 0:19
#i = 10344000 #10345000 -> interval = 1 - batch = 1000 - 894000 numeros no total de 0:22
#i = 11237000 #11238000 -> interval = 1 - batch = 1000 - 1494000 numeros no total de 0:37
#i = 12730000 #12731000 -> interval = 1 - batch = 1000 - 213000 numeros no total de 0:05
i = 12942000 #12943000 -> interval = 1 - batch = 1000 - 
seed = i
# Metodo que valida se um número é primo
def is_prime_number(number):
    n = float(number)
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n % 3 == 0: return False
    if n % 5 == 0: return False

    # Mantive uma lista de primos encontrados para evitar reprocessamento
    for prime in primeList:
        if n % prime == 0:
            return False

    # Tive como limite da busca a raiz quadrada do numero que estava procurando
    limit = math.ceil(math.sqrt(n))
    aux = primeList[-1] + 1
    while aux < limit:
        if is_prime_number(aux):
            primeList.append(aux)
            if n % aux == 0: return False
        aux += 1
    return True


# Metodo que valida se um número é ou nao palindromo
def is_palindrome(number):
    if len(number) % 2 != 0:
        for x in range(1, math.ceil(len(number) / 2)):
            if number[x-1] != number[-x]:
                return False
        return True
    else:
        for x in range(1, math.ceil(len(number) / 2)+1):
            if number[x-1] != number[-x]:
                return False
        return True


def find_prime_palindrome(_pi, size):
    for _i in range(0, (len(_pi) - 1) - math.ceil(size / 2)):
        num = _pi[_i:_i + size]
        if is_palindrome(num):
            if is_prime_number(num):
                return num
    return ""


'''URL = f'{uri}{url_param1}={0}&{url_param2}={batch}'
r = requests.get(url=URL)
data = r.json()
pi = data['content']
answer = find_prime_palindrome(pi, palindrome_size)
if answer != "":
    find = True
    print('Encontrado antes do looping!')
    print(answer)
else:
    find = False'''

try:
    while find is not True and i < limit_request:
        URL = f'{uri}{url_param1}={(i) - (palindrome_size - 1)}&{url_param2}={batch}'
        print(f'{i} digitos analisados até agora...')
        r = requests.get(url=URL)
        data = r.json()
        pi = data['content']
        answer = find_prime_palindrome(pi, palindrome_size)
        if answer != "":
            find = True
            print('Encontrado!')
            print(answer)

        else:
            find = False
            time.sleep(interval_request)
        i += batch
    print(f'Em {i} digitos analisados')

    if i >= limit_request:
        print(f'Voce atingiu o limite de {limit_request} requisicoes')
except Exception as e:
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
    print(f'foram processados {i-seed} na ultima execucao')
    print(str(e))
