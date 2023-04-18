def get_shipping_cost(quantity):
    return 1000 + 120 * (quantity - 1)
n = int(input())
print(get_shipping_cost(n))