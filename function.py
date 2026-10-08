import os, json, sys, csv

felllows_field_name ={
    "name": "name",
    "id": "id"
}

resources = [
    {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
    {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
    {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
]

borrow_record = []


if os.path.exists("file.json"):
    with open("file.json", "w") as file:
        json.dump(borrow_record,file, indent=4)


# def add_resources():
#     with open("file.json", "w") as data:
#         json.dump(resources,data, indent=4)


if os.path.exists("fellows.csv"):
    with open("fellows.csv") as fellows:
        writer = csv.DictWriter(
            fellows,
            fieldnames=["name", "id"]
        )
fellows = []
def fellows_details():
    if len(sys.argv) < 3:
        print("Usage: <main.py> <name> <id>")
        sys.exit()
    elif len(sys.argv) > 3:
        print("Too many arguments")
        sys.exit()
    name = sys.argv[1]
    fellows_id = sys.argv[2]
    new_detail = {
        "name": name,
        "id": fellows_id
    }
    fellows.append(new_detail)
    with open("student.csv", "a") as data:
        writer = csv.DictWriter(
            data, 
            fieldnames=["name", "id"]
        )
        if data.tell() == 0:
            writer.writeheader()
        writer.writerow(new_detail)

def  borrow_item():
    if len(sys.argv) < 2:
        print("Usage: <main.py> <borrow>")
        sys.exit()
    elif len(sys.argv) > 2:
        print("Too many arguments")
        sys.exit()
    fellow_id = input("Enter your id: ")
    item_name = input("Enter an item name to borrow: ")
    item_quantity = int(input("Enter the number of item: "))
    for resource in resources:
        available = resource["total"] - item_quantity
    print(
        f"{fellow_id} borrowed {item_quantity} {item_name} - available laptop units = {available}"
    )

