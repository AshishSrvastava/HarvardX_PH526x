#importing alphabet
import string
alphabet=string.ascii_letters

print('\nExercise 1b')
#declaring the count_letters function to check how many occurences of each letter there are
sentence = 'Jim quickly realized that the beautiful gowns are expensive'
count_letters = {}
for letter in sentence:
    if letter in alphabet:
        if letter in count_letters.keys():
            count_letters[letter] += 1
        else:
            count_letters[letter] = 1
#returning the 3rd and 8th values of the dictionary
print(list(count_letters.values())[2])
print(list(count_letters.values())[7])

print('\nExercise 1c')
#making a function called counter that takes the string 'input_string' and returns a dictionary
#of letter counts called 'count_letters', then using that function to return counter(sentence)
def counter(input_string):
    count_letters = {}
    for letter in input_string:
        if letter in alphabet:
            if letter in count_letters:
                count_letters[letter] += 1
            else:
                count_letters[letter] = 1
    return count_letters
print(counter(sentence))

print('\nExercise 1d')
#given the Gettysburg Address as input, count the number of occurences of each letter
#and save it as 'address_count'
address = """Four score and seven years ago our fathers brought forth on this continent, a new nation, 
conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a 
great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. 
We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final 
resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper 
that we should do this. But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- 
this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add 
or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. 
It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so 
nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored 
dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here 
highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of 
freedom -- and that government of the people, by the people, for the people, shall not perish from the earth."""   
#saving address_count, and returning the number of occurences of 'h'
address_count = counter(address)
print(address_count['h'])

print('\nExercise 1f')
#find most common letter in the gettysburg address
maximum = 0
most_frequent_letter = ""
for letter in address_count:
    if address_count[letter] > maximum:
        maximum = address_count[letter]
        most_frequent_letter = letter
print(most_frequent_letter)


#Exercises 2
import math
print('\nExercise 2a')
#print the value of pi/4
print(math.pi/4)


print('\nExercise 2b')
#Using random.uniform(), create a function rand() that generates a single float between (-1,1)
#Call rand() once. For us to be able to check your solution, 
#we will use random.seed() to fix the seed value of the random number generator.
import random

random.seed(1) # Fixes the see of the random number generator.

def rand():
   # define `rand` here!
    return(random.uniform(-1,1))
rand()


print('\nExercise 2c')
#define a function distance(x,y) which takes two vectors as inputs and returns the distance between them
def distance(x, y):
   # define your function here!
    if len(x) != len(y):
        return "x and y do not have the same length!"
    else:
        dist = math.sqrt((y[0]-x[0])**2+(y[1]-x[1])**2)
        return dist
distance((0,0),(1,1))


print('\nExercise 2d')
#write a function in_circle(x, origin) that determines whether a point in a 2D plane
#falls within a unit circle at a given origin. use the distance function
def in_circle(x, origin = [0,0]):
    #error case: x needs to have only two values
    if len(x) !=2:
        return 'x is not two-dimensional!'
    #if the distance to the origin is less than one, the point is inside the unit circle
    #and True should be returned
    elif distance(x, origin) < 1:
        return True
    else:
        return False    
x = (1,1)
print(in_circle(x))


print('\nExercise 2e')
#creates a list of R=10000 bool values called 'inside' which determines whether a random point falls 
#inside a unit circle centered at the origin. (Using rand and the in_circle functions)
#To calculate pi/4, (ratio of points inside circle to outside circle) calculate the proportion of points
#that fall inside the circle by summing all True values in the inside list; then divide by R 

#done to lock answer to a certain random answer
random.seed(1) 
#Creates R: The number of Booleans to create
R=10000
#creates inside: the list of all the boolean test values of whether the point is inside the circle or not. Currently empty
inside = []
#loops through range(R) to make R boolean values of whether the point is inside or not
for i in range(R):
    #using the rand() function defined earlier to give a float between -1 and 1 for the x and y coordinates
    point=[rand(), rand()]
    #adding the boolean value of whether the point is inside the circle to the list
    inside.append(in_circle(point))
approximation = sum(inside)/R
print("the approximation for pi/4 is " + str(approximation))


print('\nExercise 2f')
#finding the error between the actual value of pi/4 and the approximation made in 2f
error = (math.pi/4)-(sum(inside)/R)
print("the error in the approximation is " + str(error))
