from odoo import api, fields, models


class OperationalUnitTypology(models.Model):
    _inherit = 'sale.order.type'
    _description = 'Operational unit in sale order type'

    operating_unit_id = fields.Many2one('operating.unit',
                                        string='Operating Unit')


class SaleOperationalUnit(models.Model):
    _inherit = 'sale.order'
    _description = 'Onchange in Operational unit in sale order type'

    @api.multi
    @api.onchange('type_id')
    def onchange_type_id(self):
        for order in self:
            order.operating_unit_id = order.type_id.operating_unit_id.id
        res = super(SaleOperationalUnit, self).onchange_type_id()
        return res


class AccountOperationalUnit(models.Model):
    _inherit = 'account.invoice'
    _description = 'Onchange in Operational unit in invoice order type'

    @api.onchange('sale_type_id')
    def onchange_sale_type_id(self):
        if self.sale_type_id.operating_unit_id:
            self.operating_unit_id = self.sale_type_id.operating_unit_id.id
        res = super(AccountOperationalUnit, self).onchange_sale_type_id()
        return res
