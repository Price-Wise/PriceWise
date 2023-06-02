import eel

items = [
    {
        "name": "WATCH 1/ TSP-W01 TECNO WATCH 1 BLACK ( BUY ONE GET ONE ...",
        "price": "39 JOD",
        "store": "Smartbuy",
        "url": "/smartbuystore/en/Smart-Tech/Mobile-%26-Tablets/Smart-Mobile/TECNO/WATCH-1-TSP-W01-TECNO-WATCH-1-BLACK-%28-BUY-ONE-GET-ONE-FREE-%29/p/TMO0711ST0015",
        "imageURL": "/smartbuystore/medias/TMO0711ST0015.jpg?context=c21hcnRidXliMmN8aW1hZ2VzfDIwNDc5fGltYWdlL2pwZWd8aW1hZ2VzL2gyYy9oNzIvODg3NjE2NDU0NjU5MC9UTU8wNzExU1QwMDE1LmpwZ3wwY2IwM2Y2NTQ0OGYwN2Q2MTI5ZTg1NDg0ZThlMjIwYmU0ZmIwYmRlNzNiNWU5NGZhYmY2YzVjYzNiODAxZDUy",
        "description": "",
    },
    {
        "name": "TSP-W02TECNO Watch 2 | Type : Smart Watch | Color : Bla...",
        "price": "44 JOD",
        "store": "Smartbuy",
        "url": "https://smartbuy-me.com/smartbuystore/en/Wareable-Accessories/TSP-W02TECNO-Watch-2-%7C-Type-%3A-Smart-Watch-%7C-Color-%3A-Black-%7C-Additional-info-%3A-Smartwatch-%7C-warranty-%3A-1/p/TMO0701ST0112",
        "imageURL": "https://smartbuy-me.com/smartbuystore/medias/TMO0701ST0112.jpg?context=c21hcnRidXliMmN8aW1hZ2VzfDg4MDR8aW1hZ2UvanBlZ3xpbWFnZXMvaDJiL2hjZi84ODc2MTY3NjkyMzE4L1RNTzA3MDFTVDAxMTIuanBnfGRkYmI0OWU4YjI3Y2I5NjhiMzUwNDA2YWQyOGJhZDA3ZGFmYjI4YjM2MTk5YTEwNzJiM2Q4MTQxNTFkMTQ2OGI",
        "description": "",
    },
    {
        "name": "HUAWEI Watch GT 3 SE | Type : Wearable | Color : Black ...",
        "price": "",
        "store": "Smartbuy",
        "url": "https://smartbuy-me.com/smartbuystore/en/Wareable-Accessories/HUAWEI-Watch-GT-3-SE-%7C-Type-%3A-Wearable-%7C-Color-%3A-Black-%7C-Additional-info-%3A-Smart-Watch-%7C-warranty-%3A-One-warranty/p/CAV0711ST0063",
        "imageURL": "https://smartbuy-me.com/smartbuystore/medias/CAV0711ST0063.jpg?context=c21hcnRidXliMmN8aW1hZ2VzfDIxODg3fGltYWdlL2pwZWd8aW1hZ2VzL2hkNi9oNDIvODg2ODQ0ODczMTE2Ni9DQVYwNzExU1QwMDYzLmpwZ3xiM2FjMDU1N2QxM2U2MGM2MzFmOGM0MjI0ODUyNzZkYjAxZmQzZDcxMWM4YjE3ODA1MzgyZTY2ODg2ZDc5Mzlk",
        "description": "",
    },
    {
        "name": "HUAWEI Watch GT 3 SE | Type : Wearable | Color : Grey |...",
        "price": "",
        "store": "Smartbuy",
        "url": "https://smartbuy-me.com/smartbuystore/en/Wareable-Accessories/HUAWEI-Watch-GT-3-SE-%7C-Type-%3A-Wearable-%7C-Color-%3A-Grey-%7C-Additional-info-%3A-Smart-Watch-%7C-warranty-%3A-One-warranty/p/CAV0711ST0064",
        "imageURL": "https://smartbuy-me.com/smartbuystore/medias/CAV0711ST0064.jpg?context=c21hcnRidXliMmN8aW1hZ2VzfDIyMDY0fGltYWdlL2pwZWd8aW1hZ2VzL2g3Zi9oNDIvODg2ODQ0ODc2MzkzNC9DQVYwNzExU1QwMDY0LmpwZ3wxZDMwOWYyYjRlM2U2ODFkOTY1MmJiYTdmYzRkNGIyNzU0Yjk3OWQ3NGM0ZjY0NTVhMmNmMzQ2ODJlZTkxOWMw",
        "description": "",
    },
]

# Initialize Eel
eel.init("UI/web")

@eel.expose
def get_items():
    return items

# Start the web application
eel.start("search_card/filters_list.html", size=(800, 600))


# import eel

# # Initialize Eel
# eel.init('UI/web')



# # Start the Eel application
# eel.start('search_card/filters_list.html', size=(800, 600))

