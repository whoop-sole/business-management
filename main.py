# main.py

from inventory import Inventory
from sales import Sales
from customer import Customer
from supplier import Supplier
from reports import generate_report

def main():
    inventory_system = Inventory()
    sales_system = Sales()
    customer_system = Customer()
    supplier_system = Supplier()

    # Your business logic here

    generate_report()

if __name__ == "__main__":
    main()
