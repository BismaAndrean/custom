from odoo import models, fields, api, _
class wizkelas(models.TransientModel):
    _name = 'wiz.toko.detail'
    _description = 'class untuk menyimpan data detail transaksi'

    deta_id = fields.Many2one('toko.detail', string='Detail transaksi')
    bar_id = fields.Many2one('toko.barang', string='Barang', ondelete="cascade")
   

    line_ids = fields.One2many('wiz.toko.detail.lines', 'wiz_header_id', string='Detail Transaksi')

    @api.model
    def default_get(self,
                    fields_list):  # ini adalah common method, semacam constructor, akan dijalankan saat create object. Ini akan meng-overwrite default_get dari parent
        res = super(wizkelas, self).default_get(fields_list)
        # res  merupakan dictionary beserta value yang akan diisi, yang sudah diproses di super class (untuk create record baru)
        res['deta_id'] = self.env.context['active_id']
        return res

    @api.onchange('deta_id')
    def onchange_deta_id(self):
        if not self.deta_id:
            return
        vals = []
        line_ids = self.env['wiz.toko.detail.lines']
        for rec in self.deta_id.line_ids:
            line_ids += self.env['wiz.toko.detail.lines'].new({
                'wiz_header_id': self.id,
                'bar_id': rec.bar_id.id,
                'ref_kelas_lines_id': rec.id
            })
            # cara membuat record baru di m2m atau o2m
        self.line_ids = line_ids

    def action_canceled(self):
        self.state = 'canceled'

    def action_confirmed(self):
        self.state = 'confirmed'

    def action_confirm(self):
        for rec in self.line_ids:
            rec.ref_kelas_lines_id.stok = rec.stok

    def action_settodraft(self):
        self.state = 'draft'

class kelas_lines_wiz(models.TransientModel):
    _name = 'wiz.toko.detail.lines'
    _description = 'class untuk menyimpan data Detail Transaksi'
    deta_id = fields.Many2one('toko.detail', string='Detail transaksi')
    wiz_header_id = fields.Many2one('wiz.toko.detail', string='Kelas')
    bar_id = fields.Many2one('toko.barang', string='Barang', ondelete="cascade")
    ref_detail_lines_id = fields.Many2one('toko.detail.lines')
    stok = fields.Integer(related='deta_id.barastock' , readonly=False)







