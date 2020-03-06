"""
[
    [0, 1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8],
]
"""

def manual_incrementing_matrix(num):
    matrix_list = []
    temp_list = []   

    for i in range(num):                
        for j in range(num):
            temp_list.append(j + i)

        matrix_list.append(temp_list)  
        temp_list = []
    
    return matrix_list


print(manual_incrementing_matrix(5))



#Jordan solution
def manual_incrementing_matrix(n):
    matrix = [ [ None for y in range(n) ] for x in range(n) ]

    counter = 0

    for idx, el in enumerate(matrix):
        for nested_idx, nested_el in enumerate(el):
            matrix[idx][nested_idx] = counter + nested_idx

        counter += 1

    return matrix


print(manual_incrementing_matrix(5))


#Ryan solution
def manual_matrix(grid_area):
    matrix = []
    counter = 0

    while counter < grid_area:
        matrix.append(( [x for x in range(counter, grid_area + counter)] ))
        counter += 1
    
    return matrix
    

print(manual_matrix(5))
       
