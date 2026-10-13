import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from . import (
    datasets,
    lm,
    show,
)

import matplotlib
import matplotlib.pyplot as plt
import seaborn



colors = [
    "#6CA0A3",  # soft teal/blue shade from glass and walls
    "#D0C1A5",  # warm beige for walls
    "#2F3E46",  # deep blue/gray from shadows and corners
    "#403931",  # muted dark brown from wooden floor and frames
    "#E3584D",  # vibrant red-orange from robot's eye
    "#F0F0F0",  # light, almost white, for bright spots on walls
    "#7A7D80",  # mid-tone gray from shadows and robot's body
    "#F2B66D",  # accent color from robot's headlight illumination
]
palette = seaborn.color_palette(colors)

def setup_plot_style(dark=False):
    if dark:
        plt.style.use("dark_background")
    else:
        plt.style.use("default")
    seaborn.set_style("ticks")
    matplotlib.rcParams.update({
        "figure.figsize": (20, 8),
        "axes.grid": True,
    })
    seaborn.set_palette(palette)
