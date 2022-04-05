from odoo import http, _
from odoo.http import request


class WebsiteIntranet(http.Controller):

    @http.route(['/team'], type='http', auth="public", website=True)
    def employee_page(self, **kwargs):
        employees = request.env['hr.employee'].sudo().search([])
        return request.render("employees_website.team_web_page", {'employees': employees})
