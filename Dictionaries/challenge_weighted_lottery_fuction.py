# weights_dictionary = {
#     'winning': 2,
#     'break_even': 1,
#     'losing': 5
#  }

# def weighted_lottery(dictionary):
#     result_list = []
#     times_winning = dictionary['winning']
#     even_break = dictionary['break_even']
#     times_losing = dictionary['losing']      

#     for i in range(times_winning):   
#         result_list.append('winning')
#         for _ in range(even_break):
#             result_list.append('break even')
#             for _ in range(times_losing):
#                 result_list.append('losing')
    
#     return result_list  
 
# print(weighted_lottery(weights_dictionary))



# Jordan example
# import numpy as np
# weights = {
#     'winning': 1,
#     'bereak_even': 2,
#     'losing': 3
# }

# other_weights = {
#     'green': 1,
#     'yellow': 2,
#     'red': 3
# }

# def weighted_lottery(weights):
#     container_list = []

#     for (name, weight) in weights.items():
#         for _ in range(weight):
#             container_list.append(name)

#     return np.random.choice(container_list)

# print(weighted_lottery(weights))



# Ryan example
import random
weights = {
    'winning': 1,
    'break_even': 2,
    'losing': 3
}

def weighted_lottery(weights_dictionary):
    container_list = []

    for (name, weight) in weights_dictionary.items():
        for _ in range(weight):
            container_list.append(name)    
    
    return random.choice(container_list)

print(weighted_lottery(weights))
