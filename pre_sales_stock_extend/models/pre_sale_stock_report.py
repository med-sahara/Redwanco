from odoo import models, fields, api, _

import qrcode

try:
    import base64
except ImportError:
    base64 = None
from io import BytesIO


class StockPickingForm(models.Model):
    _inherit = 'stock.picking'
    _description = "Delivery Agents in stock picking"

    delivery_line = fields.Many2one('delivery.line', string='Delivery Lines')
    qr = fields.Binary(string="QR Code")

    @api.onchange('partner_id')
    def onchange_partner(self):
        delivery_line = self.env['delivery.line'].search(
            [('delivery_line', 'in', self.partner_id.zone.id)])
        delivery_agent = self.env['delivery.agent'].search(
            [('related_delivery_line', 'in', delivery_line.ids)])
        domain = {'agent_id': [('id', 'in', delivery_agent.ids)]}
        return {'domain': domain}

    def create(self, vals_list):
        res = super(StockPickingForm, self).create(vals_list)
        res['qr'] = self.generate_qr(res['name'])
        return res

    def generate_qr(self, reference):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(reference)
        qr.make(fit=True)

        img = qr.make_image()
        temp = BytesIO()
        img.save(temp, format="PNG")
        qr_image = base64.b64encode(temp.getvalue())
        return qr_image





