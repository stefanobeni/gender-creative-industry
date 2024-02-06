import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

groups = ['Women', 'Men']
data = {
        'Average Gender Split':  {'Advertising Industry Average': [49, 51], 'TW': [57, 43]},
        'Creative Roles Gender Split':        {'Advertising Industry Average': [29, 71], 'TW': [0, 100]},
        'Admin Roles Gender Split':           {'Advertising Industry Average': [70, 30], 'TW': [100, 0]}
        }
# Average Gender Split
df = pd.DataFrame(data)

fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(12, 8))
ax_flat = ax.flatten()
# wedges, texts, autotexts = 0, 0 , 0

for i, row_name in enumerate(df.index):
    for j, col_name in enumerate(df.columns):
        values = df.loc[row_name, col_name]
        wedges, texts, autotexts = ax_flat[i*3+j].pie(values, startangle=-90,
                                                      autopct=lambda pct: '{:1.0f}%'.format(pct) if pct > 0 else '',
                                                      textprops=dict(fontsize=24), colors=['#eec3cc', '#9196d2'],
                                                      pctdistance=0.5)
                                                      #d14c58 #9196d2 #4b6354 #f6bc3b #eec3cc
        ax_flat[i*3+j].set_title(f'{col_name} - {row_name}', fontsize=18)

ax_flat[0].set_title('Average Gender Split in UK \n Creative Agencies', fontsize=18)
ax_flat[1].set_title('Creative Roles Gender Split -\nAdvertising Industry Average', fontsize=18)
ax_flat[2].set_title('Admin Roles Gender Split -\nAdvertising Industry Average', fontsize=18)
ax_flat[3].set_title('Average Gender Split at TW', fontsize=18)

ax_flat[2].legend(['Women', 'Men'])
# fig.legend(wedges, groups)
plt.tight_layout()
plt.show()

# ax.pie(weights_overall_industry_standard, labels=groups, autopct="%1.0f%%")


'''
pie chart parameters:
labels=groups
shadow=True
explode = (0.2, 0)
startangle=-90
ax.axis("equal")
'''
plt.show()
