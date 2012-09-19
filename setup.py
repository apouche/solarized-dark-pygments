""" 
A Solarized style for Pygments
""" 
from setuptools import setup 

setup( 
    name         = 'solarized', 
    version      = '1.1', 
    description  = __doc__, 
    author       = "Pieter Belmans", 
    install_requires = ['pygments'],
    packages     = ['solarized'], 
    entry_points = '''
    [pygments.styles]
    solarized     = solarized:SolarizedStyle
    solarized256  = solarized:Solarized256Style
    '''
)
