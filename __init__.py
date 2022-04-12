from albert import *
from os import path

__title__ = "PHP docs"
__version__ = "0.4.0"
__triggers__ = "php "
__authors__ = "pkboom"

icon = "{}/icon.png".format(path.dirname(__file__))
search_icon = "{}/search.png".format(path.dirname(__file__))

def handleQuery(query):
    if not query.isTriggered or not query.isValid:
        return
        
    items = []

    items.append(Item(
        id='search',
        icon=search_icon,
        text = "Search {}".format(query.string.strip()),
        actions=[UrlAction(
            text='This action opens google chrome.', 
            url="https://www.google.com/search?q=php {}".format(query.string.strip())
        )],
    ))

    items.append(Item(
        id='php doc',
        icon=icon,
        text = "PHP {}".format(query.string.strip()),
        actions=[UrlAction(
            text='This action opens php docs.', 
            url='https://www.php.net/{}'.format(query.string.strip())
        )],
    ))

    return items
