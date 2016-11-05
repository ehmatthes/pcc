---
layout: default
title: Chapter 17
---

The second part of Chapter 17 walks you through a visualization summarizing the most popular Python projects on GitHub. One of the projects has been removed, but the project is still included in the results when you make an API call requesting the most popular projects. The project's name and number of stars is included, but there's no description. This causes an error in Pygal, but we can add a little code to address this. Also, the settings for font sizes have moved from `config` to `style` in Pygal 2.0.0.

This update affects the section *Visualizing Repositories Using Pygal*, which begins on page 384.

Updates
---

### p. 386, *python_repos.py*

Here's the original code for styling the chart:

```python
# Make visualization.
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
```

Here's the updated version, with the font size settings moved from `my_config` to `my_style`:

```python
# Make visualization.
my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
```

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

We first try to pull the description from the dictionary `repo_dict`. Then we make sure a description was provided. If a description was not returned from the API call, we set a description ourselves. At the moment, the project [Shadowsocks](https://github.com/shadowsocks/shadowsocks) is missing a description, and if you run the code shown above you'll see *No description provided* for that project.

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

### Complete updated version of *python_repos.py*

Here's the complete, updated version of *python_repos.py*:

```python
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call, and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Store API response in a variable.
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories.
repo_dicts = response_dict['items']

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

# Make visualization.
my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
```