from pygal.maps.world import World

wm = World()
wm.force_uri_protocol = 'http'
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('na_populations.svg')
