from random import randint
from graphic_sort import CairoArea, Worker
from time import sleep

DELAY = 0.05

def sort(w, array, ca):
    #label
    if len(ca.text) != 3:
        ca.text = []
        ca.text.append("Graphic Sorting")
        ca.text.append("Iterations: 0")
        ca.text.append("Swaps: 0")

    merge_sort(w, array, ca)
    #better_bubblesort(w, array, ca)

def better_bubblesort(w, array, ca):
    #label
    ca.text[0] = "Better Bubble Sorting"

    if 'bubble' not in w.vars: w.vars['bubble'] = len(array)
    l = w.vars['bubble']
    for i in range(1, l):
        w.vars['iterations'] += 1
        sleep(DELAY)
        ca.select(i)
        if array[i] < array[i-1]:
            w.vars['swaps'] += 1
            array[i], array[i-1] = array[i-1], array[i]
        ca.update_array(array)

        ca.text[1] = "Iterations: {}".format(w.vars['iterations'])
        ca.text[2] = "Swaps: {}".format(w.vars['swaps'])

    w.vars['bubble'] = l - 1

def bubblesort(w, array, ca):
    #label
    ca.text[0] = "Bubble Sorting"

    for i in range(1, len(array)):
        w.vars['iterations'] += 1
        sleep(DELAY)
        ca.select(i)
        if array[i] < array[i-1]:
            w.vars['swaps'] += 1
            array[i], array[i-1] = array[i-1], array[i]
        ca.update_array(array)

        ca.text[1] = "Iterations: {}".format(w.vars['iterations'])
        ca.text[2] = "Swaps: {}".format(w.vars['swaps'])

#don't really know how this works. oh well.
def sam_sort(w, array, ca):
    #label
    if len(ca.text) != 3:
        ca.text = []
        ca.text.append("Sam's Sorting")
        ca.text.append("Iterations: 0")
        ca.text.append("Swaps: 0")

    end_index = -1
    for i in range(0, len(array) + end_index):
        w.vars['iterations'] += 1
        sleep(DELAY)
        ca.select(i)

        insert = -1
        for c in range(end_index, insert+1):
            if array[i] < array[c]:
                insert -= 1
        array.insert(insert, array.pop(0))
        ca.update_array(array)
        end_index -= 1

        ca.text[1] = "Iterations: {}".format(w.vars['iterations'])
        ca.text[2] = "Swaps: {}".format(w.vars['swaps'])

def merge_sort(w, array, ca):
    #print array
    #title
    ca.text[0] = "Merge Sort"

    end_arr = []
    #sort in groups of 2
    for i in range(0, len(array), 2):
        sleep(0.001)
        ca.select(i)
        w.vars['iterations'] += 1
        if array[i] > array[i+1]: array[i], array[i+1] = swap(w, array[i], array[i+1])

        ca.text[1] = "Iterations: {}".format(w.vars['iterations'])
        ca.text[2] = "Swaps: {}".format(w.vars['swaps'])

    #print array
    ar_len = 2
    #print "start"
    while ar_len < (len(array)/2)+1:
        #print "start 2"
        for curr_in in range(0, len(array), ar_len*2):
            #print (ar_len, curr_in)
            ar, br = [], []
            for a in range(ar_len):
                #print curr_in + a, curr_in + a + ar_len
                ar.append(array[curr_in + a])
                br.append(array[curr_in + a + ar_len])
            #print ar, br,

            cr = merge_helper(ar, br, w, ca, curr_in)
            #print cr
            for i in range(len(cr)):
                sleep(DELAY)
                w.vars['swaps'] += 1
                array[curr_in+i] = cr[i]
                ca.select(curr_in+i)

            ca.text[1] = "Iterations: {}".format(w.vars['iterations'])
            ca.text[2] = "Swaps: {}".format(w.vars['swaps'])
        #print "done 2"
        ar_len *= 2
    print "done"

def merge_helper(a, b, w, ca, ci):
    c = []
    i = 0
    while len(a) > 0 or len(b) > 0:
        w.vars['iterations'] += 1
        sleep(DELAY)
        ca.select(ci + i)
        if len(a) == 0:
            c.append(b.pop(0))
        elif len(b) == 0:
            c.append(a.pop(0))
        elif a[0] < b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
        i += 1
    return c

def swap(w, a, b):
    w.vars['swaps'] += 1
    return b, a

#not very good
def magic_sort (w, array, ca):
    #title
    ca.text[0] = "Magic Sort"

    ret_arr = [0]
    for i in range (1,len (array)):

        w.vars['iterations'] += 1

        insert = len (ret_arr)
        for c in ret_arr:
            sleep(DELAY)
            ca.select(c)
            if (array[i] > array[c]):
                insert -= 1
        ret_arr.insert (insert, i)

        ca.text[1] = "Iterations: {}".format(w.vars['iterations'])
        ca.text[2] = "Swaps: {}".format(w.vars['swaps'])

    new_arr = []
    ca.select(-1)
    for i in ret_arr:
        sleep(DELAY)
        w.vars['swaps'] += 1
        w.vars['iterations'] += 1
        new_arr.insert(0, array[i])
        ca.update_array (new_arr)
        ca.text[1] = "Iterations: {}".format(w.vars['iterations'])
        ca.text[2] = "Swaps: {}".format(w.vars['swaps'])
