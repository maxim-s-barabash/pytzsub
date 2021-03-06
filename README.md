# pytzsub

[![Build Status](https://travis-ci.com/maxim-s-barabash/pytzsub.svg?branch=master)](https://travis-ci.com/maxim-s-barabash/pytzsub)
[![PyPI version](https://badge.fury.io/py/pytzsub.svg)](https://badge.fury.io/py/pytzsub)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

World timezone definitions by country subdivision (e.g., provinces or states)

## Accuracy of the database

The database is not authoritative, and it surely has errors. 
Corrections are welcome and encouraged. 


## Installation

As per usual:

```shell
pip install pytzsub
```

## Examples

```python
>>> from pytzsub import sub_timezone
>>> sub_timezone('US-CA')
'America/Los_Angeles'
```

```python
>>> from pytzsub import all_code
>>> 'US-CA' in all_code()
True
```


```python
>>> from pytzsub import sub_timezone
>>> from pytz import timezone
>>> tz = timezone(sub_timezone('CA-QC'))
>>> type(tz)
<class 'pytz.tzfile.America/Toronto'>
```

## Links

- Time Zone Database https://www.iana.org/time-zones
- ISO_3166-2 https://en.wikipedia.org/wiki/ISO_3166-2
