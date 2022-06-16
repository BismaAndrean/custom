from odoo import models, fields, api, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    discount = fields.Float(string='discount', digits='Discount', default=0.0)


    # discount = fields.Selection([('draft','Draft'),('approved','Approved'),('done','Done')],string="status",default="draft")

    # discount = fields.Char('discount', size=64, required=True, index=True, readonly=False,ondelete='cascade',
    #                       states={'draft': [('readonly', False)]})

    # status2 = fields.Monetary(string='status2', ondelete='cascade')




    # discount = fields.Float('discount', index=True, required=True, translate=True)