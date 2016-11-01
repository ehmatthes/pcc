---
layout: default
title: Chapter 17
---

The second part of Chapter 17 walks you through a visualization summarizing the most popular Python projects on GitHub. One of the projects has been removed, but the project is still included in the results when you make an API call requesting the most popular projects. The project's name and number of stars is included, but there's no description. This causes an error in Pygal, but we can add a little code to address this.

This update affects the section *Visualizing Repositories Using Pygal*, which begins on page 384.

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