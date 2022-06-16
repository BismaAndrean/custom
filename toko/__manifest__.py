{
    'name':'Toko',
    'version': '1.0',
    'author': 'Andre Bisma',
    'summary': 'Modul Toko SIB UK Petra',
    'description': 'Ideas management module',
    'category': 'Latihan',
    'website': 'http://sib.petra.ac.id',
    'depends': ['base','sales_team'],
    'data': [
        'security/ir.model.access.csv',
        'views/divisi_views.xml',
        'views/pegawai_views.xml',
        'views/customer_views.xml',
        'views/transaksi_views.xml',
        'views/barang_views.xml',
        'views/detail_views.xml',
        'views/product_views.xml',
        'views/hr_employee_views.xml',
        'wizard/wiz_toko_detail.xml',
    ],
    'qweb':[],
    'demo': [],
    'installable': True,
    'auto_install': False,
}