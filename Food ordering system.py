from pymongo import MongoClient
from tabulate import tabulate as tb
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import os

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


#View menu
def view_menu():
    h=["Items","Price"]
    d=[]
    for item,price in menu.items():
        d.append((item,price))
    print(tb(d,headers=h,tablefmt="grid"))

# Ordering items:

def order():
    bill=0
    print("Welcome sir! What is your order?")
    print()
    i1=input("First item: ")
    if i1 in menu:
        bill+=menu[i1]
    else:
        print(f"Sorry! , We don't have {i1} on the menu")
    more=input("Do you want to order anything? (Y or N): ").upper()
    while more=="Y":
        i2=input("What do you like to order?: ")
        if i2 in menu:
            bill+=menu[i2]
        else:
            print(f"Sorry! , We don't have {i2} on the menu")
        more=input("Do you need anything?: (Y or N) ").upper()
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

# Generate pdf bill

def generate_pdf_bill():
    # Fetching customer name and bill from MongoDB (use the name from the order or the last entry)
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Food_Order_System"]
    c = db["Customer_Data"]
    last_order = c.find().sort("_id", -1).limit(1)[0]  # Get the most recent order
    customer_name = last_order["Name"]
    total_bill = last_order["Total_Bill"]
    pdf_filename = f"order_bill_{customer_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    c = canvas.Canvas(pdf_filename, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 18)
    c.drawString(200, height - 50, "YJ Restaurant - Order Bill")
    c.setFont("Helvetica", 12)
    c.drawString(30, height - 100, f"Customer Name: {customer_name}")
    c.drawString(30, height - 120, f"Order Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.setFont("Helvetica-Bold", 14)
    c.drawString(30, height - 160, f"Total Bill: Rs. {total_bill}")
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(30, 50, "Thank you for dining with us! Visit us again.")
    c.setFont("Helvetica", 8)
    c.drawString(30, 30, "Address: YJ Restaurant, Coimbatore")

    c.save()  # save the pdf

    print(f"\nPDF bill generated: {pdf_filename}")
    if os.name == 'posix':
        os.system(f'open {pdf_filename}')
    elif os.name == 'nt':
        os.system(f'start {pdf_filename}')
    else:
        print("Could not open the PDF automatically. Please open it manually.")

# Main

def main():
    while True:
        print("\n Welcome to YJ restaurant\n")
        print("1. View Menu")
        print("2. Order items")
        print("3. Generate Pdf bill")
        print("4. Exit\n")
        choice=input("Enter your choice (1-3): ")
        if choice=='1':
            view_menu()
        elif choice=='2':
            order()
        elif choice=='3':
            generate_pdf_bill()
        elif choice=='4':
            print("Thank You for visiting our restaurant! Have a great day!")
            break

main()



