import random as r
ans = r.randint(1, 99)
min = 0
max = 100
count = 5
while count > 0:
    # 使用者猜
    guess = int(input('(%d). 請輸入 %d ~ %d :' % (count, min, max)))
    if guess >= max or guess <= min: # 檢查輸入數值
        print('請重新輸入')
        continue
    # 將 count 減去一次
    count = count - 1
    # 判定結果
    if guess > ans:
        max = guess
    elif guess < ans:
        min = guess
    else:
        print('使用者答對了')
        break

    # 電腦猜
    guess = r.randint(min + 1, max - 1)
    print('(%d). 電腦猜 %d ~ %d : %d' % (count, min, max, guess))
    # 判定結果
    if guess > ans:
        max = guess
    elif guess < ans:
        min = guess
    else:
        print('電腦答對了')
        break















