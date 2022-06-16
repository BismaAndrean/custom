from odoo import models, fields, api, _


class pegawai(models.Model):  # inherit dari Model
    _name = 'toko.pegawai'  # atribut dari class Model
    _description = 'class untuk berlatih ttg Toko'
    # rec_name = 'name'
    # _order = 'date desc'

    # membuat attribute field

    name = fields.Char('Nama Pegawai', size=64, required=True, index=True, readonly=False)
                       # states={'draft': [('readonly', True)]})
    pegawai_id = fields.Char('Id Pegawai', size=64, required=True, index=True, readonly=False)
                          # states={'draft': [('readonly', True)]})
    divi_id = fields.Many2one('toko.divisi', string='divisi', readonly=True, ondelete="cascade",
                              # states={'draft': [('readonly', False)]},
                              domain="[('state', '=', 'done'), ('active', '=', 'True')]")

    date = fields.Date('Date Release', default=fields.Date.context_today, readonly=True,
                       states={'draft': [('readonly', True)]})

    transaksi_ids = fields.One2many('toko.transaksi', 'pega_id', string='Votes')

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


