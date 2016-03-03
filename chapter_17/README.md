Chapter 17
===

Updates
---

As you probably saw in [Chapter 15](chapter_15/README.md#updates) and [Chapter 16](chapter_16/README.md#updates), you'll need to add a line each time you make a chart in order to render tooltips correctly:

<pre>
chart = pygal.Bar()
<b>chart.force_uri_protocol = 'http'</b>
</pre>

Page by page updates
---

### p. 384-385, python_repos.py

<pre>
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
<b>chart.force_uri_protocol = 'http'</b>
</pre>

### p. 387-388, bar_descriptions.py

<pre>
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
<b>chart.force_uri_protocol = 'http'</b>
</pre>