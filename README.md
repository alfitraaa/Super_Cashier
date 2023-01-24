# Python Project: Self-Service Super Cashier
## Background
Self-Service Super Cashier is a cashier program that can be run by the customers themself. This program will help Andi as an owner of one of the major supermarkets in Indonesia to develop his business processes with several features such as: customers can directly enter the items purchased, the number of items purchased, the price of the items and so on. So that customers who are not in the city can buy from the supermarket.

## Features Requirement
Some of the requirements that Andi needs for the program are as the follows:
- Customer creates a transaction ID.
- Enters the name of the item, the number of items, and the price of the item.
- Updates the order if there is a mistake in the name, quantity  or price of the item.
- Customer can deletes any of their shopping list or all of them if they cancel the purchase. 
- Checks their shopping list to make sure there is no error.
- Customer can checks the total price of their purchases along with additional discounts with conditions:
    a. If the total price is above Rp200.000, then get 5% discount.
    b. If the total price is above Rp300.000, then get 8% discount.
    c. If the total price is above Rp500.000, then get 10% discount.
Along with several other features that can be added if there are still features that have not been covered in the system.

## Program Flow
How is the process flow of this Super Cashier program?
1. First, customer creates a transaction ID.
2. The customerm the inputs the name, quantity, and price of the items.
3. If there is an error, the customer can update or delete the item for their shopping list.
4. Once the shopping is done, customers can check the list of items to make sure there are no remaining errors. 
5. Then determine the final price that must be paid.
6. The customer can reset the shopping list if they decide not to complete the transaction.
7. Once the customer is informed about the total price of their items, they can finally proceed to check out.
The flowchart is shown in the following picture:

<p align="center">
    <img src="https://github.com/alfitraaa/Super_Cashier/blob/main/super_cashier_flowchart.png?raw=true" width="540" height="960">
</p>

## Test Case and Outputs
### Test Case 1:
1. Customer adds 2 new items to the shopping list using the add_item() method.

![App Screenshot](https://github.com/alfitraaa/Super_Cashier/blob/main/test_case_images/test_case(1).png?raw=true)

2. It turns out that the customer incorrectly entered one of the items that have been added, then the customer uses the delete_item() method to delete the item.

3. The customer want to repeat from the beginning, instead of deleting one by one, the customer can simply use the reset_transaction() method to delete all items that have been added.

![App Screenshot](https://github.com/alfitraaa/Super_Cashier/blob/main/test_case_images/test_case(2,%203).png?raw=true)

4. When done shopping, the consumer can review the list of items and use the total_price() method to get the total amount paid.

![App Screenshot](https://github.com/alfitraaa/Super_Cashier/blob/main/test_case_images/test_case(4).png?raw=true)

### Test Case 2:
Customer_2 decides to purchase toiletries and entered many things into the item list.
1. Because of the rush, it was found that there were several errors in the input of the name, quantity and price of the items. Customer_2 can update the item using update method.

![App Screenshot](https://github.com/alfitraaa/Super_Cashier/blob/main/test_case_images/test_case(5).png?raw=true)

2. Then customer_2 checked again using the check_order() method, apparently found an error. Customer_2 incorrectly inputs the quantity of the items that should be an integer into a string. Then customer_2 deleted it.

![App Screenshot](https://github.com/alfitraaa/Super_Cashier/blob/main/test_case_images/test_case(6).png?raw=true)

3. After checking and knowing the total price that customer_2 must to pay, customer_2 finally checks out the item list using check_out() method and gets the shopping receipt.

![App Screenshot](https://github.com/alfitraaa/Super_Cashier/blob/main/test_case_images/test_case(7).png?raw=true)

## Conclusion
Andi now has a program that can help his business processes become more independent, with several features from the Super Cashier program that allows customers to make their own transactions at Andi's Supermarket, no matter if the customers are in different places. These features are:
- The customer can enter the name, quantity and price from the item taken to the shopping list.
- The customer can also update and delete the items if it turns out that there is an input errors.
- Then the customer can check to make sure the items on the shopping list have no more errors.
- Finally the customer can find out the total price to be paid with discount if it meets the conditions.

### Future Work
This Super Cashier program still needs many details to be improved, new features to be included, and also surely there will be some improvements found after the program is run by several users due to the limited knowledge and time available. If later possible, I'd like to add more dynamic features to the Super Cashier program, such as entering the menu in the Andi's Supermarket so that customers can pick what they want without having to type the item's name again and also preventing customer input errors, creating a database of customers who have made purchase at Andi's supermarket, and so on.

If there are any ideas or feedback from the projects I have worked on, I would be very appreciate. Furthermore, I'm available for work or collaboration; you can reach me at farizalfitraaa@gmail.com.
Thank You.
