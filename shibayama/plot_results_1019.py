# %%
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.size'] = 14

OUT_DIR = './figures'
os.makedirs(OUT_DIR, exist_ok=True)

def savefig(filename, dir=OUT_DIR, dpi=300, bbox_inches='tight'):
    plt.savefig(f"{dir}/{filename}.png", dpi=dpi, bbox_inches=bbox_inches)
    plt.savefig(f"{dir}/{filename}.pdf", dpi=dpi, bbox_inches=bbox_inches)

def barplot_results(results, fbasename, figsize=(4, 3), title=None, colors=None, legend=None):
    """
    Plot the results of the experiment.

    Parameters:
    results (dict): Dictionary containing the results of the experiment.
    title (str): Title of the plot.
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    conditions = list(results.keys())
    values = list(results.values())
    if colors is None:
        colors = ['#FF9999', '#66B3FF', '#99FF99']  # Example colors for the bars
    bar_width = 0.70
    x = np.arange(len(conditions))

    ax.bar(x, values, bar_width, label='Battachalya Distance', color=colors, edgecolor='black')
    ax.set_xticks(x)
    ax.set_xticklabels(conditions)
    ax.set_ylim(0, max(values) + 0.05)  # Adjust y-axis limit for better visibility
    ax.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Add a horizontal line at y=0
    # 縦グリッドをなくす
    ax.xaxis.grid(True, linestyle='--', alpha=0.7)
    ax.yaxis.grid(True, linestyle='--', alpha=0.7)
    for i, v in enumerate(values):
        ax.text(i, v + 0.01, f"{v:.4f}", ha='center', va='bottom', fontsize=10)  # Display values on top of bars
    # ax.set_title(title if title else 'Experiment Results', fontsize=14)
    ax.set_ylabel('Battachalya Distance')
    if legend:
        ax.legend()
    plt.grid()
    savefig(fbasename)
    plt.show()
    return fig, ax

# Example usage
if __name__ == "__main__":
    figsize = (5, 4)

    res_color = {
        'whilte': 0.1589,
        'gray': 0.1055,
        'black': 0.0089
    }
    colors = ['#ffffff', '#cccccc', '#000000']  # Colors for the bars
    barplot_results(res_color, 'rl-bgcolor', figsize=figsize, title='Background Color', colors=colors)

    res_size = {
        'small': 0.0070,
        'medium': 0.0595,
        'large': 0.1616
    }
    # colors = ['#ffffff', '#ffffff', '#ffffff']  # Colors for the bars
    # use Set2 colormap from matplotlib
    colors = plt.get_cmap('Set2').colors[:3]
    barplot_results(res_size, 'rl-size', figsize=figsize, title='Pseudo Fish Size', colors=colors)

    res_number_df = pd.DataFrame({
        'Real': [5, 5, 5, 8, 8, 8],
        'Pseudo': [2, 3, 4, 2, 3, 4],
        'Battachalya Distance': [0.0702, 0.0998, 0.1197, 0.0434, 0.0531, 0.0683]
    })
    res_number_df.pivot(index='Real', columns='Pseudo', values='Battachalya Distance').plot(kind='bar', figsize=figsize)
    # plt.title('Number of Pseudo Fish vs Real Fish')
    plt.xlabel('Number of Real Fish')
    plt.ylabel('Battachalya Distance')
    plt.legend({'2 (indep.)', '3 (indep.)', '4 (formation)'})
    savefig('rl-number')
    plt.show()

# %%
