def remove_first_and_last(list_to_clean):
    new_list = []
    list_to_clean.pop()

    for num in range(len(list_to_clean)):
        if num > 0:
            new_list.append(list_to_clean[num])

    return new_list   
    

html = ['<h1>', 'Some content', '</h1>']
print(remove_first_and_last(html))

html_2 = ['', 'another Some content', 'more content', '']
print(remove_first_and_last(html_2))


#Jordan example
def remove_first_and_last(list_to_clean):
  _, *content, _ = list_to_clean
  return content


html = ['<h1>', 'My content', '</h1>']
print(remove_first_and_last(html))

other_content_to_clean = ['', 'My content', 'Something else', '/']
print(remove_first_and_last(other_content_to_clean))


#Ryan example
def first_last(li):
    return li[1:-1]

print(first_last(['<h1>', 'Some content', '</h1>']))