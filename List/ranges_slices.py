tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
  'computer science'
]

tag_range = tags[:-1:2] #pasa uno si uno no

tag_range = tags[::-1] #pasa el ultimo elemento y asi sucecivamente

print(tag_range)  ['computer science', 'programming', 'code', 'tutorials', 'development', 'python']

tags.sort(reverse=True)

print(tags)