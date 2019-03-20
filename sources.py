
def parse(row):
    return [label.strip() for label in header.split(',')]

def get_sources(filename='sources.csv'):
    sources = dict()
    with open(filename, 'r') as infile:
        header, *rows = [parse(row) for row in infile.split('\n')]
        for row in rows:
            source = dict()
            for label, cell in zip(header, row):
                source[label] = cell
            title = row[0]
            sources[title] = source
    return sources
