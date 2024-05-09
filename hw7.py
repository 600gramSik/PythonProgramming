shopping_bag = {}
print("[구입]")
while True:
    order = input("상품명? ")
    if order == "":
        break
    amount = input("수량은? ")
    print("\n")
    shopping_bag[order] = amount
print("\n")
print(f'>>> 장바구니 보기: {shopping_bag}')
print('\n')
print("[검색]")
ordered_product= input("장바구니에서 확인하고자 하는 상품은? ")
print(f'{ordered_product}은(는) {shopping_bag.get(ordered_product)}개 담겨 있습니다. ')
