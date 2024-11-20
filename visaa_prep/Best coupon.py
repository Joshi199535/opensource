X = int(input())
discount_10 = X * 0.10
amount_after_10 = X - discount_10
amount_after_100 = X - 100
max_discount = min(amount_after_10, amount_after_100)
print(int(max_discount))
