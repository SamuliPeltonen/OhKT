import http_pyynto


def ryhmittele_toimipaikoittain(numero_sanakirja):
    paikat = {}
    for numero, nimi in numero_sanakirja.items():
        if nimi not in paikat:
            paikat[nimi] = []
        paikat[nimi].append(numero)

    return paikat



def main(kaupunki):
    postinumerot = http_pyynto.hae_postinumerot()
    toimipaikat = ryhmittele_toimipaikoittain(postinumerot)
    #Mikäli parametria ei ole annettu, kysytään se inputilla
    if(len(kaupunki)<1):
        toimipaikka = input('Kirjoita postitoimipaikka: ').strip().upper()
    #Mikäli parametri on annettu mm. testin yhteydessä, ei kaupunkia pyydetä enää inputilla lainkaan
    else:
        toimipaikka = kaupunki
    toimipaikka = toimipaikka.replace(" ", "")
    if toimipaikka in toimipaikat:
        toimipaikat[toimipaikka].sort()

        loydetyt_str = ', '.join(toimipaikat[toimipaikka])
        print('Postinumerot: ' + loydetyt_str)
        return toimipaikat[toimipaikka]
    else:
        print('Toimipaikkaa ei löytynyt')
        return []
if __name__ == '__main__':
    main("")

