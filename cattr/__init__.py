from .converters import Converter

__author__ = 'Tin Tvrtković'
__email__ = 'tinchester@gmail.com'
__version__ = '0.2.0'


global_converter = Converter()

dumps = global_converter.dumps
loads = global_converter.loads
loads_attrs_fromtuple = global_converter.loads_attrs_fromtuple
loads_attrs_fromdict = global_converter.loads_attrs_fromdict
