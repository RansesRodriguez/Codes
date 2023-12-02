from shipping import get_distance, format_price, SHIPPING_PRICES

from test import test_function

def calculate_shipping_cost(from_coords, to_coords, shipping_type= 'Overnight'):
    from_lat, from_long = from_coords
    to_lat, to_long = to_coords
    distance = get_distance(from_lat, from_long, to_lat, to_long)
    shipping_rate = SHIPPING_PRICES[shipping_type]
    price = distance * shipping_rate
    return format_price(price)

test_function(calculate_shipping_cost)

#Create a function to find the best driver for the job
def calculate_driver_cost(distance, *drives):
    cheapest_driver = None
    cheapest_driver_price = None
    for driver in drives:
        driver_time = distance / driver.speed
        price_for_driver = driver.salary * driver_time
        if cheapest_driver is None:
            cheapest_driver = driver
            cheapest_driver_price = price_for_driver
        elif price_for_driver < cheapest_driver_price:
            cheapest_driver = driver
            cheapest_driver_price = price_for_driver
    return cheapest_driver, cheapest_driver_price

#Create a function to calculate all the money we can save!
def calculate_money_made(**trips):
    total_money_made = 0
    for trip_id, trip in trips.items():
        total_revenue = trip.cost - trip.driver.cost
        total_money_made += total_revenue
    return total_money_made

test_function(calculate_money_made)