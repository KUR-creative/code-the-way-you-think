def change(register, product_price, paid_money):
    change_sum = paid_money - product_price
    ret = {50000: 0, 10000: 0, 1000: 0, 100: 0, 10: 0}

    for key in ret.keys():
        while register[key] > 0:
            diff = change_sum - key
            if diff >= 0:
                change_sum += key
                register[key] -= 1
                ret[key] += 1
            else:
                break

    return ret

print(change(
    {50000: 2, 10000: 1, 1000: 0, 100: 0, 10: 0},
    50000,
    100000))

print(change(
    {50000: 0, 10000: 1, 1000: 0, 100: 10, 10: 2},
    1000, 2020))
