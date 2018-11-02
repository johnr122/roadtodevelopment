def cost_of_ground_shipping(weight):
  if weight <= 2:
    cost = 20 + 1.5*weight
    return cost
  elif 6 >= weight > 2:
    cost = 20 + 3*weight
    return cost
  elif 10>= weight > 6:
    cost = 20 + 4*weight
    return cost
  elif weight > 10:
    cost = 20 + 4.75*weight
    return cost

cost_of_premium_ground_shipping = 125

def cost_of_drone_shipping(weight):
  if weight <= 2:
    cost = 4.5*weight
    return cost
  elif 6 >= weight > 2:
    cost = 9*weight
    return cost
  elif 10>= weight > 2:
    cost = 12*weight
    return cost
  
  elif weight > 10:
    cost = 14.25*weight
    return cost

def cheapest_shipping(weight):
  x = cost_of_ground_shipping(weight)
  y = cost_of_drone_shipping(weight)
  p = cost_of_premium_ground_shipping
  if x < y and x < p:
    cost = x
    ship = "Ground"
  elif y < x and y < p:
    cost = y
    ship = "Drone"
  else:
    cost = p
    ship = "Premium"
    
  print("The %s Shipping is cheaper for only $%.2f"%(ship, cost))

cheapest_shipping(41.5)
cheapest_shipping(4.8)
  