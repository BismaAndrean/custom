from odoo import models, fields, api, _


class datamaster(models.Model):  # inherit dari Model
    _name = 'library.datamaster'  # atribut dari class Model
    _description = 'class untuk berlatih ttg library'
    # rec_name = 'name'
   # _order = 'date desc'  # defaultnya adalah id, pengaruhnya saat list view
    # id = fields.Integer() #ini otomatis ada di odoo, akan jadi pk

    # membuat attribute field
    name = fields.Char('Nama Buku', size=64, required=True, index=True, readonly=True,
                       states={'draft': [('readonly', False)]})
    book_id = fields.Char('Id Buku', size=64, required=True, index=True, readonly=True,
                          states={'draft': [('readonly', False)]})

    date = fields.Date('Date Release', default=fields.Date.context_today, readonly=True,
                       states={'draft': [('readonly', False)]})
    stock = fields.Integer('Stock', size=64, required=True, index=True, readonly=True,
                           states={'draft': [('readonly', False)]})
    state = fields.Selection([('draft', 'Draft'),  # draft--> key, secara technical yang disimpan di dbase, Draft: value yang dilihat user
                            ('confirmed', 'Confirmed'),
                            ('done', 'Done'),
                            ('canceled', 'Canceled')], 'State', required=True, readonly=True,  # krn required, sebaiknya dikasi default
                            default='draft')  # tuple di dalam list, nama field harus state spy bisa diakses oleh states
    # Description is read-only when not draft!
    description = fields.Text('Description', readonly=True, states={'draft': [('readonly', False)]})
    active = fields.Boolean('Active', default=True, readonly=True, states={'draft': [('readonly', False)]})
    confirm_date = fields.Date('Confirm date')


    pinjam_idsa = fields.One2many('library.peminjaman', 'book_ids', string='Votes')

    confirm_partner_id = fields.Many2one('res.partner', 'Confirm By', readonly=True)
    # Ketambahan voting_ids supaya bs ambil dari votings.py, s -> ditambahin karena penamaan default di odoo 1:M
    voting_ids = fields.One2many('idea.voting', 'idea_id', string='Votes')
    total_yes = fields.Integer("Yes", compute="_compute_vote", store=True, default=0)
    total_no = fields.Integer("No", compute="_compute_vote", store=True, default=0)
    total_abstain = fields.Integer("Abstain", compute="_compute_vote", store=True, default=0)

    score = fields.Integer('Score', default=0, readonly=True)
    # sponsor_ids = fields.Many2many('res.partner', 'idea_idea_res_partner_rel', 'idea_idea_id', 'res_partner_id', 'Sponsors')
    sponsor_ids = fields.Many2many('res.partner', string='Sponsors')
    owner = fields.Many2one('res.partner', 'Owner', index=True, readonly=True, states={'draft': [('readonly', False)]})
    _sql_constraints = [('book_id_unik', 'unique(book_id)', _('book id must be unique!'))]


    # function api ini dijalankan:
    # 1. Tiap kali ada new record refer to voting_ids
    # 2. Tiap kali ada radio button vote pada voting.py berubah (yes, no, abstain)
    # 3. Tiap kali state pada voting.py berubah (canceled, settodraft, confirmed)



    def action_done(self):
        self.state = 'done'

    def action_canceled(self):
        self.state = 'canceled'

    def action_confirmed(self):
        self.state = 'confirmed'

    def action_settodraft(self):
        self.state = 'draft'
