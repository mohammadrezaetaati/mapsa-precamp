number_shoes=input()
size_shop=input().split()
number_customer=input()

money=0
for c in range(int(number_customer)):
    size_price=input().split()
    if size_price[0] in size_shop:
        money+=int(size_price[1])
        size_shop.remove(size_price[0])
print(money)