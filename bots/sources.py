
def parse(row):
    return [label.strip() for label in row.split(',')]

def get_sources(filename='sources.csv'):
    sources = dict()
    with open(filename, 'r') as infile:
        header, *rows = [parse(row) for row in infile.read().split('\n')]
        for row in rows:
            if len(row) == 1:
                continue
            source = dict()
            for label, cell in zip(header, row):
                source[label] = cell
            title = row[0]
            sources[title] = source
    return sources
