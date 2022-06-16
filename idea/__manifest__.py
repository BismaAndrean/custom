{
    'name':'Idea',
    'version': '1.0',
    'author': 'Yulia',
    'summary': 'Modul Idea SIB UK Petra',
    'description': 'Ideas management module',
    'category': 'Latihan',
    'website': 'http://sib.petra.ac.id',
    'depends': ['base','sales_team'],
    'data': [
        'security/ir.model.access.csv',
        'views/divisi_views.xml',
        'views/voting_views.xml',
        'data/ir_sequence_data.xml',
    ],
    'qweb':[],
    'demo': [],
    'installable': True,
    'auto_install': False,
}