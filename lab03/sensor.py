thresh = float(input('Введите порог тревоги: '))
sm = 0
cnt = 0
mx = 0
thresh_cnt = 0
error_cnt = 0
n = int(input('Введите количество записей: '))
for i in range(n):
    tem = input()
    if tem != 'error':
        temp = float(tem)
    else:
        error_cnt += 1
        temp = tem
    if temp != 'error': 
        sm += temp
        cnt += 1
        if temp > mx: mx = temp
        if temp > thresh: thresh_cnt += 1