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


def anonimizza(tab_utenti: str, dst: str, input_data: dict):
    """
    RIceve un .json con la lista di nomi indicizzati e un .json di log e anonimizza i log salvando il risultato in dst
    :param tab_utenti: tabella con nomi utenti indicizzati
    :param dst: destinazione di salvataggi dei log anonimizzati
    :param input_data: file di log da anonimizzare
    :return:
    """
    tab_indici = json.load(open(tab_utenti))

    for log in range(len(input_data)):
        for item in range(len(tab_indici)):
            if input_data[log][1] == list(tab_indici.keys())[item]:
                input_data[log][1] = tab_indici[input_data[log][1]]

    out_file = open(dst, "w")

    json.dump(data, out_file, indent=3)

    out_file.close()


tab_utenti(data, "tabella_utenti.json")
anonimizza("tabella_utenti.json", "log_anonimizzato.json", data)