products = [
    {"name": "Smartphone", "price": 15000, "description": "A handheld device used for communication and browsing the internet."},
    {"name": "Laptop", "price": 100000, "description": "A portable computer that is easy to carry around."},
    {"name": "Headphones", "price": 2500, "description": "A pair of earphones worn over the head to listen to music."},
    {"name": "Smartwatch", "price": 3000, "description": "A wearable device used for fitness tracking and receiving notifications."},
    {"name": "Bluetooth speaker", "price": 10000, "description": "A portable speaker that connects wirelessly to devices using Bluetooth technology."}
]
Cart =[]
while True:
    choice=input("Do you want to continue shopping ? : ")
    if choice.lower()=="yes" :
        print("here is a list of products and their prices .")
        for index,product in enumerate(products):
            print(f"{index}:{product['name']}: Rs{product["price"]}:{product["description"]}" )
        product_id = int(input("Enter the id of  the product you want to add to the cart "))

    # check if the product is already present in the cart
        if products[product_id] in Cart:
            products[product_id]["quantity"] +=1
        else:
            products[product_id]["quantity"]=1
            Cart.append(products[product_id])
        Total=0
        print("Here are the contents in your cart")
        for product in Cart:
            print(f"{product['name']}:{product['description']}:Rs{product['price']}:QTY:{product['quantity']}")
            Total+=product['price']*product['quantity']
        print(f"Cart total is : Rs.{Total}")
    else:
        break
    print("Thank you, your final cart contents are {Cart}")



