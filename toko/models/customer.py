from odoo import models, fields, api, _


class customer(models.Model):  # inherit dari Model
    _name = 'toko.customer'  # atribut dari class Model
    _description = 'class untuk berlatih ttg Toko'
    # rec_name = 'name'
    # _order = 'date desc'

    # membuat attribute field

    name = fields.Char('Nama Customer', size=64, required=True, index=True, readonly=False)
                       # states={'draft': [('readonly', False)]})
    customer_id = fields.Char('Id Customer', size=64, required=True, index=True, readonly=False)
                          # states={'draft': [('readonly', False)]})
    member = fields.Char('Membership? :', size=64, required=True, index=True, readonly=False)
                     # states={'draft': [('readonly', False)]})

    date = fields.Date('Date Release', default=fields.Date.context_today, readonly=False)
                       # states={'draft': [('readonly', True)]})

    transaksi_ids1 = fields.One2many('toko.transaksi', 'custo_id', string='Votes')

    state = fields.Selection([('draft', 'Draft'),  # draft--> key, secara technical yang disimpan di dbase, Draft: value yang dilihat user
                            ('confirmed', 'Confirmed'),
                            ('done', 'Done'),
                            ('canceled', 'Canceled')], 'State', required=True, readonly=True,  # krn required, sebaiknya dikasi default
                            default='draft')  # tuple di dalam list, nama field harus state spy bisa diakses oleh states
    # Description is read-only when not draft!
    description = fields.Text('Description', readonly=True, states={'draft': [('readonly', False)]})
    active = fields.Boolean('Active', default=True, readonly=True, states={'draft': [('readonly', False)]})
    confirm_date = fields.Date('Confirm date')




    _sql_constraints = [('name_unik', 'unique(divisi_id)', _('divisi_id must be unique!'))]
    def action_done(self):
        self.state = 'done'

    def action_canceled(self):
        self.state = 'canceled'

    def action_confirmed(self):
        self.state = 'confirmed'

    def action_settodraft(self):
        self.state = 'draft'




