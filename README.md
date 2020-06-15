# GGSpoofer

Program stworzony **bardzo dawno temu** w celu wykorzystywania luk w botach na GG.
Zasada działania jest bardzo prosta i opisana w sekcji **Zrzuty ekranu**.

## Zrzuty ekranu
![Główne okno](https://i.imgur.com/GTIq0y9.png)
![Informacje](https://i.imgur.com/2DgFzqd.png)
![Konferencje](https://i.imgur.com/KQxf3Ba.png)
![Okno rozmowy](https://i.imgur.com/AcuxxDs.png)
![Widok z GG](https://i.imgur.com/CGBHYBq.png)
![Okno drugiej metody](https://i.imgur.com/ooxkPl8.png)
![Opis drugiej metody](https://i.imgur.com/AlgJqHw.png)
![Okno pomocy drugiej metody](https://i.imgur.com/SG4Vrjv.png)

## FAQ

### Jak znaleźć cel?

Znalezienie odpowiedniego bota do ataków programem GG Spoofer nie zawsze jest takie proste, jakie mogło by się wydawać. Przecież największą wadą tego programu jest to, że do prawie wszystkiego wymagany jest adres URL do pliku PULL bota. Nie ma chyba konkretnych kryteriów, w jakich można szukać celów.

### Jak zdobyć wymagany adres URL pliku PULL bota?

Jeśli jest to nasz bot, wystarczy... No właśnie. Jeśli ktoś posiada własnego bota, a nie zna swej domeny, do której podłączony jest bot, to można tylko pogratulować.

Ale jeśli to nie jest nasz bot, to jest kilka sposobów, by taki adres zdobyć:

- zapytać administratora, może poda 😉
- szukać uszkodzonych funkcji/komend które wywalają błędy (w ten sposób dostaniemy tylko ścieżkę do pliku bota, nie domenę)
- zgadywać, np. popularne hostingi na których stawia się boty to Hostinger, Hekko itd... więc wystarczy próbować łączyć nazwę czatu ze standardową domeną serwowaną przez dany hosting, np. *zajebistyczat.hol.es* (hol.es należy do Hostinger'a), później możemy tak samo zgadywać ze ścieżką do pliku
- użyć super-ultra-tajnej techniki manipulacji, by omamić niedoświadczonego "skryptera", np. coś w stylu *ej, podasz mi dla testów adres pliku bota? Nic nie zrobię, jest zabezpieczenie, nie mam dostępu*
- szukać jakiegoś forum bota/czatu z nadzieją, że jest ono postawione na tym samym serwerze, co bot (w ten sposób uzyskamy tylko domenę)
- grzebać w archiwum rozmów z botem, czasami tam znajdują się takie perełki jak adres pliku 😁
- użyć metody phishingowej do wyłudzenia adresu pliku lub konta skryptera (wtedy to już nawet nie musimy się bawić z GG Spooferem 😅)
- użyć programu do rekursywnego szukania katalogów na stronach internetowych (jeśli mamy domenę)
- próbować wsztrzykiwać kod PHP lub SQL do niektórych komend na czacie z nadzieją, że wypluje nam błąd lub coś więcej

### Jak wyglądają zabezpieczenia w bocie?

GG Spoofer do ataków wykorzystuje trzy luki w botach na GG.

Pierwsza luka to niezabezpieczenie bota przed wysyłaniem żądań z innych adresów IP niż Botmaster (91.197.15.34).

Druga luka to niezabezpieczenie bota przed wysyłaniem żądań z User-agenta "GG PeekBot".

A trzecia luka to... W zasadzie to po prostu podatność bota na dodanie do konferencji, przez co dzięki pewnemu trikowi możemy nawet **globalnie zbanować samego administratora** na jakimś czacie. Wszystko jest opisane w GG Spooferze.

Linijka w kodzie łatająca pierwszą lukę najczęściej wygląda tak:

```php
if(!preg_match('/91\.((197\.1[2-5])|(214\.23[6-9]))\.[0-9]{1,3}/', $_SERVER['REMOTE_ADDR'])) die();
```

Natomiast linijka w kodzie łatająca druga lukę wygląda tak:
```php
if(strpos($_SERVER['HTTP_USER_AGENT'], "GG PeekBot") === 0) die();
```

Trzecią lukę na chwilę obecną można załatać jedynie wyłączając filtr antyreklamowy na czacie, co jest mało bezpieczne, bo tym samym narażamy się na reklamowanie innych czatów na naszym.

### Jak sprawdzić, czy nasz cel jest zabezpieczony?
No jak to, jak... 😣

Odpal GG Spoofera, wpisz wymagane dane, otwórz konwersację i napisz coś do bota. Jeśli bot odpowie coś w stylu "ACCESS DENIED!", "Brak dostępu" lub przekieruje nas do innej strony (błąd HTTP 301) to znaczy, że jest zabezpieczony.
Na szczęście (lub na nieszczęście) zabezpieczenie przed drugą luką jest rzadziej używane.

By sprawdzić, czy cel jest zabezpieczony przed trzecią luką, wystarczy zapytać (jeśli jest to czat): *ej, jest tutaj zabezpieczenie przed reklamowaniem?*. Jeśli uzyskamy odpowiedź **twierdzącą**, to nasz cel nie jest zabezpieczony.

### Dlaczego próba wysyłania żądań z User-agenta "GG PeekBot" kończy się niepowodzeniem?

Albo po prostu bot jest przed tym zabezpieczony, albo nie wiem. Nie mam pojęcia. Na moim bocie to nie działa, ale na bocie mojego kolegi (pozdrawiam!) działa to wyśmienicie. Może to być wina wersji PHP na serwerze, może to być wina nieodpowiedniego zdefiniowania zmiennej odpowiadającej za wiadomość użytkownika w skrypcie... Naprawdę nie mam pojęcia.

### Dlaczego tak trudno znaleźć cel?

Boty na GG istnieją już bardzo długo (około 10 lat). Przez ten czas użytkownicy nauczyli się, jak zabezpieczać swoje boty przed nieautoryzowanym dostępem.

### Czy można wysyłać wiadomości z dowolnego numeru GG do zwykłego użytkownika?

Nie. Ciekawe, skąd wziąć adres URL do pliku PULL człowieka 🙄