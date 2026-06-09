"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    Parameters:
        items (list): Items to create an inventory from.

    Returns:
        dict: The inventory dictionary.
    """
    result = {}
    for item in items:
        count = items.count(item)
        result[item] = count      
    return result

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    Parameters:
        inventory (dict): Dictionary of existing inventory.
        items (list): List of items to update the inventory with.

    Returns:
        dict: The inventory updated with the new items.
    """
    newlist = {}
    struct_items = create_inventory(items)
    for key, value in struct_items.items():
        newlist[key] = value + inventory.get(key,0)
    for key, value in inventory.items():
        newlist[key] = struct_items.get(key,0) + inventory.get(key,0)
    return newlist
        
def decrement_items(inventory, items):
    """Decription of the method"""
    for item in items:
        if inventory.get(item,0):
            inventory[item] = inventory[item] - 1
            if inventory[item] < 0:
                inventory[item] = 0
    return inventory
    
def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    Parameters:
        inventory (dict): Inventory dictionary.
        item (str): Item to remove from the inventory.

    Returns:
        dict: Updated inventory with item removed. Current inventory if item does not match.
    """
    inventory.pop(item,"unknown")
    return inventory

def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    Parameters:
        inventory (dict): An inventory dictionary.

    Returns:
        list[tuple]: List of key, value tuples from the inventory dictionary.
    """
    result = []
    for key, value in inventory.items():
        if value > 0:
            result.append((key,value))
    return result
