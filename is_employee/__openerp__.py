{
    'name' : 'is_employee field',
    'version' : '1.0.0',
    'author' : 'Ivan Yelizariev',
    'category' : 'Sale',
    'website' : 'https://it-projects.info',
    'description': """
Adds is_employee to res.users and res.partner

Shows "Related employees" in res.users 

Shows "Related employee" in res.partner 

Tested on 8.0 ab7b5d7
    """,
    'depends' : ['hr'],
    'data':['views.xml'],
    'installable': True
}