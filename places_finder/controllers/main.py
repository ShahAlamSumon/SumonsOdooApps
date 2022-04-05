import folium
import requests
import pandas as pd
from geopy.geocoders import Nominatim
from pandas.io.json import json_normalize
from odoo import http, _
from odoo.http import request
from odoo.exceptions import ValidationError


class SearchPlaces(http.Controller):

    @http.route(['/map_page/<int:location_id>'], type='http', auth='user', website=True)
    def map_page(self, location_id=None, **post):
        return request.render("map_by_folium.location_page", {'location_id': location_id})

    @http.route(['/search_location/<int:location_id>'], type='http', auth='user', methods=['GET'], website=True)
    def search_location(self, location_id=None, **kwargs):
        location = request.env['search.location'].browse(location_id)
        tiles = dict(location._fields['tiles'].selection).get(location.tiles)
        current_location_coord = [location.lat, location.lon]
        folium_map = folium.Map(location=current_location_coord, zoom_start=location.zoom_start, tiles=tiles)
        if location.city:
            popup_str = location.city.city_name
        else:
            popup_str = "Current Location Here"
        folium.Marker(current_location_coord, popup=popup_str).add_to(folium_map)
        map_render = folium_map.get_root().render()
        return map_render

    @http.route(['/foursquare_data_page/<int:source_id>'], type='http', auth='user', website=True)
    def cluster_tbl_page(self, source_id=None, **post):
        source = request.env['foursquare.wizard'].browse(source_id)
        df = self.get_dataframe(source)
        header_list = [i for i in df]
        item_list = [i for i in df.values.tolist()]
        values = {
            'header_list': header_list,
            'item_list': item_list
        }
        return request.render("map_by_folium.foursquare_data_page", values)

    def get_dataframe(self, source):
        geolocator = Nominatim(user_agent=source.user_agent)
        location = geolocator.geocode(source.address)
        latitude = location.latitude
        longitude = location.longitude
        try:
            url = 'https://api.foursquare.com/v2/venues/search?client_id={}&client_secret={}&ll={},{}&v={}&query={}&radius={}&limit={}'.format(
                source.client_id, source.client_secret,
                latitude, longitude,
                source.version, source.search_query, source.radius, source.limit)
            results = requests.get(url).json()
            venues = results['response']['venues']
            df = json_normalize(venues)
            return df
        except:
            raise ValidationError(_('Invalid input for Foursquare request'))
