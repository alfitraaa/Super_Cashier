'''
This module contains Transaction class and methods contained in it,
this module must be run first. After running, it can be imported into the main module
so that it can run the self-service super cashier program.   

'''

# Import the library that will be used in this module
from datetime import datetime

# Create class from transaction ID
class Transaction:
  def __init__(self):
    self.item_list = {} # Defines an attribute in the class, empty dictionary

  def __str__(self):
    '''
    Defines several attributes in the Transaction class with special method __str__()
    so that the instances or attributes can later be called when it is printed.

    As well as grouping into each category: name, quantity, price of items
    to make the process of the function easier.

    '''
    self.name = [str(key[0]) for key in self.item_list.items()]
    self.quantity = [qty[0] for qty in [values for values in self.item_list.values()]]
    self.price = [prc[1] for prc in [values for values in self.item_list.values()]]
    self.grand_total_price = 0
    return str(self.item_list)

# 1. Create a method to add shopping items.
  def add_item(self, name, qty, price):
    '''
    Method to add items to the shopping list

    Parameters:
    - name: item name, data type: string
    - qty: number of items, data type: integer
    - price: item price, data type: integer
    
    '''
    self.name = name
    self.qty = qty
    self.price = price
    self.item_list.update({name:[qty, price]})

# 2. Create a method to update the item name
  def update_item_name(self, name, new_name):
    '''
    Method to update the item name.

    Parameters:
    - name: the old name of the item that will be changed, data type: string
    - new_name: the new name of the item, data type: string
    
    '''
    self.new_name = new_name
    self.item_list[new_name] = self.item_list[name]
    del self.item_list[name]

# 3. Create a method to update the items quantity
  def update_item_qty(self, name, new_qty):
    '''
    Method to update the item quantity.

    Parameters:
    - name: the name of the item that we want to change the quantity, data type: string
    - new_qty: the new quantity of the item, data type: integer
    
    '''
    self.new_qty = new_qty
    self.item_list[name][0] = new_qty

# 4. Create a method to update the item price.
  def update_item_price(self, name, new_price):
    '''
    Method to update the item price.

    Parameters:
    - name: the name of the item that we want to change the price, data type: string
    - new_qty: the new price of the item, data type: integer
    
    '''
    self.new_price = new_price
    self.item_list[name][1] = new_price

# 5. Create a method to delete an item.
  def delete_item(self, name):
    '''
    Method for deleting an item.
    The quantity and price of the item that has been entered will also be deleted.

    Parameters:
    - name: the name of the item that will be deleted, data type: string
    
    '''
    del self.item_list[name]

# 6. Create a method to delete all items.
  def reset_transaction(self):
    '''
    Method to delete all items in the list,
    with a question to confirm the action.

    Parameters: -

    Expected input: 'yes' or 'no', lowercase or uppercase.
    
    '''
    answer = input('Are you sure you want to delete all item in the list? This action cannot be undone. (yes / no):' )
    if answer.lower() == 'yes':
      self.item_list.clear()
      print('All items deleted successfully')
    elif answer.lower() == 'no':
      print('The items list is not deleted')
    else:
      print('Your answer is wrong')

# 7. Create a method to check the shopping list
  def check_order(self):
    '''
    Method to check the list of items,
    as well as inform whether there is an error in the form of an incorrect input or not,
    and also displays the list. 

    Parameters: -
    
    '''
    check_wrong_input = []
    # Check one by one the quantity of each item, whether the data type is integer or not.
    for qty in self.quantity:
      if type(qty) == int:
        check_wrong_input.append(1)
      else:
        check_wrong_input.append(0)
      
    # Check one by one the price of each item, whether the data type is integer or not.
    for prc in self.price:
      if type(prc) == int:
        check_wrong_input.append(1)
      else:
        check_wrong_input.append(0)
    
    # Displays all item in the list if there are no input errors confirmed.
    if all(check_wrong_input):
      print('Order is correct')
      print()
      print(f'| No | Item Name               | Quantity | Price     | Total Price     |')
      n = 0
      for item in self.item_list:
        print(f'| {n+1}  | {self.name[n].ljust(23)} | {str(self.quantity[n]).ljust(8)} | {str(self.price[n]).ljust(9)} | {str(self.quantity[n]*self.price[n]).ljust(15)} |')
        n += 1
    # If there is an input error, it will be notified.
    else:
      print('There is a data input error')
      print()
      print(self.item_list)
      print()
      print('Check your shopping list again')

