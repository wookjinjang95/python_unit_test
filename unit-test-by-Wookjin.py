from sample_account import Customer
import unittest

#initalize the value for sample.
sample = Customer("Alex")
Customer.set_balance(sample)

#start the test_case.
class MyTest(unittest.TestCase):

    #test the __init__ function, already used the __init__ above.
    def test_init(self):
        #print "testing the __init__ with customer name Alex"
        self.assertEqual(sample.name, "Alex")

    #test the set_balance function.
    def test_set_balance(self):
        Customer.set_balance(sample)
        self.assertEqual(sample.balance, 0.0)

    #test the withdraw function.
    def test_withdraw(self):
        #set the testing initial balance to 10 dollars.
        Customer.set_balance(sample, balance=10.0)

        #draw 5 dollars out of the balance
        Customer.withdraw(sample, 5.0)
        self.assertEqual(sample.balance, 5.0)

        #draw 4.50 dollars out of the balance
        Customer.withdraw(sample, 4.50)
        self.assertEqual(sample.balance, 0.50)

        #try to draw balance over than the previous balance and make sure
        #the error display is correct too.
        with self.assertRaises(Exception) as content:
            Customer.withdraw(sample, 1.00)

        self.assertTrue('Amount greater than available balance.' in content.exception)

    #test the deposit function.
    def test_deposit(self):
        #set the testing initial balance to 10 dollars.
        Customer.set_balance(sample, balance=10.0)
        prev_balance = sample.balance

        #deposits nothing, the balance should stays the same.
        Customer.deposit(sample, 0)
        self.assertEqual(sample.balance, prev_balance)

        #deposit $10.50 and should be equal to 10.50 + previous balance.
        prev_balance = sample.balance
        Customer.deposit(sample, 10.50)
        self.assertEqual(sample.balance, prev_balance + 10.50)

if __name__ == '__main__':
    unittest.main()
