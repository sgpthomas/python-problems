from random import randint
import time
import math
import sys

coffee_sym = " "
marked_sym = "."
cream_sym = "X"

def gen_cup (rows, cols):
    container = []
    cream = rows*0.5 #fill the top half of the container with cream
    cream_count = 0
    cream_lim = (rows*cols)/2.
    for y in range (rows): #loop through all rows
        container.append ([])
        for x in range (cols): #loop through all columns
            #if y is less than cream, insert true
            if y < cream and cream_count <= cream_lim:
                container[y].append (2)
                cream_count += 1
            else: #else if y is greater than cream, insert space
                container[y].append (0)

    return container

def gen_homo_cup (rows, cols):
    option1 = []
    option2 = []
    coffee_count = 0
    for y in range (rows): #loop through all rows
        option1.append ([])
        for x in range (cols): #loop through all columns
            #if y is less than cream, insert true
            if (x % 2) == (y % 2):
                option1[y].append (True)
                coffee_count += 1
            else: #else if y is greater than cream, insert space
                option1[y].append (False)

    coffee_count = 0

    for y in range (rows): #loop through all rows
        option2.append ([])
        for x in range (cols): #loop through all columns
            #if y is less than cream, insert true
            if (x % 2) != (y % 2):
                option2[y].append (True)
                coffee_count += 1
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

    c = mark_swap (c)
    while (c[y][x] != 1):
        x = randint (1, len (c[0]) - 2)
        y = randint (1, len (c) - 2)
        print c[y][x]
        print ("regenning rand")

    print "finished"

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

#optimization
def mark_swap (con):
    for y in range (len (con)):
        for x in range (len (con[0])):
            xs_arr = [0] #xshift
            ys_arr = [0] #yshift
            val = con[y][x]
            #if (y == 0) or (y == len (con) - 1) or (x == 0) or (x == len (con[0]) - 1):
            if (y != 0): #top edge
                ys_arr.append (-1)

            if (y != len (con) - 1): #bottom edge
                ys_arr.append (1)

            if (x != 0):
                xs_arr.append (-1)

            if (x != len (con[0]) - 1):
                xs_arr.append (1)

            if (val == 2): #if value is 2 (cream)
                for ys in ys_arr:
                    for xs in xs_arr:
                        if (con[y+ys][x+xs] == 0):
                            con[y+ys][x+xs] = 1



    return con


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
            if col == 2:
                print cream_sym,
            elif col == 1:
                print marked_sym,
            else:
                print coffee_sym,
        print "|"

    #print bottom
    print "|",
    for a in range (len (cont[0])):
        print "=",
    print "|"

def main ():
    width = 3
    height = 3
    n = 60

    if (len (sys.argv) > 1):
        width, height, n = int (sys.argv[2]), int (sys.argv[3]), int (sys.argv[4])
        if (sys.argv[1] == 'iter'):
            for_iter (width, height, n)
        elif (sys.argv[1] == 'time'):
            for_time (width, height, n)

    else:
        for_iter (width, height, n)


def for_iter (w, h, n):

    print ("Running Simulation {} times".format (n))
    start = time.time ()

    container = gen_cup (w, h)
    #perfect1, perfect2 = gen_homo_cup (width, height)
    last_time = 0

    for a in range (n):
        container = random_swap (container)

    print_container (container)
    print ("Finished " + str (n) + " iterations in " + str (time.time () - start) + "\n")
    print ("Have a nice day?")

def for_time (w, h, t):
    print ("Running Simulation for {} seconds".format (t))
    start = time.time ()

    container = gen_cup (w, h)
    #perfect1, perfect2 = gen_homo_cup (width, height)
    itera = 0
    last_time = 0
    while (time.time () - start < time_lim):
        container = random_swap (container)
        itera += 1
        current_time = math.floor (time.time () - start)
        if (current_time != last_time):
            print (str (itera) + " iterations in " + str (current_time) + " seconds")
            last_time = current_time

        #if (container == perfect1 or container == perfect2):
        #    print ("\nMatched!")
        #    break

        #print_container (container);


    print_container (container)
    print ("Finished " + str (itera) + " iterations in " + str (time.time () - start) + "\n")
    print ("Have a nice day?")

def test_speed ():
    print "Starting Time Trial"
    current_time = 0
    times = 20

    for n in range (times):
        start = time.time ()
        c = gen_cup (20, 20);
        for a in range (200000):
            container = random_swap (c)

        print ("Trial {} finished in {} seconds".format (n, time.time () - start))
        current_time += time.time () - start

    print "Finished Time Trial"
    print "Test took {} seconds".format (current_time)
    print "Average trial took {} seconds".format (current_time / times)

if __name__ == '__main__':
    #c = gen_cup (20, 20)
    #for a in range (20000):
    #    c = random_swap (c)
    #c = mark_swap (c)
    #print_container (c)
    test_speed ()
