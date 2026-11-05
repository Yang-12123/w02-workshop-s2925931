p = 1
q = 1

fibo = [1, 1]

next_val_1 = p * fibo[1] + q * fibo[0]
fibo.append(next_val_1)

next_val_2 = p * fibo[2] + q * fibo[1]
fibo.append(next_val_2)

print(fibo)
