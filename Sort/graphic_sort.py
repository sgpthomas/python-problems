#imports
from gi.repository import Gtk, cairo
import sys
from random import randint
import threading
import time
import sorter as s
from math import floor

WIDTH, HEIGHT = 1047, 770
SIZE = 256

class Worker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.should_kill = False
        self.array = gen_rand_array(SIZE)
        #self.array = [8, 7, 0, 3, 4, 2, 6, 1]
        app.set_array(self.array)

        self.vars = {'iterations':0, 'swaps':0}
        self.count = 0

    def run(self):
        while not self.should_kill:
            if is_sorted(app.array):
                print self.vars['iterations'], self.vars['swaps'], self.count
                self.kill()
            else:
                self.count += 1
                s.sort(self, app.array, app)

    def kill(self):
        self.should_kill = True

class CairoArea(Gtk.DrawingArea):
    def __init__(self, array=None):
        #Gtk Stuffs
        Gtk.Widget.__init__(self)
        Gtk.DrawingArea.__init__(self)
        self.expand = True
        self.show_all()

        #vars
        self.uplim = 10
        self.lowlim = 0
        if array != None: self.set_array (array)
        else: self.array = None
        self.selected = -1
        self.text = []

    def draw(self, widget, cr):
        if self.array != None:
            #establish drawing dimensions
            width = self.get_allocated_width()
            height = self.get_allocated_height()
            bar_width = float(width) / len(self.array)
            quantize = height / float(self.uplim)

            for i in range(len(self.array)):
                #print (self.array[i], quantize, height)
                if i == self.selected:
                    cr.set_source_rgb(200,0,0)
                else:
                    cr.set_source_rgb(0,0,0)
                    cr.set_line_width(0.5)
                cr.rectangle(i*bar_width, height-(quantize*self.array[i]), bar_width, quantize*self.array[i])
                #print (i*bar_width, quantize*self.array[i], bar_width, height-(quantize*self.array[i]), self.array[i])
                if i == self.selected:
                    cr.fill()
                else:
                    cr.stroke()

            #text rendering
            cursor = 20
            for s in self.text:
                cr.set_source_rgb(0,0,0)
                #cr.select_font_face("Open Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
                cr.set_font_size(12)
                cr.move_to(10, cursor)
                cr.show_text(s)
                cursor += 15

    def set_array(self, array):
        high = None
        low = None
        for val in array:
            if high == None: high = val
            elif val > high: high = val

            if low == None: low = val
            elif val < low: low = val

        self.uplim = high
        self.lowlim = low
        self.array = array

    #for when he high and the low of the array don't change
    def update_array(self, array):
        self.array = array
        self.update()

    def select(self, index):
        self.selected = index
        self.update()

    def update(self):
        self.queue_draw_area(0, 0, self.get_allocated_width(), self.get_allocated_height())

def gen_rand_array(length):
    ret_arr = []
    for a in range(length):
        ret_arr.append(randint(0, length))

    return ret_arr

def is_sorted(array):
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            return False
    return True

def destroy(window):
    thr.kill()
    Gtk.main_quit()

app = CairoArea()
thr = Worker()
def main():
    window = Gtk.Window()
    window.set_size_request (WIDTH, HEIGHT)
    window.set_title("Graphic Sort")

    box = Gtk.Box()
    box.set_border_width(10)
    box.pack_start(app, True, True, 0)
    window.add(box)

    app.connect('draw', app.draw)
    window.connect_after('destroy', destroy)
    window.show_all()

    thr.start()
    Gtk.main()

if __name__ == "__main__":
    sys.exit(main())
