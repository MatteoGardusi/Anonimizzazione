# Anonimizzazione di un file di log

Scrivere un programma Python che legge una lista di log dal file “anonimizza_test1.json” . 

Ciascun elemento della lista di log è costituito dalle seguenti 9 informazioni:

- Data/Ora,
- Nome completo dell'utente
- Utente coinvolto
- Contesto dell'evento
- Componente
- Evento
- Descrizione
- Origine
- Indirizzo IP

Il programma deve anonimizzare la lista. In particolare:
- per ogni utente (campo “Nome completo dell'utente”) generare un identificatore unico (per esempio un numero progressivo) 
- sostituire nel log l’identificatore unico al nome dell’utente
- generare una tabella che mantiene l’informazione di quale identificatore è stato associato a ciascun utente (tabella che associa il nome dell'utente al codice unico a lui associato)
- eliminare da tutti i log il campo “Utente coinvolto”, che normalmente contiene la stringa “-“, ma potrebbe contenere anch’esso il nome dell’utente

Il programma infine deve salvare la lista di log anonimizzata nello stesso formato di partenza (json) e la tabella che associa ciascun utente al suo identificatore unico (anche la tabella va salvata in forato json). Il file di log anonimizzato va salvato come lista di log, e ciascun log come una lista di informazioni. 

# Modifiche da fare

Introduzione di sottoprogrammi.
I sottoprogrammi dovrebbero essere definiti in modo tale che sia facile successivamente integrare nella soluzione i seguenti miglioramenti:

- Generare identificatori anomimi degli utenti in un formato migliore (per es. un codice di lunghezza fissa)
- Ridurre dipendenze dai path dei file (per es. usare parametri da linea di comando)
- Poter anonimizzare un secondo file di log, e per gli stessi utenti voler usare gli stessi ID. Come si può generalizzare la soluzione?
- Poter effettuare la de-anonimizzazione (cioè partendo da un file anonimizzato ripristinare i nomi reali degli utenti)


