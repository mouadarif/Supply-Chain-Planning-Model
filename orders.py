import csv
from datetime import datetime

class Order:
    def __init__(self, order_id, products, quantities, loading_date, customer_details):
        self.order_id = order_id
        self.products = products
        self.quantities = quantities
        self.loading_date = loading_date
        self.customer_details = customer_details
        self.status = "Placed"  # Initial status
        self.packing_lists = {}  # Dictionary to store packing lists per product

    @classmethod
    def from_csv(cls, csv_file):
        orders = {}
        products = {}
        
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file, delimiter='\t')
            next(csv_reader)  # Skip header
            for row in csv_reader:
                order_id = row[0]
                product_id = row[1]
                quantity = int(row[2])
                loading_date = datetime.strptime(row[3], '%d/%m/%y')
                customer_details = {
                    'Name': row[4],
                    'Other_Details': row[5]
                }
                
                if order_id not in orders:
                    orders[order_id] = {
                        'order_id': order_id,
                        'products': [product_id],
                        'quantities': [quantity],
                        'loading_date': loading_date,
                        'customer_details': customer_details
                    }
                else:
                    orders[order_id]['products'].append(product_id)
                    orders[order_id]['quantities'].append(quantity)
                
                if product_id not in products:
                    # Add product to products dictionary if it doesn't exist
                    # Assuming you read product details from another CSV or data source
                    # product_data = read_product_data_from_csv(product_id)
                    # products[product_id] = Product(**product_data)
                    products[product_id] = Product(product_id, description='NEW', 		quality_release_duration=4,production_conversion_rate=3.8, product_type='REGULAR')
        
        order_objs = []
        for order_data in orders.values():
            product_objs = [products[prod_id] for prod_id in order_data['products']]
            order_objs.append(cls(order_data['order_id'], product_objs, order_data['quantities'],
                                  order_data['loading_date'], order_data['customer_details']))
        
        return order_objs

