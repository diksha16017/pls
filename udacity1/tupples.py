AngkorWat = (13.4125, 103.866667)
print(type(AngkorWat))
#<class 'tuple'>
print("Angkor Wat is at latitude: {}".format(AngkorWat[0]))
#Angkor Wat is at latitude: 13.4125
print("Angkor Wat is at longitude: {}".format(AngkorWat[1]))
#Angkor Wat is at longitude: 103.866667


#Tuples are similar to lists in that they store an ordered collection of objects which can be accessed
#by their indexes (for example AngkorWat[0] and AngkorWat[1]).
#Unlike lists, tuples are immutable.
#You can't add and remove items from tuples, or sort them in place

#Why Tuples?
#Why do we have tuples if they're like lists with less features? ' \
#'Tuples useful when you have two or more values that are so closely related that they will always be used together,' \
# like latitude and longitude coordinates.

#Tuples can be used to assign multiple variables in a compact way:

dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {}x{}x{}".format(length, width, height))
#The dimensions are 52x40x100

#Tuple Immutability
#There's also a place where the tuple's immutability is a perk.
#Unlike lists, tuples can be stored in sets or used as the keys of a dictionary.
#Since these two data structures require immutable keys, lists aren't an option. ' \
#(If you're curious why sets and dicts require immutable keys you can learn by in CS101 Lesson 5. ' \
#In that lesson you build a dict from scratch to learn how they work.) In the example below we create a dictionary, world_heritage_locations that has tuples of the form (latitude, longitude) as the keys and strings denoting the corresponding place names as values.

#world_heritage_locations = {(13.4125, 103.866667): "Angkor Wat",
                            #(25.73333, 32.6): "Ancient Thebes",
                            #(30.330556, 35.4433330): "Petra",
                            #(-13.116667, -72.583333): "Machu Picchu"}

def first_and_last(sequence):
    """returns the first and last elements of a sequence"""
    return sequence[0], sequence[-1]
print(first_and_last(["Spam", "egg", "sausage", "Spam"]))
start, end = first_and_last(["Spam", "egg", "sausage", "Spam"])
print(start)
#Spam
print(end)
#Spam