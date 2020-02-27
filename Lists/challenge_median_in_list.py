import math

"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

#Jordan
sorted_list = sorted(sale_prices)
num_of_sales = len(sorted_list) #9

half_slice = math.floor(num_of_sales/2)
print(half_slice)

first_sales_items = sorted_list[:half_slice]
last_sales_items = sorted_list[-(half_slice):]

median = sorted_list[half_slice:(half_slice + 1)]

print(sorted_list)
print(num_of_sales)
print(first_sales_items)
print(last_sales_items)
print(median)


#Ryan example
def find_median_odd(num_list):
  sorted_list = sorted(num_list)
  list_len_mid = len(num_list)/2

  return sorted_list[math.floor(list_len_mid)]

print(find_median_odd(sale_prices))