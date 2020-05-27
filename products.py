import os
# read files
def read_file(file_name):
	products = []
	if os.path.isfile(file_name):
		print('Find files!')
		with open(file_name, 'r', encoding = 'utf-8') as f:
			for line in f:
				if "商品,价格" in line:
					continue
				name, price = line.strip().split(',')
				products.append([name, price])
			print(products)
	else:
		print('Cannot find files!')
		return products

# input information
def user_input(products):
	while True:
		name = input('Please enter the product\'s name: ')
		if name == 'q': #quit
			break
		price = input('Please enter the product\'s price: ')
		products.append([name, price])
	print(products)
	return products

# print all products
def print_products(products):
	for p in products:
		print('The product\'name is: ', p[0], 'and it\'s price is: ', p[1])

# write the new file
def write_file(file_name, products):
	with open(file_name, 'w', encoding = 'utf-8') as f:
		f.write('商品,价格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

products = read_file('products.csv')
products = user_input(products)
print_products(products)
write_file('products.csv', products)