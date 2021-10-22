def judge_prime(x, prime_table):
    if x & 1:
        if x % 6 == 1 or x % 6 == 5:
            accu = 0
            for i in prime_table:
                if x // i != x / i:
                    accu += 1
                if accu == len(prime_table):
                    prime_table.append(x)


prime_list = [2, 3, 5, 7]
for k in range(7, 10000):
    judge_prime(k, prime_list)
print(prime_list)
