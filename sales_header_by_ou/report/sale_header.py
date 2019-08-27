from odoo import models, fields, api,tools, _
import os
import base64


class OperatingUnit(models.Model):
    _inherit = 'operating.unit'
    _description = 'Logo in operating unit'

    def _get_logo(self):
        return base64.b64encode(open(
            os.path.join(tools.config['root_path'], 'addons', 'base', 'static',
                         'img', 'res_company_logo.png'), 'rb').read())

    logo = fields.Binary(default=_get_logo, string="Company Logo", readonly=False)
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char(change_default=True)
    city = fields.Char()
    state_id = fields.Many2one("res.country.state", string='State',
                               ondelete='restrict',
                               domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string='Country',
                                 ondelete='restrict')
    ou_footer = fields.Char('OU Footer')
