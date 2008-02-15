# disallow.py --- Example of using Disallow with wildcards

#--[Imports]--------------------------------------------------------------------
from enthought.traits.api import Disallow, Float, \
                             HasTraits, Int, Str

#--[Code]-----------------------------------------------------------------------

class Person (HasTraits):
    name   = Str 
    age    = Int 
    weight = Float
    _      = Disallow
    
