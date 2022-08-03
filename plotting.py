import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Ad_Figure():
    def __init__(self) -> None:
        self.fig = None
        self.ax = None
    def ad_plot(self,ads_selected):
        labels, counts = np.unique(ads_selected, return_counts=True)
        freq_series = pd.Series(counts)
        freq_series.index = labels
        clrs = ['green' if (x < max(counts)) else 'red' for x in counts ]
        self.fig = plt.figure(figsize=(12, 4))
        self.ax = freq_series.plot(kind='barh', color=clrs, width=0.8,use_index = True)
        self.ax.set_title('Histogram of ads selections')
        self.ax.set_xlabel('Number of times each ad was selected')
        self.ax.set_ylabel('Ads')
        rects = self.ax.patches
        # For each bar: Place a label
        for rect in rects:
            # Get X and Y placement of label from rect.
            x_value = rect.get_width()
            y_value = rect.get_y() + rect.get_height() / 2
            # Number of points between bar and label. Change to your liking.
            space = 5
            # Vertical alignment for positive values
            ha = 'left'
            # Use X value as label and format number with one decimal place
            label = "{:.0f}".format(x_value)
            # Create annotation
            self.ax.annotate(
                label,                      # Use `label` as label
                (x_value, y_value),         # Place label at end of the bar
                xytext=(space, 0),          # Horizontally shift label by `space`
                textcoords="offset points", # Interpret `xytext` as offset in points
                va='center',                # Vertically center label
                ha=ha)                      # Horizontally align label differently for
                                            # positive and negative values.
    def update_plot(self,ads_selected):
        self.fig.clf()
        labels, counts = np.unique(ads_selected, return_counts=True)
        freq_series = pd.Series(counts)
        freq_series.index = labels
        clrs = ['green' if (x < max(counts)) else 'red' for x in counts ]
        self.ax = freq_series.plot(kind='barh', color=clrs, width=0.8,use_index = True)
        self.ax.set_title('Histogram of ads selections')
        self.ax.set_xlabel('Number of times each ad was selected')
        self.ax.set_ylabel('Ads')
        rects = self.ax.patches
        for rect in rects:
            # Get X and Y placement of label from rect.
            x_value = rect.get_width()
            y_value = rect.get_y() + rect.get_height() / 2
            # Number of points between bar and label. Change to your liking.
            space = 5
            # Vertical alignment for positive values
            ha = 'left'
            # Use X value as label and format number with one decimal place
            label = "{:.0f}".format(x_value)
            # Create annotation
            self.ax.annotate(
                label,                      # Use `label` as label
                (x_value, y_value),         # Place label at end of the bar
                xytext=(space, 0),          # Horizontally shift label by `space`
                textcoords="offset points", # Interpret `xytext` as offset in points
                va='center',                # Vertically center label
                ha=ha)                      # Horizontally align label differently for
                                            # positive and negative values.   

def regret_plot(regret,title = 'Regret plot for random approach'):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    plt.plot(regret)
    ax.set_title(title)
    ax.set_xlabel('Number of ads shown')
    ax.set_ylabel('Regret after N ads')
    ax.set_xlim(0,len(regret))
    ax.set_ylim(0,max(regret)+1)