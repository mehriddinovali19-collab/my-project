from data_base import (add_products_db, all_category_product_db, check_status_db, get_all_product_db, price_product_bd, search_product_db,
                       show_details_db, show_numbers_db, delete_product_db)




def handle_add_products_h():
    print("------------------Add Product------------------")
    Name = input("Enter name of the product: ")
    descreption = input("descreption of the product: ")
    price = int(input("Enter price of Product: "))
    category = input("Enter category of the product: ")
    quantity = input("quantity : ")
    add_products_db( Name, descreption, price, category, quantity)
    print("Product has been added successfully")




def handle_check_status_h():
    id = int(input("Enter id of the product: "))
    print("------------------Products status------------------")
    product = check_status_db(id)

    if product:
        print(f"Product ID: {product['id']}")
        print(f"Name: {product['name']}")
        print(f"Price: {product['price']}")
        print(f"Quantity: {product['quantity']}")
        print(f"In Stock: {product['in_stock']}")
    else:
        print("Product topilmadi")


def handle_show_product_h():
    products = get_all_product_db()
    print("------------------Products in Database------------------")
    for product in products:
        print(product['id'], product['name'])


def handle_show_details_h():
    id = int(input("Enter if of the product which you want to see: "))
    print("------------------Products Details------------------")
    show_details_db(id)
    


def handle_show_numbers_h():
    id = int(input("Enter an id of product which you want to know how many avaliavle here: "))
    print("------------------Products shown number------------------")

    show_numbers_db(id)




def handle_search_product_h():
    search = input("Enter search term: ")
    print("------------------Products searched------------------")
    search_product_db(search)


def handle_delete_product_h():
    id = int(input("Enter id of the product which you want to delete: "))
    print("------------------Products Deleted------------------")
    delete_product_db(id)
    


def handle_price_product_h():
    id = int(input("Enter id of the product which you want to know the price: "))
    print("------------------Products Price------------------")
    price_product_bd(id)


def handle_all_category_product_h():
    category = input("Enter category of the product which you want to see: ")
    print("------------------Products in category------------------")
    all_category_product_db(category)

