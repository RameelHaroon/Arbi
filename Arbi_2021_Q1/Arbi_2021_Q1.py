import json
import requests
import sys


def read_file(filename):

    noOfProducts = 0
    products = []
    with open(filename, 'r') as infile:

        noOfProducts = int(infile.readline())
        tempProducts = infile.readlines() 

        for each in tempProducts:
            line = each.strip().split(',')
            products.append([line[0],int(line[1])])

    return noOfProducts, products


def check_products(product, productsData):
    
    result = 0

    for item in productsData:
        if product[0] == item['collection']:
            # Matching the collection name

            # Calculating discount
            price = item['price']
            previousPrice = item['previous_price']
            discount = ((previousPrice - price) / previousPrice) * 100

            if discount >= product[1]:
                # Discount is greater the percentage limit
                result += 1
    return result


def main():

    filepath = 'input.txt' # sys.argv[1]
    try:
        noOfProducts, productCollections = read_file(filepath)

        jsonURL = 'https://www.jsonkeeper.com/b/ZVOV'
        response = requests.get(jsonURL)
        productsData = response.json()

    except:
        print("Error")
    else:

        for productNumber in range(noOfProducts):
            
            noOfRecords = check_products(productCollections[productNumber], productsData)
            print(f'{noOfRecords} found against {productCollections[productNumber][0]}')
        

if __name__ == '__main__':
    main()