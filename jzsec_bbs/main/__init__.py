__version__ = '0.2.2'
from . import *



from django.utils.module_loading import autodiscover_modules
def autodiscover():
    autodiscover_modules('admin', register_to=site)

