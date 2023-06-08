from IPython.core.display_functions import display
from ipywidgets import interact,interactive,fixed
from IPython.display import display
import ipywidgets as widgets

def func(x):
    return x**2

display(interact(func, x=10))
