def ground_shipping(weight):
    if weight <= 2:
        cost = (1.5 * weight) + 20
    elif weight <= 6:
        cost = (3.0 * weight) + 20
    elif weight <= 10:
        cost = (4.0 * weight) + 20
    elif weight > 10:
        cost = (4.75 * weight) + 20
    return cost


print(ground_shipping(8.4))

premium_ground_shipping = 125


def drone_shipping(weight):
    if weight <= 2:
        cost = (4.5 * weight)
    elif weight <= 6:
        cost = (9.0 * weight)
    elif weight <= 10:
        cost = (12.0 * weight)
    elif weight > 10:
        cost = (14.25 * weight)
    return cost


def cheapest_shipping(weight):
    if ground_shipping(weight) < (premium_ground_shipping and drone_shipping(weight)):
        print('Ground shipping is the cheapest and the cost is ' + str(ground_shipping(weight)))
    elif premium_ground_shipping < (ground_shipping(weight) and drone_shipping(weight)):
        print('Premium shipping is the cheapest and the cost is ' + str(premium_ground_shipping))
    elif drone_shipping(weight) < (ground_shipping(weight) and premium_ground_shipping):
        print('Drone shipping is the cheapest and the cost is ' + str(drone_shipping(weight)))

