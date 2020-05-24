import os
from .fs import _read_from

__all__ = ['sub_timezone']
DB_FILENAME = os.path.join(os.path.dirname(__file__), 'zone-sub.tab')
ISOCODE_INDEX = _read_from(DB_FILENAME)
DEFAUIL = {'tz': None}


def sub_timezone(isocode):
    '''World timezone definitions by country subdivision
    (e.g., provinces or states)

    >>> from pytzsub import sub_timezone
    >>> sub_timezone('US-CA')
    'America/Los_Angeles'
    >>> 
    '''
    return ISOCODE_INDEX.get(isocode, DEFAUIL)['tz']


# if __name__ == "__main__":
#     import pprint
#     import pytz
#     # pprint.pprint(ISOCODE_INDEX)
#     for isocode in sorted(ISOCODE_INDEX.keys()):
#         tz = sub_timezone(isocode)
#         if tz not in pytz.common_timezones:
#             print('#!!! not in common_timezones', isocode)
#         print("%s\t%s" %(isocode, tz) )
