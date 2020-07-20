# MIT License

# Copyright (c) 2020 Maxim Barabash

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os

from .fs import read_tab

__all__ = ("sub_timezone", "all_code")

DB_FILENAME = os.path.join(os.path.dirname(__file__), "zone-sub.tab")
ISOCODE_INDEX = read_tab(DB_FILENAME)


def sub_timezone(isocode):
    """World timezone definitions.

    By country subdivision (e.g., provinces or states)

    Args:
        isocode (str): iso_code of country, provinces, states, e.g.

    Returns:
        (str, None): timezone name or None

    Example:
        >>> from pytzsub import sub_timezone
        >>> sub_timezone("US-CA")
        'America/Los_Angeles'
        >>> sub_timezone("FOO") == None
        True
    """
    return ISOCODE_INDEX.get(isocode, {"tz": None})["tz"]


def all_code():
    """Return all known iso_code of countries and subdivision.

    Example:
        >>> from pytzsub import all_code
        >>> "US-CA" in all_code()
        True
        >>> "FOO" in all_code()
        False
    """
    return tuple(ISOCODE_INDEX.keys())
