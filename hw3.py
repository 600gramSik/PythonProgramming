def get_fixed_price (discounted_price, discount_rate):
    original_price = discounted_price / (1 - (discount_rate / 100))
    return original_price

# 사용자로부터 할인율 입력 받기
discount_rate = float(input("할인율은? "))

# 사용자로부터 상품 A의 할인된 가격 입력 받기
dp_A = float(input("A 상품의 할인된 가격은? "))

# 사용자로부터 상품 B의 할인된 가격 입력 받기
dp_B = float(input("B 상품의 할인된 가격은? "))


# 상품 A의 정가 계산
original_price_A = get_fixed_price(dp_A, discount_rate)
print(f"A 상품의 정가는 {original_price_A:.0f} 원")

# 상품 B의 정가 계산
original_price_B = get_fixed_price(dp_B, discount_rate)
print(f"B 상품의 정가는 {original_price_B:.0f} 원")
