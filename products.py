import os

products = []
if os.path.isfile('products.csv'):
	print('Find files!')
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if "商品,价格" in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
		print(products)
else:
	print('Cannot find files!')

while True:
	name = input('Please enter the product\'s name: ')
	if name == 'q': #quit
		break
	price = input('Please enter the product\'s price: ')
	# p = []
	# p.append(name)
	# p.append(price)

	products.append([name, price])

print(products)

for p in products:
	print('The product\'name is: ', p[0], 'and it\'s price is: ', p[1])

with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,价格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

