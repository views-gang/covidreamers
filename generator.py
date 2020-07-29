import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import requests
import datetime

ekb = (56.688468, 56.988468, 60.45337, 60.75337)
today = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

data = requests.get('https://www.gorses.na4u.ru/data/COVID.json').json()

    coords = []
for i in data['features']:
    coords.append(i['geometry']['coordinates'])
coords = pd.DataFrame(coords)

coords=coords[coords[0]>ekb[0]]
coords=coords[coords[0]<ekb[1]]
coords=coords[coords[1]>ekb[2]]
coords=coords[coords[1]<ekb[3]]

norm_coords = (coords-[ekb[0], ekb[2]]).round(2).mul(100)


stats = np.zeros(shape=(32,32))
for i in norm_coords.iterrows():
    stats[int(i[1][0]),int(i[1][1])] +=1

fig = plt.figure(frameon=False)
fig.set_size_inches(20,20)
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)

plt.imshow(stats/255, aspect='auto', cmap='plasma')
plt.savefig(f'{today}.png')
