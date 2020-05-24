def _read_from(filename, sep='\t'):
    table = {}
    with open(filename, 'r') as f:
        for line in f:
            if not line or line.startswith("#"):
                continue
            line = line.strip()
            codes = line.split(sep)
            iso_code = codes[0]
            table[iso_code] = dict(tz=codes[1])
    return table
