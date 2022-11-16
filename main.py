from argparse import ArgumentParser
from json import load, dump


def leggi_file_JSON(fname):
    # leggere il file di log fname (lista di liste di stringhe)
    fin = open(fname)
    data_to_be_read = load(fin)
    fin.close()
    return data_to_be_read


def scrivi_file_JSON(fname, data_to_be_written, indent=3):
    # salvare il file di log anonimizzato
    fout = open(fname, 'w')
    dump(data_to_be_written, fout, indent=indent)
    fout.close()


# import da riga di comando
parser = ArgumentParser(
    description="Programma che anonimizza una lista di log e salva la corrispondenza tra nomi e codici assegnati")
parser.add_argument('file_input',
                    help='Path del file da anonimizzare',
                    type=str)
parser.add_argument('-t', '--tab_output',
                    help='Path del file in cui salvare la tabella; se non indicato, il default è '
                         './results/tabella_utenti.json',
                    type=str,
                    default='./results/tabella_utenti.json')
parser.add_argument('-o', '--file_output',
                    help='Path del file in cui salvare la lista anonimizzata; se non indicato, il default è '
                         './results/log_anonimizzato.json',
                    type=str,
                    default='./results/log_anonimizzato.json')

args = parser.parse_args()

# leggere il file di log (lista di liste di stringhe)
data = leggi_file_JSON(args.file_input)


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
            index_tab[input_data[utente][1]] = f'{len(index_tab):03d}'

    # the json file where the output must be stored
    scrivi_file_JSON(dst, index_tab)


def anonimizza(tab_utenti: str, dst: str, input_data: dict):
    """
    Riceve un .json con la lista di nomi indicizzati e un .json di log e anonimizza i log salvando il risultato in dst
    :param tab_utenti: tabella con nomi utenti indicizzati
    :param dst: destinazione di salvataggi dei log anonimizzati
    :param input_data: file di log da anonimizzare
    :return:
    """
    tab_indici = load(open(tab_utenti))

    for log in range(len(input_data)):
        for item in range(len(tab_indici)):
            if input_data[log][1] == list(tab_indici.keys())[item]:
                input_data[log][1] = tab_indici[input_data[log][1]]

    scrivi_file_JSON(dst, input_data)


def elimina_utente_coinvolto(src: str):
    """
    riceve un file di log e elimina il campo "Utente coinvolto"
    :param src: path file di log
    :return:
    """
    input_data = load(open(src))
    for log in range(len(input_data)):
        del (input_data[log][2])

    scrivi_file_JSON(src, input_data)


tab_utenti(data, args.tab_output)

anonimizza(args.tab_output, args.file_output, data)

elimina_utente_coinvolto(args.file_output)
