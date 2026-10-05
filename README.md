# Self-Service Super Cashier

**Self-Service Super Cashier** is a Python-based self-service cashier simulation built around a `Transaction` class. It allows customers to independently input their purchases, calculate total costs, and generate a receipt. This repository serves as an educational portfolio project demonstrating foundational Python programming concepts and basic business-rule implementation.

## Problem / Objective

The objective of this project is to streamline the checkout process for Andi, a supermarket owner. By allowing customers to self-serve and manage their own shopping carts, the program reduces the need for manual cashier intervention. This helps facilitate a smoother purchasing process for customers who wish to record their items and checkout independently.

## Key Features

- **Add Items**: Customers can add items by specifying the name, quantity, and price.
- **Update Items**: Customers can correct mistakes by updating an item's name, quantity, or price.
- **Delete Items**: Customers can remove individual items or reset the entire transaction.
- **Input Validation**: The system checks and detects invalid quantity or price types during order validation (e.g., when calling methods like `check_order` or `check_out`). It does not prevent invalid inputs from being added initially.
- **Discount Calculation**: The project outlines business rules for applying tiered discounts based on the total purchase amount:
  - 5% discount for totals above Rp200,000.
  - 8% discount for totals above Rp300,000 (Note: there is a known limitation in the implementation of this tier).
  - 10% discount for totals above Rp500,000.
- **Checkout / Receipt Generation**: Displays a final list of purchased items, total price, and applied discounts in a structured receipt format.

## How It Works

1. The customer creates a transaction.
2. The customer inputs the name, quantity, and price of the items.
3. If there is an error, the customer can update or delete the item from their shopping list.
4. The customer checks the order to ensure there are no input errors.
5. The final price and applicable discounts are calculated.
6. The customer proceeds to checkout, generating a text-based receipt.

<p align="center">
    <img src="https://github.com/alfitraaa/Super_Cashier/blob/main/super_cashier_flowchart.png?raw=true" width="540" height="960" alt="Super Cashier Flowchart">
</p>

## Technical Implementation

This project is built purely in Python and demonstrates the following technical skills:

- **Object-Oriented Programming (OOP)**: Core logic is encapsulated within a `Transaction` class.
- **Transaction-State Handling**: Uses a dictionary to store and manage the current state of items in the cart.
- **Item Management Operations**: Implements methods to Create, Read, Update, and Delete items from the shopping list.
- **Validation Logic**: Basic type checking checks if quantities and prices are integers during order validation.
- **Conditional Discount Logic**: Contains tiered discount business rules based on spending thresholds; the current 8% tier has a known implementation defect.
- **Receipt/Output Generation**: Utilizes f-strings and the `datetime` module to format terminal output into a readable receipt.

## Example / Test Scenarios

The project includes manual test scenarios (available in the Jupyter Notebook) to verify core functionalities.

### Scenario 1: Adding, Deleting, and Checking Out
1. Adding items to the shopping list:
![App Screenshot](https://github.com/alfitraaa/Super_Cashier/blob/main/test_case_images/test_case(1).png?raw=true)

2. Resetting the transaction to start over:
![App Screenshot](https://github.com/alfitraaa/Super_Cashier/blob/main/test_case_images/test_case(2,%203).png?raw=true)

3. Reviewing the order and calculating the final price:
![App Screenshot](https://github.com/alfitraaa/Super_Cashier/blob/main/test_case_images/test_case(4).png?raw=true)

### Scenario 2: Updating Items and Error Handling
1. Updating an incorrect item input (name, quantity, or price):
![App Screenshot](https://github.com/alfitraaa/Super_Cashier/blob/main/test_case_images/test_case(5).png?raw=true)

2. Detecting validation errors (e.g., inputting a string instead of an integer for quantity):
![App Screenshot](https://github.com/alfitraaa/Super_Cashier/blob/main/test_case_images/test_case(6).png?raw=true)

3. Checking out and generating the final receipt:
![App Screenshot](https://github.com/alfitraaa/Super_Cashier/blob/main/test_case_images/test_case(7).png?raw=true)

## Repository Structure

- `super_cashier.py`: Contains the main `Transaction` class and application logic.
- `test_case.ipynb`: A Jupyter Notebook containing manual test scenarios and demonstrations of the class methods.
- `super_cashier_flowchart.png`: Visual flowchart of the application's process.
- `test_case_images/`: Directory containing screenshots used in the documentation.
- `README.md`: Project documentation.

## Current Limitations / Future Improvements

As a legacy portfolio project, the current implementation has several limitations that could be addressed in future iterations:
- **In-Memory Storage**: Data is only stored in memory during the active session. There is no database integration for long-term persistence or historical records.
- **No Executable CLI**: The project is designed to be interacted with via the Python interactive interpreter or a Jupyter Notebook; it lacks a standalone executable terminal application entry point.
- **Terminal-Based Interface**: There is no graphical user interface (GUI) or web front-end; interaction is strictly via command-line / code execution.
- **Manual Testing**: Testing relies on manual execution of scenarios within the provided notebook. There is no automated test suite.
- **Hardcoded Product Entry**: Customers must manually type the item name, price, and quantity. A predefined catalog or inventory system would prevent data entry errors.
- **Discount Implementation Defect**: The source code contains a defect in the 8% discount branch within the `total_price` method, referencing an incorrect variable scope.

## Running the Project

To run this project locally, ensure you have Python installed, then clone the repository:

1. Clone the repository:
   ```bash
   git clone https://github.com/alfitraaa/Super_Cashier.git
   cd Super_Cashier
   ```

2. Open and explore `test_case.ipynb`. This Jupyter Notebook serves as the canonical example of the supported execution flow and demonstrates how to initialize and use the `Transaction` class found in `super_cashier.py`.

## Author / Contact

This project was developed by Fariz Alfitra.

If you have any ideas, feedback, or would like to discuss collaboration opportunities, you can reach me at farizalfitraaa@gmail.com.