# 8. Create a method to calculate the total price and the addition of discounts (if any).
  def total_price(self):
    '''
    Method for calculating total shopping and adding discounts
    with the conditions found at Andi's supermarket. 

    Parameters: -
    
    '''

    # Using try and except to make it easier to track errors.
    try:
      # Displays all item in the list.
      n = 0
      print(f'The following are items purchased:')
      print()
      print(f'| No | Item Name               | Quantity | Price     | Total Price     |')
      for item in self.item_list:
        print(f'| {n+1}  | {self.name[n].ljust(23)} | {str(self.quantity[n]).ljust(8)} | {str(self.price[n]).ljust(9)} | {str(self.quantity[n]*self.price[n]).ljust(15)} |')
        n += 1
      print()

      # Get the total price and discount.
      # Sum the price of every items on the list.
      n = 0
      for item_price in self.item_list:
        self.grand_total_price += self.quantity[n]*self.price[n]
        n += 1
      print(f'Total : {self.grand_total_price}')

      # Discount conditions.
      if 300_000 >= self.grand_total_price > 200_000:
          self.grand_total_price -= self.grand_total_price * 0.05
          print('Discount : 5%')
      elif 500_000 >= grand_total_price > 300_000:
          grand_total_price -= grand_total_price * 0.08
          print('Discount : 8%')
      elif self.grand_total_price > 500_000:
          self.grand_total_price -= self.grand_total_price * 0.1
          print('Discount : 10%')
      else:
        pass
      print(f'The total amount to be paid is: Rp {self.grand_total_price}')
      
    # Again, if there is an input error, it will be notified.
    except:
      print('There is a data input error')
      print()
      print(self.item_list)
      print()
      print('Check your shopping list again')

# 9. Create a method to check out the shopping list.
  def check_out(self):
    '''
    Method for checking out the shopping list
    to display the receipt.

    Parameters: -
    
    '''
    # Check one by one the quantity of each item, whether the data type is integer or not.
    check_wrong_input = []
    for qty in self.quantity:
      if type(qty) == int:
        check_wrong_input.append(1)
      else:
        check_wrong_input.append(0)

    # Check one by one the price of each item, whether the data type is integer or not. 
    for prc in self.price:
      if type(prc) == int:
        check_wrong_input.append(1)
      else:
        check_wrong_input.append(0)

    # Displays the receipt if there are no input errors confirmed.
    if all(check_wrong_input): 
      customer_name = str(input('Your Name:')) # input your name to be displayed on the receipt.
      
      # Get today's date with predefined format
      now = datetime.now()
      date = now.strftime('%B %d, %Y %H:%M:%S')

      str_price = 'Rp '+ str(self.grand_total_price) # Change the data type to a string so that it can use the ljust() method.

      print(f'------------------------------------------------------------------------')
      print(f"                      Welcome to Andi's Supermarket                     ")
      print(f'------------------------------------------------------------------------')
      print(f'Name : {customer_name}')
      print(f'Date : {date}')
      print(f'------------------------------------------------------------------------')
      print(f'| No | Item Name               | Quantity | Price     | Total Price     |')
      print(f'|----|-------------------------|----------|-----------|-----------------|')
      n = 0
      for item in self.item_list:
        print(f'| {n+1}  | {self.name[n].ljust(23)} | {str(self.quantity[n]).ljust(8)} | {str(self.price[n]).ljust(9)} | {str(self.quantity[n]*self.price[n]).ljust(15)} |')
        n += 1
      print(f'------------------------------------------------------------------------')
      print(f'The total amount to be paid is : {str_price.rjust(33)}')
      print(f'------------------------------------------------------------------------')
      print(f"                        Thank You for Visiting!                         ")
      print(f'------------------------------------------------------------------------')
    
    # if there is an input error, it will be notified.
    else:
      print('There is a data input error')
      print()
      print(self.item_list)
      print()
      print('Check your shopping list again')