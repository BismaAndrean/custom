{
    'name':'library',
    'version': '1.0',
    'author': 'Andre Bisma',
    'summary': 'Modul Library SIB UK Petra',
    'description': 'Library management module',
    'category': 'Latihan',
    'website': 'http://sib.petra.ac.id',
    'depends': ['base','sales_team'],
    'data': [
        'security/ir.model.access.csv',
        'views/datamaster_views.xml',
        'views/anggota_views.xml',
        'views/peminjaman_views.xml',

    ],
    'qweb':[],
    'demo': [],
    'installable': True,
    'auto_install': False,
}