# Blog Django - Progetto Sviluppo Web App

## Descrizione
Questa è una web application di tipo Blog sviluppata con Django e database SQLite. Permette di creare, visualizzare, modificare ed eliminare post, con interfaccia responsive e moderna.

## Funzionalità implementate
- **Create:** aggiunta di nuovi post tramite admin o form
- **Read:** visualizzazione della lista dei post in homepage
- **Update:** modifica dei post esistenti
- **Delete:** eliminazione dei post
- **Gestione immagini:** ogni post può avere un'immagine
- **Editor avanzato:** integrazione con Django Summernote per la formattazione dei contenuti

## Struttura del progetto
- `blog/` - codice applicativo Django
- `templates/` - template HTML
- `static/` - file CSS e risorse statiche
- `media/` - immagini caricate
- `db.sqlite3` - database SQLite
- `requirements.txt` - dipendenze Python

## Istruzioni per avviare l'applicazione
1. Installa le dipendenze:
   ```powershell
   pip install -r requirements.txt
   ```
2. Avvia il server Django:
   ```powershell
   python manage.py runserver
   ```
3. Apri il browser su `http://127.0.0.1:8000/`

## Note
- Puoi gestire i post anche tramite l'admin Django (`/admin`).
- Il database è già inizializzato e contiene la struttura necessaria.
- Per allegare immagini ai post, assicurarsi che la cartella `media/` sia presente.

## Screenshot
### Homepage
![Homepage](Screenshot%202025-11-21%20181917.png)
### Dettaglio post
![Dettaglio post](Screenshot%202025-11-21%20181929.png)


