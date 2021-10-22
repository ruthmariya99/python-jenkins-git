from functools import reduce
products = [
{
'productId':1,
'productName':'Iphone',
'price':135556.5
},
{
'productId': 4,
'productName':'Oneplus',
'price':69999.5
},
{
'productId':3,
'productName':'SamsungFlip',
'price':149999.5
}

]
def myFunc():
return ""
print(reduce(lambda price1, price2 : price1+price2,(map(lambda p : p['price'],filter(lambda product: product['price'] > 10000.0, products))),10))

myFunc()