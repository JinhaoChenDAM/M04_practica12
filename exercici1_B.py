import json


# creem un json com si fos String
def creaJson():
    datas = """
        {
        "book":[
            {"title":"Flors per l'Àlgernon",
            "cover":"Blanda",
            "year":"2016",
            "pages":"273"
            },
            {"title":"El juego de Ender",
            "cover":"Dura",
            "year":"2003",
            "pages":"392"
            },
            {"title":"Harry Potter",
            "cover":"Dura",
            "year":"1997",
            "pages":"445"
            },   
            {"title":"Clean Code",
            "cover":"Blanda",
            "year":"2019",
            "pages":"230"
            }
        ]
    """
    # Creem un document amb el nom arxiuJson
    with open("arxiu.json", 'w') as fileW:
        json.dump(datas, fileW)
    print(datas)


# imprimim per pantalla el json
def imprimirJson():

    with open("arxiu.json", 'r') as fileR:
        resultat = json.load(fileR)
        print(resultat)