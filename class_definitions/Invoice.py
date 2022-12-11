"""
Program: Invoice.py
Auther: Katie Freerksen
Last Date Modified: 12/10/2022
This creates an invoice class
"""
class invoice:
    """Invoice Class"""

    #Constructor
    def __init__(self, invID, custID, addy, lname, fname, phone, ip_dict = dict() ):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        phone_number_characters = set("1234567890-()")
        id_characters = set("1234567890")
        if not(name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        if not phone_number_characters.issuperset(phone):
            raise ValueError
        if not id_characters.issuperset(str(custID)):
            raise ValueError
        if not id_characters.issuperset(str(invID)):
            raise ValueError
        self.invoice_id = invID
        self.customer_id = custID
        self.last_name = lname
        self.first_name = fname
        self.phone_number = phone
        self.address = addy
        self.items_with_price = ip_dict

    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname

    def set_address(self, addy):
        self.address = addy

    def set_phone(self, phone):
        self.phone = phone
    def __str__(self):
        return self.invoice_id + ": " + self.customer_id + " | " + self.lname + ", " + self.fname + " | " +\
            self.phone_number + " | " + self.address

    def __repr__(self):
        return 'invoice({},{},{},{},{},{},{}'.format(self.invoice_id,self.customer_id,self.last_name,
                                                    self.first_name,self.phone_number,self.address,
                                                    self.items_with_price)

    def add_item(self, dict):
        self.items_with_price.update(dict)

    def create_invoice(self):
        total = 0
        tax = 0

        for key, value in self.items_with_price.items():
            print(key, '.....', value)
            total += value
        tax = total * 0.06
        total += tax
        print('Tax..........' + "${:.2f}".format(tax))
        print('Total.....' + "${:.2f}".format(total))

# Driver code (you shouldn't have to modify this)
if __name__ == "__main__":
    invoice = invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802' ,'Mouse', 'Minnie', '555-867-5309')
    invoice.add_item({'iPad': 799.99})
    invoice.add_item({'Surface': 999.99})
    invoice.create_invoice()

