import math
import time

#entropy function
def shannon_entropy (timeseries, n=5):
    combos = []
    #total = float (math.factorial (n))
    #loop through timeseries
    for lag in range (0, len (timeseries)-(n)):
        combos.append (sort (timeseries [0+lag:n+lag]))

    times = count_occurences (combos)
    total = float (len (timeseries)-(n))

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
        print (combo, count)

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

    return ret_arr


def test ():
    fun = range (1000);
    for n in range (len (fun)):
        fun[n] = math.sin (n)

    n = 5
    print ("n:" + str (n) + " Entropy:" + str (shannon_entropy (fun, n)))

def test_sort ():
    a = [-1.534512345, 1.6453412, 34125.1235, -541.5435, 0.5413]
    start = time.time ()
    print (sort (a))
    print (time.time () - start)

if __name__ == '__main__':
    #test_sort ()
    test ()
