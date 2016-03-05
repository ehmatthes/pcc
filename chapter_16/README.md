Chapter 16
===

Pygal has been updated recently, which is a good thing; you're learning a library that's being steadily improved. If you're using the latest version of Pygal, you'll need to make some slight changes to the code in Chapter 16.

You can easily [install a version of Pygal](chapter_15/README.md#installing-pygal) that allows the code in the book to run exactly as it's written.

The first part of this update will tell you what to look for as you work through the section **Mapping Global Data Sets: JSON Format**, which begins on page 362. The second part will give you a page by page update. You can see the updated code files [here](pygal2_update/).

Updates
---

### The `pygal_maps_world` package

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
    
### Rendering tooltips correctly

As you probably saw in [Chapter 15](chapter_15/README.md#updates), you need to add a line each time you make a chart in order to render tooltips correctly:

<pre>
wm = World()
<b>wm.force_uri_protocol = 'http'</b>
</pre>
    
Page by page updates
---

In the following sections, bold lines of code differ from the code that appears in the book:

### p. 365, *countries.py* and *country_codes.py*

Use **`from pygal.maps.world import COUNTRIES`** instead of `from pygal.i18n import COUNTRIES`.

### p. 367, *americas.py*

Use **`from pygal.maps.world import World`** instead of `import pygal`.

Use **`wm = World()`** instead of `wm = pygal.Worldmap()`. Then add the line **`wm.force_uri_protocol = 'http'`**.

### p. 368, *na_populations.py*

Use **`from pygal.maps.world import World`** instead of `import pygal`.

Use **`wm = World()`** instead of `wm = pygal.Worldmap()`. Then add the line **`wm.force_uri_protocol = 'http'`**.

### p. 369-370, *world_populations.py*

Use **`from pygal.maps.world import World`** instead of `import pygal`.

Use **`wm = World()`** instead of `wm = pygal.Worldmap()`. Then add the line **`wm.force_uri_protocol = 'http'`**.s

