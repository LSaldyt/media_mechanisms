import pandas
import matplotlib.pyplot as plt
import seaborn as sns

def get_bias():
    biasLookup = dict()
    with open('bias.csv') as infile:
        lines = infile.read().split('\n')[1:]
        for line in lines:
            if line != '':
                k, a, b = line.split(',')
            biasLookup[k] = (a, b)
    return biasLookup


def get_traffic():
    return pandas.read_csv('data.csv')#.set_index('Source')

def combine():
    bias = get_bias()
    def combiner(row):
        a, b = bias[row['Source']]
        row['Objectivity'] = a
        row['Bias']        = b
        return row
    data = get_traffic()
    data = data.apply(combiner, axis=1)
    data = data.set_index('Source')
    return data

def plot():
    f, ax = plt.subplots(figsize=(8,8))
    ax.set_aspect('equal')
    #data = combine()
    data = pandas.read_csv('bias.csv')
    clean = lambda x : [float(i) for i in x]
    x = clean(data['Bias'])
    y = clean(data['Objectivity'])
    pairs = list(zip(x, y))

    #print(pairs)
    left   = [p for p in pairs if p[0] < 5]
    center = [p for p in pairs if p[0] < 5 and p[0] > -5]
    right  = [p for p in pairs if p[0] > 5]
    left_x, left_y   = zip(*left)
    mid_x, mid_y     = zip(*center)
    right_x, right_y = zip(*right)

    kws = dict(n_levels=20, shade=True, shade_lowest=False)
    sns.set(style="darkgrid", font_scale=1.5)
    sns.kdeplot(list(left_x),  list(left_y),  cmap='Blues', ax=ax, **kws)
    sns.kdeplot(list(right_x), list(right_y), cmap='Reds', ax=ax, **kws)
    sns.kdeplot(list(mid_x), list(mid_y), cmap='Purples', ax=ax, **kws)
    sns.scatterplot(x, y, color='k')

    red = sns.color_palette("Reds")[-2]
    blue = sns.color_palette("Blues")[-2]
    purple = sns.color_palette("Purples")[-2]

    ax.text(-35, 60, "Left", size=16, color=blue)
    ax.text(35, 55,  "Right", size=16, color=red)
    ax.text(-15, 75, "Neutral", size=16, color=purple)

    plt.title('Topology of The Political Media Landscapce')
    plt.xlabel('Bias')
    plt.ylabel('Objectivity')
    plt.show()

plot()
