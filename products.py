products = []

while True:
	name = input('Please enter the product\'s name: ')
	if name == 'q': #quit
		break
	price = input('Please enter the product\'s price: ')
	p = []
	p.append(name)
	p.append(price)

	products.append(p)

print(products)

for p in products:
	print('The product\'name is: ', p[0], 'and it\'s price is: ', p[1])
