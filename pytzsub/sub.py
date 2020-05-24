import os
from .fs import _read_from

__all__ = ['sub_timezone', 'all_code']
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


def all_code():
    '''Returns all known codes of countries and subdivision

    >>> from pytzsub import all_code
    >>> 'US-CA' in all_code()
    True
    >>> 'XXX' in all_code()
    False
    '''
    return tuple(ISOCODE_INDEX.keys())


# if __name__ == "__main__":
#     import pytz
#     for isocode in sorted(ISOCODE_INDEX.keys()):
#         tz = sub_timezone(isocode)
#         if tz not in pytz.common_timezones:
#             print('#!!! not in common_timezones', isocode)
#         print("%s\t%s" % (isocode, tz))

#     country_names = set(pytz.country_names.keys())
#     know_country_names = set([
#         x for x in all_code() if '-' not in x
#     ])
#     print("# not set country_names:", country_names ^ know_country_names)
