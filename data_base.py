import json 

def read_file()-> list[dict]:
    f = open("data_base.json", "r")
    content = f.read()
    data = json.loads(content)
    return data


def write_file(tasks: list[dict]):
    fh = open("data_base.json", "w")
    data = json.dumps(tasks, indent= 4 )
    fh.write(data)


def add_products_db(Name: str, descreption: str, price: int, category: str, quantity: int):
    data = read_file()
    data['products'].append( 
        {
        'id': data['current_id'],
        'name': Name,
        'price': price,
        'category': category,
        'descreption': descreption,
        'quantity': quantity,
        'in_stock': True
        }
        )
    data['current_id'] += 1
    write_file(data)


def check_status_db(id: int):
    data = read_file()
    for product in data['products']:
        if product['id'] == id:
            if product['quantity'] == 0:
                product['in_stock'] = False
            else:
                product['in_stock'] = True
    
                write_file(data)
                return product
            
    return None

            

def get_all_product_db():
    data = read_file()
    return data['products']



def show_details_db(product_id: int):
    data = read_file()
    for product in data['products']:
        if product['id'] == product_id:
            print(f"Product ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: {product['price']}")
            print(f"category: {product['category']}")
            print(f"descreption: {product['descreption']}")
            print(f"Quantity: {product['quantity']}")
            print(f"In Stock: {product['in_stock']}")
            print("---------------------------------------")



def show_numbers_db(id: int):
    data = read_file()
    for product in data['products']:
        if product['id'] == id:
            print(f"Quantity of the product with id {id} is: {product['name']}: {product['quantity']} - available in stock")
            return
   



def search_product_db(search: str):
    data = read_file()
    for product in data['products']:
        if search.lower() in product['name'].lower() or search.lower() in product['descreption'].lower():
            print(f"Product ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: {product['price']}")
            print(f"category: {product['category']}")
            print(f"descreption: {product['descreption']}")
            print(f"Quantity: {product['quantity']}")
            print(f"In Stock: {product['in_stock']}")
            print("---------------------------------------")
           
        

    


def delete_product_db(id: int):
    data = read_file()
    for product in data['products']:
        if product['id'] == id:
            data['products'].remove(product)
            write_file(data)
            print(f"Product with id {id} has been deleted.")
            return




def price_product_bd(id: int):
    data = read_file()
    for product in data['products']:
        if product['id'] == id:
            print(f"Price of the product with id {id} is: {product['name']}: {product['price']} - available in stock")
            return
        


def all_category_product_db(category: str):
    data = read_file()
    for product in data['products']:
        if product['category'].lower() == category.lower():
            print(f"product ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"category: {product['category']}")      
            print("-----------------Finished----------------------")


        



