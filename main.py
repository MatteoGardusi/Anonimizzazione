import json

data = json.load(open("./test_data/anonimizza_test1.json"))


def tab_utenti(input_data: dict, dst: str):
    """
    Riceve il dict dei log e resituisce una tabella che associa un nome ad un indice
    :param input_data: data log fornito
    :param dst: path del file.json di destinazione
    :return:
    """
    index_tab = {}

    for utente in range(len(data)):
        if input_data[utente][1] not in index_tab:
            index_tab[input_data[utente][1]] = len(index_tab)

    # the json file where the output must be stored
    out_file = open(dst, "w")

    json.dump(index_tab, out_file, indent=3)

    out_file.close()


tab_utenti(data, "tabella_utenti.json")
