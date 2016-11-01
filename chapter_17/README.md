---
layout: default
title: Chapter 17
---

The second part of the chapter walks you through a visualization summarizing the most popular Python projects on GitHub. One of the projects has been removed, but the project is still included in the results when you make an API call requesting the most popular projects. The project's name and number of stars is included, but there's no description. This causes an error in Pygal, but we can add a little code to address this.

This update affects the section **Visualizing Repositories Using Pygal**, which begins on page 384.

Updates
---

### p. 389, *python_repos.py* 

Here's the original code for generating the data that will be included on the chart:

```python
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        }
    plot_dicts.append(plot_dict)
```

And here's the updated version:

```python
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    # Some projects lack a description, which causes an error when 
    #  labeling bars. Specify a label if there's no description.
    description = repo_dict['description']
    if not description:
        description = "No description provided."

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description,
        }
    plot_dicts.append(plot_dict)
```

We first try to pull the description from the dictionary `repo_dict`. Then we make sure a description was provided. If a description was not returned from the API call, we set a description ourselves. At the moment, the project *Shadowsocks* is missing a description, and if you run the code shown above you'll see *No description provided* for that project.

### p. 390, *python_repos.py*

This also affects the code on page 390, which should now be:

```python
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    # Some projects lack a description, which causes an error when 
    #  labeling bars. Specify a label if there's no description.
    description = repo_dict['description']
    if not description:
        description = "No description provided."

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description,
        'xlink': repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)
```


### The `plot_dicts`

The dictionary `COUNTRIES` and the world map module have been moved to a separate package called `pygal_maps_world`. Here's how to install this package:

    $ pip install --user pygal_maps_world
    
On Windows, this is:

    $ python -m pip install --user pygal_maps_world
    
### *countries.py*, *country_codes.py*

The dictionary `COUNTRIES` needs to be imported from `pygal_maps_world` now:

    from pygal.maps.world import COUNTRIES
    
### *world_populations.py*, *americas.py*, *na_populations.py*

Pygal's world map has been moved and renamed, so these progams need an additional import statement. This update also affects one other line of code. Add the following import statement near the top of the file:

    from pygal.maps.world import World
    
In the line that creates the world map, change `Worldmap` to `World`:

    wm = World()
    
Page by page updates
---

In the following sections, bold lines of code differ from the code that appears in the book:

### p. 365, *countries.py* and *country_codes.py*

Use **`from pygal.maps.world import COUNTRIES`** instead of `from pygal.i18n import COUNTRIES`.

### p. 367, *americas.py*

Use **`from pygal.maps.world import World`** instead of `import pygal`.

Use **`wm = World()`** instead of `wm = pygal.Worldmap()`.

### p. 368, *na_populations.py*

Use **`from pygal.maps.world import World`** instead of `import pygal`.

Use **`wm = World()`** instead of `wm = pygal.Worldmap()`.

### p. 369-370, *world_populations.py*

Use **`from pygal.maps.world import World`** instead of `import pygal`.

Use **`wm = World()`** instead of `wm = pygal.Worldmap()`.

