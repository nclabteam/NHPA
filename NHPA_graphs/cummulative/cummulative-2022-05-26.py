import matplotlib.pyplot as plt
from matplotlib.transforms import ScaledTranslation
import pandas as pd
import numpy as np
from matplotlib import transforms

N = 3
plt.rcParams["axes.prop_cycle"] = plt.cycler("color", plt.cm.viridis(np.linspace(0, 1, N)))
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = "13"

# Cummulative throughput data
df1 = pd.read_csv("../2022-05-26/evaluation_result_2022_05_26.csv",
                  delimiter=',')

# x position, y lim, and legend definition
x_pos = [0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14]
y = np.arange(0, 1000, 100)
legend = ["Node1", "Node2", "Node3"]
labels1 = list(["3:3:3", "5:2:2", "7:1:1", "3:3:3", "5:2:2", "7:1:1", "3:3:3", "5:2:2", "7:1:1", "3:3:3", "5:2:2", "7:1:1"])
node1_nine = df1['node1']
node2_nine = df1['node2']
node3_nine = df1['node3']
width = 0.8  # the width of the bars: can also be len(x) sequence

fig, axe = plt.subplots(1)
# Left sub-figure
y_range = np.arange(0, 1000, 500)
axe.set_ylim(0, 500, 10)
# axe.set_yticks(y_range)
axe.set_ylabel("Throughput [req/s]", fontsize=12)
axe.set_xticks(x_pos)
axe.set_xticklabels(labels1, fontsize=15)
axe.bar(x_pos, node1_nine, width, label='Node 1', color='black', edgecolor='black', alpha=.7)
axe.bar(x_pos, node2_nine, width, bottom=node1_nine,
       label='Node 2', color='dimgray', edgecolor='black', alpha=.7)
axe.bar(x_pos, node3_nine, width, bottom=node1_nine+node2_nine,
       label='Node 3', color='darkgray', edgecolor='black', alpha=.7)
axe.legend(fontsize=12)

# Set text
trans = transforms.blended_transform_factory(axe.transData, axe.transAxes)
axe.text(1, -0.4,  "KE (1-1-1)", transform=trans, ha='center', va='bottom', color='black', fontsize=12)
axe.text(5, -0.4,  "KE (3-3-3)", transform=trans, ha='center', va='bottom', color='black', fontsize=12)
axe.text(9, -0.4,  "KE (6-6-6)", transform=trans, ha='center', va='bottom', color='black', fontsize=12)
axe.text(13, -0.4,  "NHPA", transform=trans, ha='center', va='bottom', color='black', fontsize=12)
axe.text(7, -0.28,  "Proportion of concurrent requests", transform=trans, ha='center', va='bottom', color='black', fontsize=12)
axe.tick_params(axis='x', rotation=45)
axe.tick_params(axis='both', which='major', labelsize=12)
plt.tight_layout()
plt.show()
