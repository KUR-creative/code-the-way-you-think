def change(register, product_price, paid_money):
    if product_price > paid_money:
        return {}

    change_sum = paid_money - product_price
    ret = {50000: 0, 10000: 0, 1000: 0, 100: 0, 10: 0}

    for won in sorted(ret.keys(), reverse=True):
        while register[won] > 0 and change_sum >= won:
            change_sum -= won
            register[won] -= 1
            ret[won] += 1
    return ret
