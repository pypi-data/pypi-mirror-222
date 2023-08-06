{
    'name': "sm_crm_donations",

    'summary': """""",

    'description': """""",

    'author': "Som Mobilitat",
    'website': "https://www.sommobilitat.coop",

    'category': 'vertical-cooperative',
    'version': '12.0.0.0.2',

    'depends': ['base', 'vertical_carsharing', 'crm', 'crm_metadata'],

    'data': [
        'data/utm_source_data.xml',
        'data/crm_team_data.xml',
        'data/crm_stage_data.xml',
        'views/crm_lead_views.xml',
    ],

    'demo': [

    ],
    'application': True,
}
