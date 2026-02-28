import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Read CSV file (semicolon delimiter and comma decimal separator)
df = pd.read_csv('your_neurosynth_results.csv', sep=';', decimal=',')

# Categories matching CSV
categories = ['Memory & cognition', 'Motor & somatosensory', 'Speech & language']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

for category_name, color in zip(categories, colors):
    # Filter for this category
    df_filtered = df[df['Category'] == category_name]
    
    concepts = df_filtered['Concept'].tolist()
    scores = df_filtered['Association Score'].tolist()
    
    n = len(concepts)
    angles = [i / float(n) * 2 * pi for i in range(n)]
    angles += angles[:1]
    scores += scores[:1]
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
    
    ax.plot(angles, scores, 'o-', linewidth=2.5, markersize=8, color=color)
    ax.fill(angles, scores, alpha=0.25, color=color)
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(concepts, size=19)
    ax.set_ylim(0, 0.65)
    ax.set_yticks([0.1, 0.2, 0.3, 0.4, 0.5])
    ax.tick_params(axis='y', labelsize=14)
    ax.grid(True)
    
    plt.title(f'{category_name}', fontsize=22, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig(f'radar_plot_{category_name}_SR.png', dpi=1200, bbox_inches='tight')
    plt.show()

print("All radar plots saved!")
