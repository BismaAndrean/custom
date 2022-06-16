from odoo import models, fields, api, _


class detail(models.Model):  # inherit dari Model
    _name = 'toko.detail'  # atribut dari class Model
    _description = 'class untuk berlatih ttg Toko'
    # rec = 'name'
    # _order = 'date desc'

    # membuat attribute field

    # name = fields.Char('Nama Pegawai', size=64, required=True, index=True, readonly=False)
    #                    # states={'draft': [('readonly', True)]})



    detail_id = fields.Char('Id detail', size=64, required=True, index=True, readonly=False)
                          # states={'draft': [('readonly', True)]})

    barastock = fields.Integer('Stock', size=64, required=True, index=True, readonly=False)
                         # states={'draft': [('readonly', False)]})
    baraprice = fields.Integer('Price', size=64, required=True, index=True, readonly=False)
                         # states={'draft': [('readonly', False)]})
    subtotal = fields.Integer('total', size=64, required=True, index=True, readonly=False)
                         # states={'draft': [('readonly', False)]})
    total = fields.Integer('subtotal', size=64, required=True, index=True, readonly=False)
    # states={'draft': [('readonly', False)]})
    totalprice = fields.Integer('Subtotal', size=64, required=True, index=True, readonly=False)
    # states={'draft': [('readonly', False)]})
    #ngmbildata
    trans_id = fields.Many2one('toko.transaksi', string='transaksi', readonly=False, ondelete="cascade",
                              # states={'draft': [('readonly', False)]},
                              domain="[('state', '=', 'done'), ('active', '=', 'True')]")
    bara_id = fields.Many2one('toko.barang', string='barang', readonly=False, ondelete="cascade",
                               # states={'draft': [('readonly', False)]},
                               domain="[('state', '=', 'done'), ('active', '=', 'True')]")

    date = fields.Date('Date Release', default=fields.Date.context_today, readonly=True,
                       states={'draft': [('readonly', True)]})

    # bara_id = fields.Many2one('toko.barang', string='barang', readonly=True, ondelete="cascade",
    #                           # states={'draft': [('readonly', False)]},
    #                           domain="[('state', '=', 'done'), ('active', '=', 'True')]")

    state = fields.Selection([('draft', 'Draft'),  # draft--> key, secara technical yang disimpan di dbase, Draft: value yang dilihat user
                            ('confirmed', 'Confirmed'),
                            ('done', 'Done'),
                            ('canceled', 'Canceled')], 'State', required=True, readonly=True,  # krn required, sebaiknya dikasi default
                            default='draft')  # tuple di dalam list, nama field harus state spy bisa diakses oleh states
    # Description is read-only when not draft!
    description = fields.Text('Description', readonly=True, states={'draft': [('readonly', False)]})
    active = fields.Boolean('Active', default=True, readonly=True, states={'draft': [('readonly', False)]})
    confirm_date = fields.Date('Confirm date')

    line_ids = fields.One2many('toko.detail.lines', 'deta_id', string='Detail Transaksi', readonly=True,
                               states={'draft': [('readonly', False)]})

    _sql_constraints = [('name_unik', 'unique(divisi_id)', _('divisi_id must be unique!'))]
    def action_done(self):
        self.state = 'done'

    def action_canceled(self):
        self.state = 'canceled'

    def action_confirmed(self):
        self.state = 'confirmed'

    def action_settodraft(self):
        self.state = 'draft'

    @api.onchange('bara_id','barastock')
    def func_onchange_bara_id(self):
        if not self.bara_id:
            return {}
        else:
            self.baraprice = self.bara_id.price
            self.totalprice = self.barastock * self.bara_id.price
            self.subtotal = self.subtotal + self.totalprice
        return {}

    def action_wiz_detail(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Wizard Toko Detail'),
            'res_model': 'toko.detail.lines',
            'view_mode': 'form',
            'target': 'new',
            'context': {'active_id': self.id},
        }

    class detail_lines(models.Model):
        _name = 'toko.detail.lines'
        _description = 'class untuk mengupdate data detail transaksi'

        deta_id = fields.Many2one('toko.detail', string='Detail transaksi', ondelete="cascade")
        bar_id = fields.Many2one('toko.barang', string='Barang', ondelete="cascade")
        stok = fields.Integer(related='deta_id.barastock',readonly=False)
        # states={'draft': [('readonly', False)]})
        _sql_constraints = [('name_unik', 'unique(kelas_id, mhs_id)', _('The student is already exist!'))]
