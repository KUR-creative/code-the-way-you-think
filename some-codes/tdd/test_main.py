from main import *

def test_paid_money_is_smaller_than_product_money_then_zero():
    assert {} == change({100: 1, 1000: 2}, 10000, 10)

def test_normal_cases():
    assert change(
        {50000: 2, 10000: 1, 1000: 0, 100: 0, 10: 0},
        50000, 100000
    ) == {50000: 1, 10000: 0, 1000: 0, 100: 0, 10: 0}

    assert {50000: 0, 10000: 0, 1000: 0, 100: 10, 10: 2} \
        == change({50000: 0, 10000: 1, 1000: 0, 100: 10, 10: 2},
                  1000, 2020)
