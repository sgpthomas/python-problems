import math
import time
#import matplotlib.pyplot as plt
#import numpy as np

#entropy function
def shannon_entropy (timeseries, n=5):
    combos = []
    total = float (len (timeseries)-(n-1))
    #loop through timeseries
    for lag in range (0, int (total)):
        combos.append (sort (timeseries [0+lag:n+lag]))

    times = count_occurences (combos)

    entropy = 0
    for combo in times:
        s = combo[1] / total
        s *= math.log (s)
        s /= math.log (total)
        entropy += s

    return entropy * -1

def count_occurences (arr):
    ret_arr = []
    while (len (arr) > 0):
        combo = arr.pop ()
        count = 1
        while (combo in arr):
            arr.remove (combo);
            count += 1

        ret_arr.append ((combo, count))
        #print (combo, count)

    return ret_arr



def sort (bucket):
    ret_arr = []
    comp_val = None
    curr_index = 1

    for i in range (len (bucket)):
        if (len (ret_arr) < 1):
            ret_arr.append (i)
            comp_val = bucket[i]
        else:
            curr_index = len (ret_arr)
            while (bucket[i] > comp_val):
                curr_index -= 1
                comp_val = bucket[curr_index-1]

            ret_arr.insert (curr_index, i)
            comp_val = bucket[i]

    #print (bucket, ret_arr)
    return ret_arr


def test ():
    x = [0.01]
    for i in range (60):
        v = 3.95 * x[i] * (1 - x[i])
        x.append (v)

    n = 5
    print ("n:" + str (n) + " Entropy:" + str (shannon_entropy (x, n)))
    #plt.plot (x)
    #plt.plot (x2)
    #plt.grid ()
    #plt.show ()

def test_sort ():
    a = [-1.534512345, 1.6453412, 34125.1235, -541.5435, 0.5413]
    start = time.time ()
    print (sort (a))
    print (time.time () - start)

if __name__ == '__main__':
    #test_sort ()
    test ()
