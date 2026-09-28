RFC 2460
Numero di indirizzi maggiore [2^128 > 2^32]
DHCP deprecato
Unique-local deprecato

Obiettivi per passare da IPv4 a IPv6
- Supportare miliardi di host anche con un'allocazione di indirizzi inefficiente
- Ridurre la dimensione delle tabelle di routing
- Semplificare i protocolli per permettere ai router di elaborare i pacchetti più velocemente
- Fornire un grado di sicurezza maggiore (autenticazione e privacy)
- Prestare più attenzione al tipo di servizio, in particolare in tempo reale
- Aumentare il multicasting permettendo di specificare l'univocità degli indirizzi
- Permettere a un host di spostarsi senza cambiare indirizzo
- Permettere al protocollo di evolvere nel futuro
- Permettere al protocollo vecchio e al nuovo di coesistere

Miglioramenti rispetto all'IPv4
- Fornisce un numero di indirizzi pressoché illimitato [2^128]
- Semplifica l'intestazione dell'header; contiene solo 7 campi anziché 13 dell'IPv4, quindi il router può elaborare i pacchetti piu velocemente migliorando throughput e ritardo
- Supporta meglio le opzioni: i campi obbligatori sono ora opzionali e sono rappresentati in modo da rendere più semplice non considerare le opzioni se non è necessario; riduce il tempo di elaborazione dei pacchetti
- Migliorare autenticazione e privacy
- Maggiore attenzione alla qualità del servizio
