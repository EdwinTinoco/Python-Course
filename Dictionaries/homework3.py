# Create a dictionary called 'filter_genre'. 'filter_genre' should have 3 keys: action, romance and comedy. 
# Each genre will have 2 channels (also dictionaries). Each channel will have a LIST of 2 tv shows.

###
# filter_genre 
#   action
#     HBO - "The Pacific", "Watchmen"
#     TNT - "Top Gun", "Terminator"
#   romance
#     ABC - "The Bachelorette", "Once Upon a Time"
#     CBS - "Mom", "I love Lucy"
#   comedy
#     Fox - "How I Met Your Mother", "New Girl"
#     Disney Channel - "That's so Raven", "Mickey's Playhouse"

# Write a line of code that prints all of the genres.
# Write a line of code that prints all of the channels inside of the comedy genre
# Write a line of code that prints the cannels and tv shows inside of the romance genre
# Write a line of code that prints the second tv show inside of HBO

# Dictionary
filter_genre = {
    "action": {
        "HBO": ["The Pacific", "Watchmen"],
        "TNT": ["Top Gun", "Terminator"]
    },
    "romance": {
        "ABC": ["The Bachelorette", "Once Upon a Time"],
        "CBS": ["Mom", "I love Lucy"]
    },
    "comedy": {
        "Fox": ["How I Met Your Mother", "New Girl"],
        "Disney Channel": ["That's so Raven", "Mickey's Playhouse"]
    }
}

# Write a line of code that prints all of the genres.
print(list(filter_genre.keys()))

# Write a line of code that prints all of the channels inside of the comedy genre
print(list(filter_genre.get('comedy', 'channel not found')))

# Write a line of code that prints the cannels and tv shows inside of the romance genre
print(list(list(list(filter_genre.items())[1]))[1])
print(filter_genre["romance"])

# Write a line of code that prints the second tv show inside of HBO
print(filter_genre["action"]["HBO"][1])

