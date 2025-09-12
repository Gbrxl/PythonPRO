meme_dict = {
            "CRINGE": " Algo excepcionalmente raro o embarazoso",
            "LOL": " Una respuesta común a algo gracioso",
            "ROFL": " Una respuesta a una broma",
            "CREEPY": " aterrador, siniestro",
            "SHEESH":" ligera desaprobación",
            }
for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

    if word in meme_dict.keys():
        print('Encontraste la palabra ' + word +"! Significa" +meme_dict[word])
    else:
        print('No has encontrado la palabra, Sigue intentando!')
