# SI 206 HW4
# Your name:
# Your student id:
# Your email:
# Who you worked with on this homework:

import unittest


class Customer:
    def __init__(self, name, employeer_id=None, account=15):
        '''initializes the name, employeer_id, and the amount of money in the customer's account'''
        self.name = name
        self.employeer_id = employeer_id
        self.account = account

    def __str__(self):
        '''returns the customer's name and the amount in their account as a string.'''
        return f'My name is {self.name}, and I have ${self.account} in my account'

    def deposit_money(self, amount):
        '''adds the passed amount to the customer's account'''
        self.account += amount

    def place_item_order(self, store, order):
        ''' 
        This takes a store object and an 'order', which is a dictionary where the keys are Item objects
        and the values are another dictionary with keys of quantity and express_order.

        It returns a boolean value (True or False) that indicates if the order was successfully placed or not.
        '''

        pass


class Item:

    def __init__(self, name, cost):
        ''' initializes the name and cost'''
        self.name = name
        self.cost = cost

    def __str__(self):
        ''' returns the name and cost of the item as a string'''
        return self.name + " costs $" + str(self.cost)


class Store:

    def __init__(self, name, store_id, income=0):
        ''' 
        initializes the name and income of the store
        sets the inventory to an empty dictionary
        '''
        self.name = name
        self.store_id = store_id
        self.income = income
        self.inventory = {}

    def __str__(self):
        '''returns the name of the store and their inventory'''
        print(
            f"Hello we are {self.name}. This is the current inventory {self.inventory.keys()}")

    def accept_payment(self, amount):
        '''adds the passed amount to the stores income'''
        self.income += amount

    def calculate_item_cost(self, item, quantity, express_order, customer):
        '''
        takes the item object, quantity, and a boolean variable express_order, 
        which specifics whether the order is an express order. 
        If an express order is requested, it adds a 20% upcharge.

        EXTRA CREDIT: If the customer works at the store, then they receive a 40% discount
        on the item. They also still pay the 20% upcharge for express orders.
        '''
        pass

    def stock_up(self, item, quantity):
        ''' 
        If the item is already in the inventory then add the passed quantity
        to the existing value.  Otherwise set the value for the item
        in the inventory dictionary.
        '''
        pass

    def process_order(self, order):
        '''
        Checks that there is enough of each item for an order and if not returns False,
        otherwise it subtracts the order items from the quantity in the inventory
        and returns True.
        '''

        pass


