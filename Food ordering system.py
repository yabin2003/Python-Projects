
from pymongo import MongoClient
from tabulate import tabulate as tb

# Menu
menu = {
    "Chicken Biriyani": 120,
    "Mutton Biriyani": 200,
    "Vegetable Biriyani": 110,
    "Paneer Butter Masala": 150,
    "Butter Chicken": 180,
    "Dal Tadka": 90,
    "Chicken Korma": 160,
    "Mutton Korma": 220,
    "Shahi Paneer": 160,
    "Aloo Gobi": 85,
    "Chole Bhature": 130,
    "Chana Masala": 110,
    "Palak Paneer": 140,
    "Chicken Tikka": 140,
    "Mutton Kebab": 250,
    "Paneer Tikka": 130,
    "Tandoori Chicken": 180,
    "Fish Curry": 220,
    "Chicken Curry": 160,
    "Mutton Curry": 240,
    "Prawn Curry": 250,
    "Gosht Nihari": 260,
    "Lamb Rogan Josh": 230,
    "Chicken Vindaloo": 170,
    "Mutton Vindaloo": 220,
    "Hyderabadi Haleem": 220,
    "Mutton Seekh Kebab": 230,
    "Fish Tikka": 200,
    "Prawn Masala": 270,
    "Grilled Fish": 250,
    "Vegetable Pulao": 100,
    "Jeera Rice": 60,
    "Garlic Naan": 40,
    "Butter Naan": 35,
    "Plain Naan": 30,
    "Tandoori Roti": 25,
    "Chapati": 15,
    "Pineapple Raita": 50,
    "Boondi Raita": 40,
    "Plain Raita": 30,
    "Papad": 15,
    "Naan":30,
    "Samosa": 20,
    "Pakora": 25,
    "Spring Roll": 30,
    "Veg Hakka Noodles": 110,
    "Chicken Hakka Noodles": 130,
    "Vegetable Manchurian": 120,
    "Gulab Jamun": 50,
    "Jalebi": 60,
    "Rasgulla": 40,
    "Carrot Halwa": 70,
    "Kulfi": 90,
    "Ice Cream (Vanilla)": 50,
    "Lassi (Sweet)": 80,
    "Masala Papad": 20,
    "Kachori": 25
}

# Ordering items:

def order():
    bill=0
    print("Welcome sir! What is your order?")
    print()
    i1=input("First item: ")
    if i1 in menu:
        bill+=menu[i1]
    more=input("Do you want to order anything? (Y or N): ")
    while more=="Y":
        i2=input("What do you like to order?: ")
        if i2 in menu:
            bill+=menu[i2]
        more=input("Do you need anything?: (Y or N) ")
    else:
        print(f"Thank you for ordering ! This is your bill amount - {bill}")
    dt=[]

    name=input("What's your good name sir? : ")
    dt.append((name,bill))

    headers=["Name","Total_Bill"]

    data={
        "Name":name,
        "Total_Bill":bill
    }
    client=MongoClient("mongodb://localhost:27017/")
    db=client["Food_Order_System"]
    c=db["Customer_Data"]
    result=c.insert_one(data)
    print(tb(dt,headers=headers,tablefmt="grid"))

order()