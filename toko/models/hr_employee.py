from odoo import models, fields, api, _

class hr_employee(models.Model):
    _inherit = 'hr.employee'
    gaji = fields.Char('gaji', size=64, required=True, index=True, readonly=False)
    # states={'draft': [('readonly', False)]})

    # discount = fields.Selection([('draft','Draft'),('approved','Approved'),('done','Done')],string="status",default="draft")

    # discount = fields.Char('discount', size=64, required=True, index=True, readonly=False,ondelete='cascade',
    #                       states={'draft': [('readonly', False)]})

    # status2 = fields.Monetary(string='status2', ondelete='cascade')




    # discount = fields.Float('discount', index=True, required=True, translate=True)