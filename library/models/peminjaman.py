from odoo import models, fields, api, _


class peminjaman(models.Model):  # inherit dari Model
    _name = 'library.peminjaman'  # atribut dari class Model
    _description = 'class untuk berlatih ttg library'
    # rec_name = 'name'
   # _order = 'date desc'  # defaultnya adalah id, pengaruhnya saat list view
    # id = fields.Integer() #ini otomatis ada di odoo, akan jadi pk

    # membuat attribute field

    transaksi_id = fields.Char('Id Transaksi', size=64, required=True, index=True, readonly=True,
                          states={'draft': [('readonly', False)]})

    date = fields.Date('Tanggal ', default=fields.Date.context_today, readonly=True,
                       states={'draft': [('readonly', False)]})

    pinjam_id = fields.Many2one('res.users', 'voted by', readonly=True, ondelete='cascade',
                                default=lambda self: self.env.user)
    book_ids = fields.Many2one('library.datamaster', string='book_ids', readonly=True, ondelete="cascade",
                               states={'draft': [('readonly', False)]}, domain="[('state', '=', 'done'), ('active', '=', 'True')]")

    anggota_ids = fields.Many2one('library.anggota', string='anggota_ids', readonly=True, ondelete="cascade",
                               states={'draft': [('readonly', False)]},
                               domain="[('state', '=', 'done'), ('active', '=', 'True')]")

    vote = fields.Selection([('pengembalian', 'Pengembalian'),
                             ('peminjaman', 'Peminjaman')], 'Transaksi', required=True, readonly=False)



    state = fields.Selection([('draft', 'Draft'),  # draft--> key, secara technical yang disimpan di dbase, Draft: value yang dilihat user
                            ('confirmed', 'Confirmed'),
                            ('done', 'Done'),
                            ('canceled', 'Canceled')], 'State', required=True, readonly=True,  # krn required, sebaiknya dikasi default
                            default='draft')  # tuple di dalam list, nama field harus state spy bisa diakses oleh states
    # Description is read-only when not draft!
    description = fields.Text('Description', readonly=True, states={'draft': [('readonly', False)]})
    active = fields.Boolean('Active', default=True, readonly=True, states={'draft': [('readonly', False)]})
    confirm_date = fields.Date('Confirm date')
    total_denda = fields.Integer("Total Denda", compute="_compute_denda", store=True, default=0)

    datekembalir = fields.Date('Tanggal kembali real ', default=fields.Date.context_today, readonly=True,
                       states={'draft': [('readonly', False)]})#real
    datepinjam = fields.Date('Tanggal pinjam ', default=fields.Date.context_today, readonly=True,
                       states={'draft': [('readonly', False)]})
    datekembalid = fields.Date('Tanggal kembali dedline', default=fields.Date.context_today, readonly=True,
                               states={'draft': [('readonly', False)]}) #dedline
    _sql_constraints = [('transaksi_id_unik', 'unique(transaksi_id)', _('transaksi must be unique!'))]

    @api.depends('datekembalir', 'datekembalid')

    def _compute_denda(self):
        if self.datekembalid and self.datekembalir:
            datekembalid = fields.Datetime.from_string(self.datekembalid)
            datekembalir = fields.Datetime.from_string(self.datekembalir)
            self.total_denda = abs((datekembalir - datekembalid).days) * 15000
            if self.datekembalir <= self.datekembalid:
                self.total_denda = 0

   # def _compute_vote(self):
        #for peminjaman in self.filtered(lambda s: s.state == "done"):
           # val = {
                #"total_denda": 0,
           # }
           # for rec in peminjaman.book_ids.filtered(lambda s: s.state == "voted"):
                # lambda merupakan on the fly function dari phyton
                # s ini adalah self dari voting_ids, fungsi filtered ini akan memfilter khusus state yang bernilai voted
                # bisa pake looping, ga ush difilter. Tapi pengecekan tidak efisien
                # karena misal ada 100 data, trs hanya 2 yang canceled berarti tetep 100 pengecekan. Sedangkan filter hanya 2x saja
         #       if rec.vote == "yes":
                    #val["total_denda"] += 15000

           # peminjaman.update(val)

    def action_done(self):
        self.state = 'done'

    def action_canceled(self):
        self.state = 'canceled'

    def action_confirmed(self):
        self.state = 'confirmed'

    def action_settodraft(self):
        self.state = 'draft'
