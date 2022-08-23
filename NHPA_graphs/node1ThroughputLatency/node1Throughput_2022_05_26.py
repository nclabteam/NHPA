import matplotlib.pyplot as plt
from matplotlib.transforms import ScaledTranslation

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = "30"
import numpy as np
import pandas as pd
from matplotlib import transforms

df = pd.read_csv("/home/phuclh/PycharmProjects/graph/2022-05-26/throughput_latency_at_node1_ms_scale.csv", delimiter=',')

# Throughput data
xPos = [1, 4, 8, 12]
labels1 = ['1', '3', '6', '9']
hpaThroughput = df['t1']
onePodThroughput = df['t2']
threePodsThroughput = df['t3']
sixPodsThroughput = df['t4']

# Response time data
withHPALatency = df['l1'].tolist()
onePodLatency = df['l2'].tolist()
threePodsLatency = df['l3'].tolist()
sixPodsLatency = df['l4'].tolist()
yerr1 = df['d1'].tolist()
yerr2 = df['d2'].tolist()
yerr3 = df['d3'].tolist()
yerr4 = df['d4'].tolist()

x = np.arange(len(labels1))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots(1, 2, figsize=(10, 6), sharex=True, sharey=False)
# ax2 configuration
ax[0].set_ylim(0, 200)
ax[0].set_ylabel('Average response time [ms]')
ax[0].set_xticks(xPos)
ax[0].set_xticklabels(labels1)
# ax[0] configuration
ax[1].set_ylim(0, 500)
ax[1].set_ylabel('Throughput [req/sec]')
ax[1].set_xticks(x)
ax[1].set_xticklabels(labels1)

# ax[0] is used to display the response time
er1 = ax[0].errorbar(x + 0.25, withHPALatency, yerr=yerr1, marker="o",  markersize=10, linewidth=4, linestyle="none", label='NHPA')
er2 = ax[0].errorbar(x - 0.25, onePodLatency, yerr=yerr2, marker="o", markersize=10, linewidth=4, linestyle="none", label='KE (1 pod)')
er3 = ax[0].errorbar(x - 0.1, threePodsLatency, yerr=yerr3, marker="o", markersize=10, linewidth=4, linestyle="none", label='KE (3 pods)')
er4 = ax[0].errorbar(x + 0.1, sixPodsLatency, yerr=yerr4, marker="o", markersize=10, linewidth=4, linestyle="none", label='KE (6 pods)')
legend2 = ax[0].legend(loc='upper left')
legend2.get_frame().set_alpha(0.5)
# legend2.get_frame().set_facecolor((0, 0, 1, 0.1))
ax[0].grid(axis='both')

# ax[1] is used to display the throughput
rects1 = ax[1].bar(x + (1.5 * width), hpaThroughput, width, label='NHPA', color='black', alpha=0.7, edgecolor='black')
rects2 = ax[1].bar(x - (1.5 * width), onePodThroughput, width, label='KE (1 pod)', color='white', alpha=0.7, edgecolor='black')
rects3 = ax[1].bar(x - width/2, threePodsThroughput, width, label='KE (3 pods)', color='darkgray', alpha=0.7, edgecolor='black')
rects4 = ax[1].bar(x + width/2, sixPodsThroughput, width, label='KE (6 pods)', color='dimgray', alpha=0.7, edgecolor='black')

legend1 = ax[1].legend(loc='upper left')
legend1.get_frame().set_alpha(0.5)
trans = transforms.blended_transform_factory(ax[0].transData, ax[0].transAxes)
ax[0].text(1.5, -0.2,  "(a)", transform=trans, ha='center', va='bottom', color='black')
ax[1].text(7.15, -0.2,  "(b)", transform=trans, ha='center', va='bottom', color='black')
fig.text(4.325, -0.2,  "Concurrent requests", transform=trans, ha='center', va='bottom', color='black')

fig.tight_layout()
plt.show()
