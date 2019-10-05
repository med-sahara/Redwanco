from odoo import api, fields, models


class SalesTeamSalesType(models.Model):
    _inherit = 'sale.order.type'
    _description = 'Sales Team in sale order type'

    sales_team_id = fields.Many2one('sale.order',string='Sales Team')


class SaleTeam(models.Model):
    _inherit = 'sale.order'
    _description = 'Onchange in Sales Team onchange sale order type'

    @api.multi
    @api.onchange('type_id')
    def onchange_type_id(self):
        for order in self:
            order.team_id = order.type_id.sales_team_id.id
        res = super(SaleTeam, self).onchange_type_id()
        return res

