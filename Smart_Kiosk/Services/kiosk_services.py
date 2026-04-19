import uuid
from typing import Optional, List, Dict 

#Query 1: Place a new order for an item and quantity

#Find orders placed for an inventory id using item id

#Step 2: Find how many orders placed for the item using item id

#Find item information in inventory

def place_order(inventory: list, orders: list, item_id: str, quantity: int) -> Optional[Dict]:
    #Find item in the inventory
    item = find_inventory_item_by_item_id(inventory, item_id)
    #If it exists -> 
    if item:
        if item['stock'] >= quantity:
            item['stock'] = item['stock'] - quantity
            total_cost = item['unit_price']*quantity
            
            #If the stock > the quantity asked
                #Reduce the inventory
                #Then place the new order
            new_order = {
                "order_id":str(uuid.uuid4()),
                "item_id": item_id,
                "quantity": quantity,
                "status":"placed",
                "total_cost":total_cost
            }
            orders.append(new_order)
            return new_order

def find_inventory_item_by_item_id(inventory: list, item_id: str) -> Optional[Dict]:
    for item in inventory:
        if item['item_id'] == item_id:
            return item
    return None 

def update_order_status():
    pass 

def cancel_order():
    pass

def count_orders_for_item_by_item_id():
    pass