from random import randint
from graphic_sort import CairoArea, Worker
from time import sleep

def sort(w, array, ca):
    #label
    if len(ca.text) != 3:
        ca.text = []   
        ca.text.append("Graphic Sorting")
        ca.text.append("Iterations: 0")
        ca.text.append("Swaps: 0")
        
    better_bubblesort(w, array, ca)
    #bubblesort(w, array, ca)
       
def better_bubblesort(w, array, ca):
    #label
    ca.text[0] = "Better Bubble Sorting"
    
    if 'bubble' not in w.vars: w.vars['bubble'] = len(array)
    l = w.vars['bubble']
    for i in range(1, l):
        w.vars['iterations'] += 1
        sleep(0.001)
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
        sleep(0.0001)
        ca.select(i)
        if array[i] < array[i-1]:
            w.vars['swaps'] += 1
            array[i], array[i-1] = array[i-1], array[i]
        ca.update_array(array)
        
        ca.text[1] = "Iterations: {}".format(w.vars['iterations'])
        ca.text[2] = "Swaps: {}".format(w.vars['swaps'])
        
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
        sleep(0.0001)
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
        
def merge_sort (w, array, ca):
    #title
    ca.text[0] = "Merge Sort"

def magic_sort (w, array, ca):
    #title
    ca.text[0] = "Magic Sort"

    ret_arr = [0]  
    for i in range (1,len (array)):
        
        w.vars['iterations'] += 1
        
        insert = len (ret_arr)
        for c in ret_arr:
            sleep(0.0001)
            ca.select(c)
            if (array[i] > array[c]):
                insert -= 1
        ret_arr.insert (insert, i)
            
        ca.text[1] = "Iterations: {}".format(w.vars['iterations'])
        ca.text[2] = "Swaps: {}".format(w.vars['swaps'])
    
    new_arr = []
    ca.select(-1)
    for i in ret_arr:
        sleep(0.001)
        w.vars['swaps'] += 1
        w.vars['iterations'] += 1
        new_arr.insert(0, array[i])
        ca.update_array (new_arr)
        ca.text[1] = "Iterations: {}".format(w.vars['iterations'])
        ca.text[2] = "Swaps: {}".format(w.vars['swaps'])
    



















