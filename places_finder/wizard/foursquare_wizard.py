from odoo import api, fields, models, _


class FoursquareWizard(models.TransientModel):
    _name = 'foursquare.wizard'

    client_id = fields.Char(string='Client Id', required=True)
    client_secret = fields.Char(string='Client Secret', required=True)
    version = fields.Char(string='Version', required=True, default='20180604')
    limit = fields.Char(string='Limit', required=True, default='30')
    address = fields.Char(string='Address', required=True, default='102 North End Ave, New York, NY')
    user_agent = fields.Char(string='User Agent', required=True, default='foursquare_agent')
    search_query = fields.Char(string='Search Query', required=True, default='Restaurant')
    radius = fields.Char(string='Radius', required=True, default='500')

    def act_dataset(self):
        return {'type': 'ir.actions.act_url',
                'target': 'new',
                'url': '/foursquare_data_page/%s' % self.id,
                'res_id': self.id,
                }
