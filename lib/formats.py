from random import choice, shuffle

colors = [ 'b', 'g', 'r', 'c', 'm', 'y', 'k' ]
line_styles = [ '-', '--', '-.', ':' ]
point_styles = [ 'o', '+', '.', 's', 'p', 'D' ] 

shuffle(colors)
formats = [ '%s%s%s' % (color, choice(point_styles), choice(line_styles)) for color in colors ]
def fmt(idx, bar=False):
    return formats[idx]

