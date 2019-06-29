from odoo import models, fields, api, _


class SalesTeam(models.Model):
    _inherit = 'crm.team'
    _description = "Sales Agents in Sales Team"

    agent_ids = fields.Many2many('sales.agent', string='Sales Agents')


class SaleOrderAgent(models.Model):
    _inherit = 'sale.order'
    _description = "Sales Agents in Sales Order"

    agent_id = fields.Many2one('sales.agent', string='Sales Agent')

    @api.multi
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        """Show sales agent based on customer zone"""

        commercial_line = self.env['commercial.line'].search([('commercial_line', 'in', self.partner_id.zone.id)])
        sales_agent = self.env['sales.agent'].search([('related_commercial_line', 'in', commercial_line.ids)])
        domain = {'agent_id': [('id', 'in', sales_agent.ids)]}
        return {'domain': domain}


class AccountinvoiceInherit(models.Model):
    _inherit = 'account.invoice'
    _description = "Sales Agent in invoice"

    agent_id = fields.Many2one('sales.agent', string='Sales Agent')

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        """Show sales agent in Invoice form"""
        commercial_line = self.env['commercial.line'].search(
            [('commercial_line', 'in', self.partner_id.zone.id)])
        sales_agent = self.env['sales.agent'].search(
            [('related_commercial_line', 'in', commercial_line.ids)])
        domain = {'agent_id': [('id', 'in', sales_agent.ids)]}
        return {'domain': domain}

    @api.model
    def create(self, vals_list):
        res = super(AccountinvoiceInherit, self).create(vals_list)
        if res.refund_invoice_id:
            res.agent_id = res.refund_invoice_id.agent_id.id \
                if res.refund_invoice_id.agent_id else None
        return res


class SaleOrderInvoice(models.Model):
    _inherit = 'sale.order'
    _description = "Sale Order inherit to add agent"

    @api.multi
    def _prepare_invoice(self):
        res = super(SaleOrderInvoice, self)._prepare_invoice()
        res.update({
            'agent_id': self.agent_id.id
        })
        return res


class SaleReportExtend(models.Model):
    _inherit = 'sale.report'
    _description = "Sale Agent in sales report"

    agent_id = fields.Many2one('sales.agent', string='Sales Agent', readonly=True)

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['agent_id'] = ', s.agent_id as agent_id'

        groupby += ', s.agent_id'
        return super(SaleReportExtend, self)._query(with_clause, fields, groupby, from_clause)


class PaymentForm(models.Model):
    _inherit = 'account.payment'
    _description = "Sale Agent in payment form"

    agent_id = fields.Many2one('sales.agent',string='Sales Agent')


class PaymentFormWizard(models.AbstractModel):
    _inherit = 'account.abstract.payment'
    _description = "Sales Agent in Payment"

    agent_id = fields.Many2one('sales.agent', string='Sales Agent')

    @api.model
    def default_get(self, fields):
        active_ids = self._context.get('active_ids')
        invoices = self.env['account.invoice'].browse(active_ids)
        res = super(PaymentFormWizard, self).default_get(fields)
        res.update({
            'agent_id': invoices.agent_id.id
        })
        return res








