import numpy as np
import matplotlib.pyplot as plt
from graph_engine import Grid 
COLOR_WALL = (125, 16, 16)
COLOR_PASSABLE = (255, 255, 255)
COLOR_PATH = (33, 204, 90) # green
COLOR_SEARCHED = (92, 123, 247) # blue
COLOR_START = (255, 0, 72) # red
COLOR_GOAL = (255, 191, 0) # yellow
COLOR_CURRENT = (33, 204, 90) # green
COLOR_NEXT = (143, 2, 250)
COLOR_FRONTIER = (192, 52, 235)
pixel_fontsize = 20
def plot_details(graph, id, style): # id: horizontal, vertical
    pixel_color = COLOR_PASSABLE
    r = None
    if 'number' in style and id in style['number']: 
        r = " %d" % style['number'][id]
    if 'point_to' in style and style['point_to'].get(id, None) is not None:
        (x1, y1) = id
        (x2, y2) = style['point_to'][id]
        if x2 == x1 + 1 and y1 == y2: r = " → "
        if x2 == x1 - 1 and y1 == y2: r = " ← "
        if y2 == y1 + 1 and x1 == x2: r = " ↓ "
        if y2 == y1 - 1 and x1 == x2: r = " ↑ "
        if x2 == x1 + 1 and y2 == y1 + 1: r = " ↘ "
        if x2 == x1 + 1 and y2 == y1 - 1: r = " ↗ "
        if x2 == x1 - 1 and y2 == y1 + 1: r = " ↙ "
        if x2 == x1 - 1 and y2 == y1 - 1: r = " ↖ "
        pixel_color = COLOR_SEARCHED
    if 'path' in style and id in style['path']:   
        pixel_color = COLOR_PATH
    if 'start' in style and id == style['start']: 
        r = "○"
        pixel_color = COLOR_START
    if 'goal' in style and id == style['goal']:
        r = "☆"
        pixel_color = COLOR_GOAL
    if 'current' in style and id == style['current']:
        pixel_color = COLOR_CURRENT
    if 'frontier' in style and id in style['frontier']:
        pixel_color = COLOR_FRONTIER
    if 'next' in style and id == style['next']:
        pixel_color = COLOR_NEXT
    if id in graph.walls:
        pixel_color = COLOR_WALL
    # notice that in ax.annotate need horizontal x and vertical y
    # while ax.imshow need horizontal y and vertical x
    return r, pixel_color

def plot_grid(ax, graph:Grid, **details):
    data = np.zeros([graph.height, graph.width, 3]).astype(np.uint8) # height, width, channel
    for y in range(graph.height):
        for x in range(graph.width):
            r, pixel_color = plot_details(graph, (x,y), details)
            if r:
                ax.annotate(r, (x,y), ha='center', va='center', fontsize=pixel_fontsize)
            data[y, x, :] = pixel_color
    # notice that in ax.annotate need horizontal x and vertical y
    # while ax.imshow need horizontal y and vertical x
    ax.imshow(data)
    ax.tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=False, right=False, left=False, labelleft=False)
    ax.hlines(y=np.arange(0, graph.height+1)-0.5, 
              xmin=np.full(graph.height+1, 0)-0.5, 
              xmax=np.full(graph.height+1, graph.width)-0.5, 
              color="black", linewidth=1)
    ax.vlines(x=np.arange(0, graph.width+1)-0.5, 
              ymin=np.full(graph.width+1, 0)-0.5, 
              ymax=np.full(graph.width+1, graph.height)-0.5, 
              color="black", linewidth=1)    
    return ax 

def tellme(s, ax):
    print(s)
    ax.set_title(s, fontsize=16)
    plt.draw()