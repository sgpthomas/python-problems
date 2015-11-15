from random import randint
import time
import math

coffee_sym = "."
cream_sym = "X"

def gen_cup (rows, cols):
    container = []
    cream = rows*0.5 #fill the top half of the container with cream
    for y in range (rows): #loop through all rows
        container.append ([])
        for x in range (cols): #loop through all columns
            #if y is less than cream, insert true
            if y < cream:
                container[y].append (True)
            else: #else if y is greater than cream, insert space
                container[y].append (False)

    return container

def gen_homo_cup (rows, cols):
    option1 = []
    option2 = []
    for y in range (rows): #loop through all rows
        option1.append ([])
        for x in range (cols): #loop through all columns
            #if y is less than cream, insert true
            if (x % 2) == (y % 2):
                option1[y].append (True)
            else: #else if y is greater than cream, insert space
                option1[y].append (False)

    for y in range (rows): #loop through all rows
        option2.append ([])
        for x in range (cols): #loop through all columns
            #if y is less than cream, insert true
            if (x % 2) != (y % 2):
                option2[y].append (True)
            else: #else if y is greater than cream, insert space
                option2[y].append (False)

    container = []
    container.append (option1);
    container.append (option2)
    return container

#optimize this later
def random_swap (c):

    x = randint (1, len (c[0]) - 2)
    y = randint (1, len (c) - 2)
    s = randint (0, 7)
    #while (should_swap (x, y, s, c) != True):
    #    x = randint (1, len (c[0]) - 2)
    #    y = randint (1, len (c) - 2)
    #    s = randint (0, 7)

    """
    /       \
    | 0 1 2 |
    | 3 x 4 |
    | 5 6 7 |
    |=======|
    """
    shiftx = 0
    shifty = 0
    #set y shift
    if s < 3:
        shifty = -1
    elif s > 4:
        shifty = 1

    #set x shift
    if s in [0,3,5]:
        shiftx = -1
    elif s in [2,4,7]:
        shiftx = 1

    c[y][x], c[y+shifty][x-shiftx] = c[y+shifty][x-shiftx], c[y][x]

    return c

def should_swap (x, y, s, c):
    shiftx = 0
    shifty = 0
    #set y shift
    if s < 3:
        shifty = -1
    elif s > 4:
        shifty = 1

    #set x shift
    if s in [0,3,5]:
        shiftx = -1
    elif s in [2,4,7]:
        shiftx = 1

    if (c[y][x] != c[y+shifty][x+shiftx]):
        return True
    return False


def print_container (cont):
    #print top line
    print "/",
    for a in range (len (cont[0])):
        print " ",
    print "\\"

    #loop through rest of array
    for row in cont: #loop through rows
        print "|",
        for col in row: #loop through columns
            if col:
                print cream_sym,
            else:
                print coffee_sym,
        print "|"

    #print bottom
    print "|",
    for a in range (len (cont[0])):
        print "=",
    print "|"


def main ():
    print ("Running Simulation\n"),
    start = time.time ()

    container = gen_cup (12, 20)
    perfect1, perfect2 = gen_homo_cup (20, 20)
    itera = 0
    last_time = -1
    while (time.time () - start < 120):
        container = random_swap (container)
        itera += 1
        current_time = math.floor (time.time () - start)
        if (current_time != last_time):
            print (str (itera) + " iterations in " + str (current_time) + " seconds")
            last_time = current_time

        if (container == perfect1 or container == perfect2):
            print ("\nMatched!")
            break

        #print_container (container);
    print_container (container)
    print ("Finished " + str (itera) + " iterations in " + str (time.time () - start) + "\n")
    print ("Have a nice day?")

if __name__ == '__main__':
    main ()
