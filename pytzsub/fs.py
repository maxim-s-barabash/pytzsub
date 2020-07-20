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

"""Implements methods for working with the file system."""

TAB_CHAR = "\t"


def read_tab(filename, sep=TAB_CHAR):
    """Read tab files.

    Description of the teb file structure:
    - Columns are separated by a single tab.
    - Lines beginning with '#' are comments.
    - All text uses UTF-8 encoding.

    The columns of the table are as follows:
    1.  Subdivision names are listed as in the ISO 3166-2 standard
        published by the ISO 3166 Maintenance Agency (ISO 3166/MA).
    2.  Timezone name used in value of TZ environment variable.

    Args:
        filename (str): the path to the tab file.
        sep (str, optional): [description]. Defaults to TAB_CHAR.

    Returns:
        dict: key (str) iso_code, value (dict)

    Example:
        >>> from pytzsub.sub import DB_FILENAME
        >>> db = read_tab(DB_FILENAME)
    """
    table = {}
    with open(filename, "r") as fileptr:
        for line in fileptr.readlines():
            line = line.strip()
            if line and not line.startswith("#"):
                codes = line.split(sep)
                iso_code = codes[0]
                table[iso_code] = dict(tz=codes[1])
    return table
