class Product:
    def __init__(self, product_id, description, quality_release_duration, production_conversion_rate, net_weight,product_type):
    	# whatever is the identification of each product that the company uses and that's unique to the product 
        self.product_id = product_id
        # this is a description of the product
        self.description = description
        # this attribute is particularly useful 
        self.quality_release_duration = quality_release_duration
        # this attribute is particularly important for shipment and production planning, since no product can be shipped before the approval for quality 
        self.production_conversion_rate = production_conversion_rate
        # this will be useful since the net weight define the the processing rate in the line
        self.net_weight=net_weight
        # this product type mainly specify wether it's a finished product or copacked made of semi-finished products, if it's copacked there's a set of products that needs to be produced initially based on a copacking BOM 
        self.copacked = False
        # RBOM : it sets  the products that share the same  Bill Of Materials and major ingredients (raw BOM) , hence, they can be produced on the same production line, without significant changeover time.
        #  
        self.RBOM=RBOM
	# this is a dictionnary to store the quantity per batch for the product, this information is important for quality release and shipment planning, we want to ship always the old batches first 
        self.batches = {}  

    def add_batch(self, batch_id, quantity):
        # Add a new batch with its associated quantity
        if batch_id not in self.batches:
            self.batches[batch_id] = quantity
        else:
            # If batch_id already exists, update the quantity
            self.batches[batch_id] += quantity

    def update_stock(self, batch_id, quantity):
        # Update the stock quantity for a specific batch
        if batch_id in self.batches:
            self.batches[batch_id] += quantity
        else:
            self.batches[batch_id] = quantity

    def get_details(self):
        # Return product details including batches and their quantities
        details = {
            'Product ID': self.product_id,
            'Description': self.description,
            'Quality Release Duration': self.quality_release_duration,
            'Production Conversion Rate': self.production_conversion_rate,
            'Product Type': self.product_type,
            'Batches': self.batches
        }
        return details

# Additional methods relevant to product management can be added here

