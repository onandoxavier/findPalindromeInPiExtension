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
palindrome_size = 21
batch = 1000 - palindrome_size
limit_request = 1000000000
interval_request = 0.5

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
#i = 12942000 #12943000 -> interval = 4 - batch = 1000 -        numeros no total de 7:05
#i = 13831000 #13832000 -> interval = 2 - batch = 1000 - 103000 numeros no total de 0:04
#i = 13933000 #13934000 -> interval = 2 - batch = 1000 - 308000 numeros no total de 0:08
#i = 14240000 #14241000 -> interval = 4 - batch = 1000 - 93000 numeros no total de 0:07
#i = 14332000 #14333000 -> interval = 0.5 - batch = 1000 - 2055000 numeros no total de 0:29
#i = 16386000 #16387000 -> interval = 0.5 - batch = 1000 - 19198000 numeros no total de 0:40
#i = 19197000 #19198000 -> interval = 0.5 - batch = 1000 - 1105000 numeros no total de 0:15
#i = 20301000 #20302000 -> interval = 0.5 - batch = 1000 - 1219000 numeros no total de 0:17
#i = 21519000 #21520000 -> interval = 0.5 - batch = 1000 - 558000 numeros no total de 0:08
#i = 22076000 #22077000 -> interval = 0.5 - batch = 1000 - 2189000 numeros no total de 0:51
#i = 24263000 #24264000 -> interval = 0.5 - batch = 1000 - 549219 numeros no total de 0:08 # virada de chave
#i = 24812198 # interval = 0.5 - batch = 1000 - 616770 numeros no total de 0:08
#i = 25428947 # interval = 0.5 - batch = 1000 - 839982 numeros no total de 0:12
#i = 26268908 # interval = 0.5 - batch = 1000 - 777326 numeros no total de 0:11
#i = 27046213 # inverval = 0.5 - batch = 1000 - 662783 numeros no total de 0:09
#i = 27708975 # inverval = 0.5 - batch = 1000 - 337755 numeros no total de 0:04
#i = 28046709 # inverval = 0.5 - batch = 1000 - 353419 numeros no total de 0:05
#i = 28400107 # inverval = 0.5 - batch = 1000 - 709775 numeros no total de 0:10
#i = 29109861 # inverval = 0.5 - batch = 1000 - 436634 numeros no total de 0:06
#i = 29546474 # inverval = 0.5 - batch = 1000 - 378873 numeros no total de 0:05
#i = 29925326 # inverval = 0.5 - batch = 1000 - 1481227 numeros no total de 0:21
#i = 31406532 # inverval = 0.5 - batch = 1000 - 2269322 numeros no total de 1:44
#i = 33675833 # inverval = 0.5 - batch = 1000 - 3172939 numeros no total de 0:45
i = 36848751
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
        URL = f'{uri}{url_param1}={(i) - (palindrome_size)}&{url_param2}={batch + palindrome_size}'
        #print(f'{i} digitos analisados até agora...')
        print(f'de {(i) - (palindrome_size)} ate {((i) - (palindrome_size)) + (batch + palindrome_size)}')
        r = requests.get(url=URL)
        data = r.json()
        pi = data['content']
        #print(pi)
        answer = find_prime_palindrome(pi, palindrome_size)
        if answer != "":
            find = True
            print('Encontrado PORRA CARALHO PRESTA ATENCAO FOI!!!!!')
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
