def buy(sb):
    name = input("상품명? ")
    quantity = int(input("수량은? "))
    print(f'장바구니에 {name} {quantity}개가 담겼습니다.')
    shopping_bag.append(sb)
    return True

def show(sb):
    print






shopping_bag = {}
while True:
    if  buy(shopping_bag) == False:
        break
    show(shopping_bag)
    find(shopping_bag)