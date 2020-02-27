---
layout: default
title: Chapter 16
---

There's a slight change to [Exercise 16-1](#exercise-16-1-san-francisco).

Pygal has been updated recently, which is a good thing; you're learning a library that's being steadily improved. If you're using the latest version of Pygal, you'll need to make some slight changes to the code in Chapter 16.

You can easily [install a version of Pygal](chapter_15/README.html#installing-pygal) that allows the code in the book to run exactly as it's written.

The first part of this update will tell you what to look for as you work through the section **Mapping Global Data Sets: JSON Format**, which begins on page 362. The second part will give you a page by page update.

Updates
---

### Exercise 16-1: San Francisco

You can still get historical weather data from Weather Underground in the CSV format, but the link to the CSV file is not visible on the screen. To get historical weather data, go to the [Weather Underground home page](wunderground.com), click on the Menu on the right side of the screen, and click on [Historical Weather](https://www.wunderground.com/history/). Enter a location, pick a starting date, and click Submit. A summary for this date will appear, with several tabs. Click on Custom, enter an end date on the next page, and click Get History.

If you scroll down you'll see the weather data for the range you requested, in a neatly formatted table. To get the CSV version of this data, append `&format=1` to the URL in your browser's address bar. You can do this by clicking in the address bar, pressing Ctrl-End, typing `&format=1`, and pressing Enter. Your URL should look something like this:

[https://www.wunderground.com/history/airport/PASI/2017/1/1/CustomHistory.html?dayend=1&monthend=7&yearend=2017&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1](https://www.wunderground.com/history/airport/PASI/2017/1/1/CustomHistory.html?dayend=1&monthend=7&yearend=2017&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1)

Once you see the data in CSV format you can either use the Save As dialog from your browser, or you can copy the data and paste it into a text editor to save it. It's good practice to use the *.csv* file extension when saving this kind of file.

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

