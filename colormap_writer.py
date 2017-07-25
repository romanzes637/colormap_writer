import seaborn as sns
import json


print("Reading names")
names = []
with open("names") as f:
    data = f.readlines()
    for line in data:
        names.extend(line.split())
print(names)


print("Importing colormaps")
n_colors = []
colors = []
n_components = []
for name in names:
    palette = sns.color_palette(name)
    n_components.append(len(palette[0]))
    n_colors.append(len(palette))
    colors.extend([x for color in palette for x in color])

colormaps = dict()
colormaps.update({"names": names})
colormaps.update({"n_colors": n_colors})
colormaps.update({"colors": colors})
colormaps.update({"n_components": n_components})

colormaps_json = json.dumps(colormaps)
# print(colormaps_json)


print("Writing colormaps")
with open("colormaps.json", 'w') as f:
    f.write(colormaps_json)


print("Done")
