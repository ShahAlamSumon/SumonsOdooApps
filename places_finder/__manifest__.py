# -*- coding: utf-8 -*-
{
	'name': "Place Finder",
	'summary': """Find the place nearby based on user interest""",
	'description':
	"""Place Finder
	=================
	This app is using for finding the places nearby based on what user want like food, bus stand etc""",
	'author': "Shah Alam Sumon",
	'website': 'https://github.com/ShahAlamSumon',
	'category': 'Web',
	'version': '0.1',
	'license': 'LGPL-3',
	'depends': ['website'],
	'data': [
		'security/ir.model.access.csv',
		'wizard/foursquare_wizard.xml',
		'views/menu_views.xml',
		'views/map_template.xml',
	],
	"external_dependencies": {
		'python': ['folium', 'geocoder', 'pandas', 'geopy'],
	},
	'installable': True,
	'application': True,
	'auto_install': False,
}