class TestAllMethods(unittest.TestCase):

    def setUp(self):
        self.notebook = Item('Notebook', 3.00)
        self.loose_leaf_paper = Item('Loose Leaf Paper', 1.75)
        self.pen_package = Item('Pen Package', 1.50)
        self.pencil_package = Item('Pencil Package', 0.75)

        self.charlies_office_supplies = Store(
            name="Charlie's Office Supplies", store_id=1)
        self.super_office_supplies = Store(
            name="Super Office Supplies", store_id=2)

        self.bob = Customer(name='Bob', employeer_id=None)
        self.alice = Customer(name='Alice', employeer_id=17, account=12.50)
        self.charlie = Customer(name='Charlie', employeer_id=1, account=20)

    # Check the constructors
    def test_customer_constructor(self):
        self.assertEqual(self.bob.name, 'Bob')
        self.assertEqual(self.bob.account, 15)

    def test_item_constructor(self):
        self.assertEqual(self.pen_package.name, 'Pen Package')
        self.assertAlmostEqual(self.pen_package.cost, 1.50, 1)
        self.assertEqual(self.pencil_package.name, 'Pencil Package')
        self.assertAlmostEqual(self.pencil_package.cost, 0.75, 0)

    def test_store_constructor(self):
        self.assertEqual(self.charlies_office_supplies.name,
                         "Charlie's Office Supplies")
        self.assertEqual(self.charlies_office_supplies.income, 0)
        self.assertEqual(self.super_office_supplies.name,
                         "Super Office Supplies")
        self.assertEqual(self.super_office_supplies.inventory, {})

    # Check the deposit_money method for customer
    def test_customer_deposit_money(self):
        self.alice.deposit_money(10)
        self.assertAlmostEqual(self.alice.account, 22.50, 1)

    # Check the calculate_item_cost for store
    def test_store_calculate_item_cost(self):
        self.assertAlmostEqual(self.charlies_office_supplies.calculate_item_cost(
            self.pen_package, 10, False, self.alice), 15.00, 2)

    # Check if discount is applied
        self.assertAlmostEqual(self.super_office_supplies.calculate_item_cost(
            self.notebook, 3, False, self.alice), 9, 2)

    # Check if fresh picks are billed correctly
        self.assertAlmostEqual(self.super_office_supplies.calculate_item_cost(
            self.pencil_package, 3, True, self.alice), 2.70, 2)

    # EXTRA CREDIT: UNCOMMENT THE TEST LINES BELOW: Check if only employees of the store get the employee discount
        # cameron = Customer(name='Cameron', employeer_id=4, account=20)
        # extra_credit_order = {
        #     self.notebook: {
        #         "quantity": 7,
        #         "express_order": True,
        #     }
        # }
        # self.charlies_office_supplies.stock_up(self.notebook, 21)
        # self.assertAlmostEqual(self.charlies_office_supplies.calculate_item_cost(
        #     self.notebook, 7, True, self.charlie), 15.12, 2)
        # self.assertTrue(self.charlie.place_item_order(
        #     self.charlies_office_supplies, extra_credit_order))
        # self.assertFalse(cameron.place_item_order(
        #     self.charlies_office_supplies, extra_credit_order))

    # Check the accept_payment method for store

    def test_store_accept_payment(self):
        self.super_office_supplies.accept_payment(50)
        self.assertAlmostEqual(self.super_office_supplies.income, 50.00, 0)

    # Check the stock_up method for store
    def test_store_stock_up(self):
        self.super_office_supplies.stock_up(self.notebook, 4)
        self.super_office_supplies.stock_up(self.loose_leaf_paper, 10)
        self.assertEqual(self.super_office_supplies.inventory, {
                         self.notebook: 4, self.loose_leaf_paper: 10})

        self.charlies_office_supplies.stock_up(self.pen_package, 5)
        self.charlies_office_supplies.stock_up(self.pencil_package, 3)
        self.assertEqual(self.charlies_office_supplies.inventory, {
                         self.pen_package: 5, self.pencil_package: 3})

    # Check the place_item_order method for customer
    def test_customer_place_item_order(self):
        pam = Customer(name='Pam', employeer_id=19)
        supplies_r_us = Store(name="Supplies R Us", store_id=14)

        supplies_r_us.stock_up(self.pencil_package, 5)
        supplies_r_us.stock_up(self.notebook, 3)

        # Scenario 1: customer doesn't have enough money in their account

        # Scenario 2: store doesn't have enough of an item left in stock

        # Scenario 3: store doesn't sell that item

    def test_customer_place_item_order_2(self):
        ali = Customer(name='Ali', employeer_id=47)
        dunder_mifflin = Store(name="Dunder Mifflin", store_id=19)
        dunder_mifflin.stock_up(self.pen_package, 5)
        dunder_mifflin.stock_up(self.loose_leaf_paper, 10)

        # Fix the test cases below to check if the customer's account and the store's income has
        # the right amount after an order is processed

        self.assertEqual(ali.place_item_order(dunder_mifflin, {
            self.pen_package: {
                "quantity": 2,
                "express_order": False
            },
            self.loose_leaf_paper: {
                "quantity": 4,
                "express_order": True
            }}
        ), False)
        self.assertAlmostEqual(self.ali.account, 1.50, 2)
        self.assertAlmostEqual(ali.income, 8.50, 2)


def main():
    pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
    main()
