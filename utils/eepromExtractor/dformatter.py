#!/usr/bin/python

from string import Formatter

class DFormatter(Formatter):
     def get_value(self, field_name, args, kwargs):
         return getattr(kwargs, field_name)

     def get_field(self, field_name, args, kwargs):
          first, rest = field_name._formatter_field_name_split()
          obj = self.get_value(first, args, kwargs) 

          for is_attr, i in rest:
               obj = getattr(obj, i) if is_attr else obj[i]
          return obj, first

