{
    'name': 'CRM and Sales Update',
    'version': '1.0',
    'category': 'CRM Custom Modules',
    'summary': 'Created custom Module to handle updates of CRM and Sales',
    'description': """
        This modules is created for Handling updates of CRM and Sales.
    """,
    'author': 'Michael Lejano',
    'company': 'Blackpearl Technology Solutions Corporation',
    'depends': ['base','sale','crm'],  # Depends on sale and crm modules
    'data': [
        "report/quotation_template.xml",
        "report/report.xml",
    ],
    'installable': True,
    'application': True,
}
