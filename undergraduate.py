# 한참 짠 뒤 예시를 넣어 보고, 프린트하면서 버그를 잡는다.
# try 1: 일단 끝까지 짜본다
def change(register, product_price, paid_money):
    change_sum = paid_money - product_price
    # 일단 줘야할 돈은 이렇겠지?

    ret = {10: 0, 100: 0, 1000: 0, 10000: 0, 50000: 0}
    #반환도 dict니까 이러면 될거야

    for key in ret.keys(): # 사실 큰 지폐 먼저 지급해야되는데, 나중에 고침
        while register[key] > 0: # 레지스터에 있을 때
            diff = change_sum - register[key]
            if diff > 0: # >= 이 맞는데 일단 간다
                change_sum -= diff
                register[key] -= 1
                ret[key] += 1
    return ret

#print(change({50000: 2, 10000: 1, 1000: 0, 100: 0, 10: 0}, 50000, 100000))
# 왜 아무것도 안 뜰까? 무한 루프

# try 2: 무한 루프를 고치기 위해 코드를 뚫어져라 본다. w를 프린트해보고 고친다.
def change(register, product_price, paid_money):
    change_sum = paid_money - product_price
    ret = {10: 0, 100: 0, 1000: 0, 10000: 0, 50000: 0}

    for key in ret.keys():
        while register[key] > 0:
            diff = change_sum - register[key]
            print(diff)
            if diff > 0:
                change_sum -= diff
                register[key] -= 1
                ret[key] += 1
            else: # 2) 무한루프인 걸 확인하고 else를 넣음
                break
            print('w') # 1) 루프를 체크해 본다.
    return ret

# 10만원 주고 50000원 냈으니 50000원 하나가 돌아오는 것을 원한다.
#print(change({50000: 2, 10000: 1, 1000: 0, 100: 0, 10: 0}, 50000, 100000))
#=> {10: 0, 100: 0, 1000: 0, 10000: 1, 50000: 0}
# 되네? 이걸로 끝? 하나만 더 해보자

#print(change({50000: 0, 10000: 1, 1000: 0, 100: 10, 10: 2}, 1000, 2020))
#=> {10: 2, 100: 0, 1000: 0, 10000: 0, 50000: 0}
# 뭔가 잘못되었다. 뭘까? 디버깅을 시작하자!

# try 3: key를 출력해보고 정렬되지 않은 것을 확인
def change(register, product_price, paid_money):
    change_sum = paid_money - product_price
    ret = {10: 0, 100: 0, 1000: 0, 10000: 0, 50000: 0}

    for key in sorted(ret.keys(), reverse=True): # 2) 확인하고 고친다.
        print(key) # 1) key가 작은 것부터 나오고 있다. 그러고 보니 큰거부터 해야지
        while register[key] > 0:
            diff = change_sum - register[key]
            if diff > 0:
                change_sum -= diff
                register[key] -= 1
                ret[key] += 1
            else:
                break
    return ret

#print(change({50000: 2, 10000: 1, 1000: 0, 100: 0, 10: 0}, 50000, 100000))
#=> {10: 0, 100: 0, 1000: 0, 10000: 0, 50000: 2} 왜 5만원이 하나가 아냐
#print(change({50000: 0, 10000: 1, 1000: 0, 100: 10, 10: 2}, 1000, 2020))
#=> {10: 0, 100: 0, 1000: 0, 10000: 1, 50000: 0} 왜 100원이 안 나와?
# 왜 둘 다 틀리나?

# try 4: diff를 출력해본다. 아! 고친다.
def change(register, product_price, paid_money):
    change_sum = paid_money - product_price
    ret = {10: 0, 100: 0, 1000: 0, 10000: 0, 50000: 0}

    for key in sorted(ret.keys(), reverse=True): # 2) 확인하고 고친다.
        while register[key] > 0:
            #diff = change_sum - register[key]
            diff = change_sum - key # 2) 수정
            print(diff) # 1) diff 출력
            if diff > 0:
                change_sum -= diff
                register[key] -= 1
                ret[key] += 1
            else:
                break
    return ret
#print(change({50000: 2, 10000: 1, 1000: 0, 100: 0, 10: 0}, 50000, 100000))
#=> {10: 0, 100: 0, 1000: 0, 10000: 1, 50000: 0} 왜 5만원이 하나가 아냐.. 여전히 틀림
#print(change({50000: 0, 10000: 1, 1000: 0, 100: 10, 10: 2}, 1000, 2020))
#=> {10: 1, 100: 1, 1000: 0, 10000: 0, 50000: 0} 여전히 틀렸네..?

# try 5: 잘 보니... diff >= 0 이 문제였다!
def change(register, product_price, paid_money):
    change_sum = paid_money - product_price
    ret = {10: 0, 100: 0, 1000: 0, 10000: 0, 50000: 0}

    for key in sorted(ret.keys(), reverse=True): # 2) 확인하고 고친다.
        while register[key] > 0:
            diff = change_sum - key
            if diff >= 0: # 1) 어떻게든 보고 고침. 어떻게? "사실 저는 학부생이 아닙니다 ㅎㅎ; 짬이 있다 이말이야"
                change_sum -= diff
                register[key] -= 1
                ret[key] += 1
            else:
                break
    return ret
#print(change({50000: 2, 10000: 1, 1000: 0, 100: 0, 10: 0}, 50000, 100000))
#=> {10: 0, 100: 0, 1000: 0, 10000: 1, 50000: 2} # <- 이거 사실 틀렸는데 걍 넘어가버림
#print(change({50000: 0, 10000: 1, 1000: 0, 100: 10, 10: 2}, 1000, 2020))
#=> {10: 2, 100: 10, 1000: 0, 10000: 0, 50000: 0}

# 오... 이제 된다. 이걸로 끝?
#print(change({50000: 10, 10000: 10, 1000: 10, 100: 10, 10: 10}, 1120, 2340))
# {10: 10, 100: 10, 1000: 10, 10000: 0, 50000: 0} 천원 하나, 100원 두개, 10원 하나인데..

# try 5: 루프에서 변수를 다 출력해본다.
def change(register, product_price, paid_money):
    change_sum = paid_money - product_price
    ret = {10: 0, 100: 0, 1000: 0, 10000: 0, 50000: 0}

    for key in sorted(ret.keys(), reverse=True): # 2) 확인하고 고친다.
        while register[key] > 0:
            diff = change_sum - key
            if diff >= 0:
                print(key, change_sum, register, ret) # 1) 변수를 다 출력해봄
                #change_sum -= diff # 2) diff가 아니라 key를 빼야 한다!
                change_sum -= key # 2) diff가 아니라 key를 빼야 한다!
                register[key] -= 1
                ret[key] += 1
            else:
                break
    return ret

print(change({50000: 2, 10000: 1, 1000: 0, 100: 0, 10: 0}, 50000, 100000))
#=> {10: 0, 100: 0, 1000: 0, 10000: 1, 50000: 2}
print(change({50000: 0, 10000: 1, 1000: 0, 100: 10, 10: 2}, 1000, 2020))
#=> {10: 2, 100: 10, 1000: 0, 10000: 0, 50000: 0}
print(change({50000: 10, 10000: 10, 1000: 10, 100: 10, 10: 10}, 1120, 2340))
#=> {10: 2, 100: 2, 1000: 1, 10000: 0, 50000: 0}

# 이제 진짜 끝인가?
# 과연 디버깅의 끝은 어딜까?
# 이걸 언제까지 해야하나..?
# 뭘 더 넣어서 확인해 봐야 할까........
