def exchange(money):
    fh = money // 500
    fhn = money % 500
    print("500원 동전의 개수: ", fh)
    oh = fhn // 100
    ohn = fhn % 100
    print("100원 동전의 개수: ", oh)
    ft = ohn // 50
    ftn = ohn % 50
    print("50원 동전의 개수: ", ft)
    t = ftn // 10
    print("10원 동전의 개수: ", t)


def get_integer(prompt_message):
    return int(input(prompt_message))

m = get_integer("동전으로 교환하고자 하는 금액은? ")
exchange(m)


