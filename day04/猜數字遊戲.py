import random as r
ans = r.randint(1, 99)
min = 0
max = 100
count = 5
while count > 0:
    guess = int(input('(%d). 請輸入 %d ~ %d :' % (count, min, max)))
    if guess >= max or guess <= min: # 檢查輸入數值
        print('請重新輸入')
        continue
    # 將 count 減去一次
    count = count - 1
    if guess > ans:
        max = guess
    elif guess < ans:
        min = guess
    else:
        print('答對了')
        break