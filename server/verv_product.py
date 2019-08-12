from datetime import datetime


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
PRODUCT_ID = {
    "123": {
        "_id": "123",
        "prodname": "verv smartmeter v1",
        "category": "Electric Meter",
        "quantity": 101
    },
    "124": {
        "_id": "124",
        "prodname": "verv smartmeter v2",
        "category": "Electric Meter",
        "quantity": 11
    },
    "125": {
        "_id": "125",
        "prodname": "verv smartsensor v1",
        "category": "IoT Sensor",
        "quantity": 101
    },
    "126": {
        "_id": "126",
        "prodname": "verv smartsensor v2",
        "category": "IoT Sensor",
        "quantity": 1
    },
    "127": {
        "_id": "127",
        "prodname": "verv smartsolar v1",
        "category": "Solar Panel",
        "quantity": 109
    },
    "128": {
        "_id": "128",
        "prodname": "verv smartsolar v2",
        "category": "Solar Panel",
        "quantity": 10000
    },
    "129": {
        "_id": "129",
        "prodname": "verv smartsolar v3",
        "category": "Solar Panel",
        "quantity": 1000
    }
}


# Create a handler for our read (GET) people
def read(prod_id):
    """
    This function responds to a request for /v1.0/getproduct?prod_id=123
    and returns a product conforming to the JSON Object definition:

    product{
        {_id: {type: string}
        {prodname: {type: string}
        {catagory: {type: string}
        {quantity: {type: number}
    }

    :return:        product
    """
    print("The GET request provided a Product ID of: {}".format(prod_id))
    # Create the list of people from our data

    try:
        product = PRODUCT_ID[prod_id]
        print("Got Product: {}".format(product))
    except KeyError as e:
        print('Error value is: {}'.format(e))
        print('No such product! For product ID: {}'.format(prod_id))
        return "No product with product ID: {}".format(prod_id)

    return product
