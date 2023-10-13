import sys

import gi
gi.require_version("Gtk", "4.0")
from gi.repository import GLib,Gtk

from model import Model
from view import View
from presenter import Presenter

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    presenter = Presenter()
    presenter.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
