# picoGym Level 474: Guess My Cheese (Part 2)
Source: https://play.picoctf.org/practice/challenge/474

## Goal
The imposter was able to fool us last time, so we've strengthened our defenses!<br>
Here's our list of cheeses.<br>
https://challenge-files.picoctf.net/c_verbal_sleep/e910e8a18170825276b65da470bcc5cb2898b5f4d8c60d781d29d83289e20302/cheese_list.txt<br>
Connect to the program on our server:<br>
nc verbal-sleep.picoctf.net 50698

## What I learned
```
SHA256 is a cryptographic hash function: one direction
But if you know all possible originals(cheese_list.txt) try them all and see which one produces same output

Brute-force: Try every cheese name with every possible salt, hash each, and see which matches the server’s hash
Rainbow Table: Build a lookup table (hash → cheese) for all possible combinations so you can answer instantly

multiple encodings (utf-8, utf-16-le, utf-16-be, latin-1)

2 nibble or 1 byte hexademical-character salt
   1 nibble = 4 bits
   2 nibbles = 8 bits = 1 byte
   1 hex digit = 1 nibble (single hex digit encodes values 0–15, which fits in 4 bits) ❤️❤️❤️❤️❤️
   2 hex digits = 2 nibbles = 1 byte (values 0–255) ❤️❤️❤️❤️❤️

Example (Important Concept):
   0xA → 1 hex digit = 1 nibble = 4 bits (1010 in binary)
   0x3F → 2 hex digits = 2 nibbles = 1 byte = 8 bits (00111111 in binary)

Linux: grep    Windows: findstr ❤️
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://challenge-files.picoctf.net/c_verbal_sleep/ e910e8a18170825276b65da470bcc5cb2898b5f4d8c60d781d29d83289e20302/cheese_list.txt ⌨️
--2025-09-12 00:16:48--  https://challenge-files.picoctf.net/c_verbal_sleep/e910e8a18170825276b65da470bcc5cb2898b5f4d8c60d781d29d83289e20302/cheese_list.txt
Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.95, 3.160.5.40, 3.160.5.64, ...
Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.95|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 7611 (7.4K) [application/octet-stream]
Saving to: 'cheese_list.txt'

cheese_list.txt                             100%[=========================================================================================>]   7.43K  --.-KB/s    in 0s      

2025-09-12 00:16:48 (2.09 GB/s) - 'cheese_list.txt' saved [7611/7611]

AsianHacker-picoctf@webshell:/tmp$ cat cheese_list.txt ⌨️
Abbaye du Mont des Cats
Abertam
Ackawi
Acorn
Allgauer Emmentaler
Anejo Enchilado
Anthoriro
Ardi Gasna
Asiago
Balaton
Barry's Bay Cheddar
Basing
Bavarian Bergkase
Beauvoorde
Berkswell
Blue
Boeren Leidenkaas
Bra
Buffalo
Cabrales
Caerphilly
Cairnsmore
Canestrato
Castellano
Castelleno
Castelmagno
Castigliano
Comte
Coolea
Coquetdale
Corleggy
Cotherstone
Cotija
Coverdale
Crayeux de Roncq
Crottin de Chavignol
Curworthy
Cwmtawe Pecorino
Denhany Dorset Drum
Derby
Doolin
Dorset Blue Vinney
Double Worcester
Dry Jack
Duddleswell
Dunlop
Duroblando
Dutch Mimolette (Commissiekaas)
Emmental
Etorki
Evora De L'Alentejo
Finlandia Swiss
Fiore Sardo
Folded cheese with mint
Four Herb Gouda
Fourme de Montbrison
Fribourgeois
Friesekaas
Friesian
Fromage a Raclette
Frying Cheese
Gabriel
Gammelost
Gaperon a l'Ail
Garrotxa
Gornyaltajski
Gospel Green
Gowrie
Grafton Village Cheddar
Grana
Grana Padano
Graviera
Gruyere
Halloumi
Halloumy (Australian)
Haloumi-Style Cheese
Heidi Gruyere
Herriot Farmhouse
Iberico
Idaho Goatster
Idiazabal
Isle of Mull
Jarlsberg
Jindi Brie
Kadchgall
Kefalotyri
Laguiole
Lairobell
Lancashire
Laruns
Lavistown
Leafield
Leicester
Leyden
Lincolnshire Poacher
Llanboidy
Llanglofan Farmhouse
Loch Arthur Farmhouse
Longhorn
Lou Palou
Mahon
Malvern
Manchego
Manur
Marble Cheddar
Menallack Farmhouse
Mihalic Peynir
Montasio
Monterey Jack Dry
Northumberland
Orkney Extra Mature Cheddar
Oschtjepka
Parmesan (Parmigiano)
Parmigiano Reggiano
Pecorino
Pecorino Romano
Penbryn
Piora
Plymouth Cheese
Pressato
Pyengana Cheddar
Queso del Tietar
Queso Iberico
Queso Majorero
Queso Para Frier
Raclette
Ragusano
Reggianito
Remedou
Ricotta Salata
Romano
Roncal
Saanenkaese
Sainte Maure
Salers
Sancerre
Sap Sago
Sardo
Sardo Egyptian
Sbrinz
Schabzieger
Serat
Seriously Strong Cheddar
Shelburne Cheddar
Shropshire Blue
Smoked Gouda
Spenwood
Sraffordshire Organic
Stinking Bishop
Swaledale
Swiss
Syrian (Armenian String)
Tala
Teifi
Tillamook Cheddar
Tomme d'Abondance
Tyn Grug
Tyning
Ubriaco
Wellington
Wensleydale
White Stilton
Xynotyro
Yarg Cornish
Zamorano
Zanetti Grana Padano
Zanetti Parmigiano Reggiano
Abbaye de Belloc
Abondance
Airedale
Alverca
Appenzell
Aragon
Ardrahan
Aubisque Pyrenees
Beaufort
Bierkase
Blarney
Bleu de Septmoncel
Braudostur
Brick
Canadian Cheddar
Cantal
Chaumes
Cheddar
Cheshire
Chevres
Chontaleno
Cojack
Colby-Jack
Crowley
Devon Blue
Devon Garland
Double Gloucester
Edam
Edelpilz
Esbareich
Esrom
Filetta
Fontal
Fourme d' Ambert
Friesla
Fynbo
Geitost
Gjetost
Gloucester
Gouda
Goutu
Grabetto
Graddost
Greve
Herrgardsost
Herve
Juustoleipa
Kikorangi
Leerdammer
Maasdam
Mamirolle
Maribo
Matocq
Meira
Menonita
Meyer Vintage Gouda
Mimolette
Mixte
Molbo
Mondseer
Monterey Jack
Murol
Nokkelost
Orla
Ossau Fermier
Ossau-Iraty
Oszczypek
Passendale
Penamellera
Petit Pardou
Podhalanski
Port-Salut
Prastost
Provolone
Provolone (Australian)
Rabacal
Ridder
Roquefort
Royalp Tilsit
Saaland Pfarr
Sage Derby
Saint-Paulin
Samso
San Simon
Schloss
Siraz
Stilton
String
Sveciaost
Sweet Style Swiss
Tasmania Highland Chevre Log
Testouri
Tete de Moine
Tibet
Tilsit
Toma
Tomme de Romans
Tommes
Toscanello
Touree de L'Aubier
Tourmalet
Trappe (Veritable)
Turunmaa
Vasterbottenost
Waimata Farmhouse Blue
Yorkshire Blue
Adelost
Airag
Aisy Cendre
American Cheese
Ami du Chambertin
Aromes au Gene de Marc
Asadero
Autun
Baby Swiss
Beenleigh Blue
Bel Paese
Bergere Bleue
Beyaz Peynir
Bishop Kennedy
Bocconcini (Australian)
Boulette d'Avesnes
Brillat-Savarin
Brin
Bruder Basil
Butterkase
Calenzana
Casciotta di Urbino
Celtic Promise
Charolais
Chevrotin des Aravis
Colby
Cougar Gold
Cream Havarti
Croghan
Curd
Danbo
Danish Fontina
Dauphin
Durrus
Feta (Australian)
Folded
Fontina Val d'Aosta
Fresh Jack
Fromage de Montagne de Savoie
Gubbeen
Havarti
Hipi Iti
Hushallsost
Il Boschetto al Tartufo
King River Gold
Lajta
Langres
Lappi
Le Brin
Le Fium Orbo
Livarot
Loddiswell Avondale
Maroilles
Milleens
Monastery Cheeses
Morbier
Morbier Cru de Montagne
Mozzarella (Australian)
Neufchatel (Australian)
Oaxaca
Paneer
Pasteurized Processed
Pave d'Auge
Pepper jack
Picos de Europa
Pinconning
Polkolbin
Pont l'Eveque
Port Nicholson
Quartirolo Lombardo
Queso Blanco con Frutas --Pina y Mango
Raschera
Reblochon
Rocamadour
Rollot
Rubens
Saint-Nectaire
Sonoma Jack
Sottocenare al Tartufo
Sourire Lozerien
Taleggio
Tamie
Tetilla
Tomme de Chevre
Tomme de Savoie
Tronchon
Ulloa
Waterloo
Wigmore
Ambert
Anneau du Vic-Bilh
Avaxtskyr
Babybel
Baguette Laonnaise
Bakers
Baladi
Bandal
Banon
Basket Cheese
Bath Cheese
Beer Cheese
Bergader
Bleu d'Auvergne
Bleu de Gex
Bleu de Laqueuille
Bleu Des Causses
Blue Castello
Bonchester
Bosworth
Bougon
Boursault
Boursin
Bouyssou
Breakfast Cheese
Brebis du Lavort
Brebis du Lochois
Brebis du Puyfaucon
Bresse Bleu
Brie
Brie de Meaux
Brie de Melun
Brin d' Amour
Brin d'Amour
Brinza (Burduf Brinza)
Briquette de Brebis
Broccio
Broccio Demi-Affine
Brousse du Rove
Brusselae Kaas (Fromage de Bruxelles)
Bryndza
Buchette d'Anjou
Butte
Button (Innes)
Buxton Blue
Cabecou
Caboc
Cachaille
Caciocavallo
Caciotta
Camembert de Normandie
Caprice des Dieux
Capricorn Goat
Caravane
Carre de l'Est
Cashel Blue
Castelo Branco
Cathelain
Cendre d'Olivet
Cerney
Chabichou
Chabichou du Poitou
Chabis de Gatine
Chaource
Civray
Coeur de Camembert au Calvados
Coeur de Chevre
Cold Pack
Cooleney
Cornish Pepper
Cottage Cheese
Cottage Cheese (Australian)
Coulommiers
Cream Cheese
Crema Agria
Crema Mexicana
Creme Fraiche
Crottin du Chavignol
Cuajada
Cure Nantais
Daralagjazsky
Delice des Fiouves
Dessertnyj Belyj
Dolcelatte
Doppelrhamstufel
Dreux a la Feuille
Dunbarra
Emlett
Evansdale Farmhouse Brie
Explorateur
Farmer
Feta
Figue
Fin-de-Siecle
Finn
Fleur du Maquis
Flor de Guia
Flower Marie
Fondant de Brebis
Fontainebleau
Fougerus
Fourme de Haute Loire
Fresh Mozzarella
Fresh Ricotta
Frinault
Fromage Corse
Fromage Frais
Fruit Cream Cheese
Galette du Paludier
Galette Lyonnaise
Gastanberra
Golden Cross
Gorgonzola
Grand Vatel
Grataron d' Areches
Gratte-Paille
Greuilh
Gris de Lille
Guerbigny
Hereford Hop
Humboldt Fog
Jubilee Blue
Kenafa
Kernhem
Kervella Affine
King Island Cape Wickham Brie
Klosterkaese
Kugelkase
L'Aveyronnais
L'Ecir de l'Aubrac
La Taupiniere
La Vache Qui Rit
Le Lacandou
Le Roule
Lebbene
Limburger
Lingot Saint Bousquet d'Orb
Little Rydings
Lyonnais
Macconais
Mahoe Aged Gouda
Maredsous
Margotin
Mascarpone
Mascarpone (Australian)
Mascarpone Torta
Metton (Cancoillotte)
Mine-Gabhar
Mothais a la Feuille
Mozzarella
Mozzarella di Bufala
Mozzarella Fresh, in water
Mozzarella Rolls
Munster
Mycella
Myzithra
Nantais
Neufchatel
Niolo
Olivet au Foin
Olivet Cendre
P'tit Berrichon
Palet de Babligny
Panela
Pannerone
Pant ys Gawn
Pate de Fromage
Patefine Fort
Pave d'Affinois
Pave de Chirac
Peekskill Pyramid
Pelardon des Cevennes
Pelardon des Corbieres
Pencarreg
Petit-Suisse
Picodon de Chevre
Pithtviers au Foin
Plateau de Herve
Poivre d'Ane
Pouligny-Saint-Pierre
Pourly
Prince-Jean
Provel
Pyramide
Quark
Quark (Australian)
Quatre-Vents
Quercy Petit
Queso Blanco
Queso de Murcia
Queso del Montsec
Queso Fresco
Queso Fresco (Adobera)
Queso Jalapeno
Queso Quesadilla
Regal de la Dombes
Requeson
Richelieu
Ricotta
Ricotta (Australian)
Rigotte
Romans Part Dieu
Rouleau De Beaulieu
Rustinu
Saga
Saint-Marcellin
Scamorza
Selles sur Cher
Selva
Serra da Estrela
Sharpam
Sirene
Somerset Brie
Soumaintrain
Sussex Slipcote
Taupiniere
Telemea
Texas Goat Cheese
Timboon Brie
Tomme des Chouans
Torta del Casar
Trois Cornes De Vendee
Truffe
Tupi
Tymsboro
Vacherin-Fribourgeois
Valencay
Venaco
Vendomois
Vieux Corse
Vignotte
Vulscombe
Washed Rind Cheese (Australian)
Weichkaese
Whitestone Farmhouse
Woodside Cabecou
Yarra Valley Pyramid

# Method 1: Brute Force, Interactive
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> cat .\pythonScript.py ⌨️
import hashlib
import time
import re
import threading
import itertools
import sys

# Prompt user for the SHA-256 hash
print("=" * 60)
print("ðŸ”
print("=" * 60)

while True:
    user_hash = input("Enter the target SHA-256 hash: ").strip().lower()
    if re.fullmatch(r"[a-f0-9]{64}", user_hash):
        TARGET_HASH = user_hash
        break
    else:
        print("â\033[0m")
    print(ascii_bunny())
    print("-" * 50)
    print(f"\033[96mCheese Name   :\033[0m {cheese}")
    print(f"\033[96mCase Variant  :\033[0m {case_type}")
    print(f"\033[96mEncoding      :\033[0m {encoding}")
    print(f"\033[96mSalt Value    :\033[0m (0x{salt:02x})")
    print(f"\033[96mMethod Used   :\033[0m {method}")
    print(f"\033[96mExtra Info    :\033[0m {extra_info}")
    print(f"\033[96mSHA-256 Hash  :\033[0m {TARGET_HASH}")
    try:
        decoded = candidate.decode(encoding)
    except Exception:
        decoded = repr(candidate)
    print(f"\033[96mCandidate Str :\033[0m {decoded}")
    print("-" * 50)
    return True

def generate_candidates(cheese_bytes, salt, encoding):
    salt_byte = bytes([salt])
    try:
        salt_hex_bytes = format(salt, "02x").encode(encoding)
    except Exception:
        salt_hex_bytes = format(salt, "02x").encode("utf-8")

    # Standard variations
    yield cheese_bytes + salt_byte, "append_raw", "raw byte appended"
    yield salt_byte + cheese_bytes, "prepend_raw", "raw byte prepended"
    yield cheese_bytes + salt_hex_bytes, "append_hex", "hex string appended"
    yield salt_hex_bytes + cheese_bytes, "prepend_hex", "hex string prepended"

    # Insert raw byte at each index
    for i in range(len(cheese_bytes) + 1):
        yield cheese_bytes[:i] + salt_byte + cheese_bytes[i:], "insert_raw", f"at index {i}"

    # Insert hex byte at each index
    for i in range(len(cheese_bytes) + 1):
        yield cheese_bytes[:i] + salt_hex_bytes + cheese_bytes[i:], "insert_hex", f"at index {i}"

# Spinner control flag
spinner_running = False

def loading_spinner():
    for frame in itertools.cycle(['|', '/', '-', '\\']):
        if not spinner_running:
            break
        sys.stdout.write(f'\r\033[93m[*] Cracking in progress... {frame}\033[0m')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * 50 + '\r')  # Clear line

# === Brute-force Execution ===
start_time = time.time()
print("\n[*] Starting cheese cracking operation...\n")

# Start spinner thread
spinner_running = True
spinner_thread = threading.Thread(target=loading_spinner)
spinner_thread.start()

match_found = False

for cheese in cheese_names:
    for case_type, transform in CASE_TRANSFORMS.items():
        transformed = transform(cheese)

        for encoding in ENCODINGS:
            try:
                cheese_bytes = transformed.encode(encoding)
            except Exception:
                continue

            for salt in range(256):
                for candidate, method, extra_info in generate_candidates(cheese_bytes, salt, encoding):
                    if check_candidate(candidate, cheese, case_type, encoding, salt, method, extra_info):
                        match_found = True
                        break
                if match_found:
                    break
            if match_found:
                break
        if match_found:
            break
    if match_found:
        break

# Stop spinner
spinner_running = False
spinner_thread.join()

end_time = time.time()

# Final status
if match_found:
    print(f"\n[+] Execution completed in \033[92m{end_time - start_time:.2f}\033[0m seconds.")
else:
    print("\n\033[91m[!] No matching cheese and salt combination was found.\033[0m")

PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> python .\pythonScript.py ⌨️
============================================================
🔐 Cheese Cracker v1.0 - SHA-256 Hash Brute-Forcer
============================================================
Enter the target SHA-256 hash: a66e329b26635af5dacc15b418f05083563bdf8c1ad389cc90da012952647680 ⌨️

[*] Starting cheese cracking operation...

[*] Cracking in progress... /
[✔] Match Found! 🧀🐰

         _   _
        (q\_/p)
         /. .\         __     
  ,__   =\_t_/=      .'o O'-. 
     )   /   \      / O o_.-`|
    (   ((   ))    /O_.-'  O |
     \  /\) (/\    | o   o  o|
      `-\  Y  /    |o   o O.-`
         nn^nn     | O _.-'
                   '--`

--------------------------------------------------
Cheese Name   : Little Rydings 👀
Case Variant  : lower
Encoding      : utf-8
Salt Value    : (0x7e) 👀 Need 2 digits to right
Method Used   : append_raw
Extra Info    : raw byte appended
SHA-256 Hash  : a66e329b26635af5dacc15b418f05083563bdf8c1ad389cc90da012952647680
Candidate Str : little rydings~
--------------------------------------------------

[+] Execution completed in 332.01 seconds.

AsianHacker-picoctf@webshell:~$ nc verbal-sleep.picoctf.net 52298 ⌨️

*******************************************
***             Part 2                  ***
***    The Mystery of the CLONED RAT    ***
*******************************************

DRAT! The evil Dr. Lacktoes Inn Tolerant's clone was able to guess the cheese last time! I guess simple ciphers aren't good hashing methods. But now I've strengthened my encryption scheme so that now ONLY SQUEEXY can guess it...

Here's my secret cheese -- if you're Squeexy, you'll be able to guess it:  a66e329b26635af5dacc15b418f05083563bdf8c1ad389cc90da012952647680 👀

Commands: (g)uess my cheese
What would you like to do?
g ⌨️

   _   _
  (q\_/p)
   /. .\.-.....-.     ___,
  =\_t_/=     /  `\  (
    )\ ))__ __\   |___)
   (/-(/`  `nn---'

SQUEAK SQUEAK SQUEAK

         _   _
        (q\_/p)
         /. .\        
  ,__   =\_t_/=   
     )   /   \      
    (   ((   ))   
     \  /\) (/\    
      `-\  Y  /    
         nn^nn        
                          

Is that you, Squeexy? Are you ready to GUESS...MY...CHEEEEEEESE?
Remember, this is my encrypted cheese:  a66e329b26635af5dacc15b418f05083563bdf8c1ad389cc90da012952647680 👀
So...what's my cheese?
Little Rydings ⌨️
Annnnd...what's my salt?
7e ⌨️

         _   _
        (q\_/p)
         /. .\         __
  ,__   =\_t_/=      .'o O'-.
     )   /   \      / O o_.-`|   
    (   ((   ))    /O_.-'  O |  
     \  /\) (/\    | o   o  o|   
      `-\  Y  /    |o   o O.-`  
         nn^nn     | O _.-'      
                   '--`         

munch...

         _   _
        (q\_/p)
         /. .\         __
  ,__   =\_t_/=      .'o O'-.
     )   /   \      / O o_.-`|   
    (   ((   ))      ).-'  O |  
     \  /\) (/\      )   o  o|   
      `-\  Y  /    |o   o O.-`  
         nn^nn     | O _.-'      
                   '--`         

munch...

         _   _
        (q\_/p)
         /. .\         __
  ,__   =\_t_/=      .'o O'-.
     )   /   \      / O o_.-`|   
    (   ((   ))        )'  O |  
     \  /\) (/\          )  o|   
      `-\  Y  /         ) O.-`  
         nn^nn        ) _.-'      
                   '--`         

MUNCH.............

YUM! MMMMmmmmMMMMmmmMMM!!! Yes...yesssss! That's my cheese!
Here's the password to the cloning room:  picoCTF{cHeEsYfd97a77d} 🔐

Method 2: brute force
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> vim pythonScript.py ⌨️
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> cat .\pythonScript.py ⌨️
#!/usr/bin/env python3
import hashlib
import sys

target_hash = "a66e329b26635af5dacc15b418f05083563bdf8c1ad389cc90da012952647680"

encodings = ["utf-8", "utf-16-le", "utf-16-be", "latin-1"]
case_variants = {
    "original": lambda s: s,
    "lower": lambda s: s.lower(),
    "upper": lambda s: s.upper(),
}

try:
    with open("cheese_list.txt", "r") as f:
        cheeses = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("cheese_list.txt not found.")
    sys.exit(1)

found = False

def test_candidate(candidate_bytes, method, extra, cheese, case_name, enc, salt):
    global found
    hash_val = hashlib.sha256(candidate_bytes).hexdigest()
    if hash_val == target_hash:
        print(f"âœ… Match found!")
        print(f"Cheese: {cheese} | Case: {case_name} | Encoding: {enc}")
        print(f"Salt: {salt} | Method: {method} | Extra: {extra}")
        found = True
        return True
    return False

for cheese in cheeses:
    for case_name, case_func in case_variants.items():
        cheese_variant = case_func(cheese)
        for enc in encodings:
            try:
                cheese_bytes = cheese_variant.encode(enc)
            except:
                continue
            for salt in range(256):
                salt_raw = bytes([salt])
                salt_hex_str = format(salt, "02x")
                try:
                    salt_hex = salt_hex_str.encode(enc)
                except:
                    salt_hex = salt_hex_str.encode("utf-8")

                if test_candidate(cheese_bytes + salt_raw, "append_raw", "raw byte appended", cheese, case_name, enc, salt): break
                if test_candidate(salt_raw + cheese_bytes, "prepend_raw", "raw byte prepended", cheese, case_name, enc, salt): break
                if test_candidate(cheese_bytes + salt_hex, "append_hex", "hex string appended", cheese, case_name, enc, salt): break
                if test_candidate(salt_hex + cheese_bytes, "prepend_hex", "hex string prepended", cheese, case_name, enc, salt): break

                for i in range(len(cheese_bytes) + 1):
                    if test_candidate(cheese_bytes[:i] + salt_raw + cheese_bytes[i:], "insert_raw", f"at byte {i}", cheese, case_name, enc, salt): break   
                if found: break
                for i in range(len(cheese_bytes) + 1):
                    if test_candidate(cheese_bytes[:i] + salt_hex + cheese_bytes[i:], "insert_hex", f"at byte {i}", cheese, case_name, enc, salt): break   
                if found: break
            if found: break
        if found: break
    if found: break

if not found:
    print(" No match found.")

PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> python .\pythonScript.py ⌨️
✅ Match found!
Cheese: Little Rydings | Case: lower | Encoding: utf-8 👀
Salt: 126 | Method: append_raw | Extra: raw byte appended 👀❤️ Convert

# Note: Need convert salt to hex in linux enviroment, windows printf not work
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> printf "%x\n" 126 ⌨️
printf : The term 'printf' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a 
path was included, verify that the path is correct and try again.
At line:1 char:1
+ printf "%x\n" 126
+ ~~~~~~
    + CategoryInfo          : ObjectNotFound: (printf:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

AsianHacker-picoctf@webshell:~$ printf "%x\n" 126 ⌨️
7e 👀
AsianHacker-picoctf@webshell:~$ printf "%X\n" 126 ⌨️
7E 👀
AsianHacker-picoctf@webshell:~$ python3 -c "print(hex(126))" ⌨️
0x7e 👀

Method 3: rainbow table of all cheeses with each possible one byte hexadecimal salt (Easiest Method to understand)
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> cat .\pythonScript.py ⌨️
#!/usr/bin/env python3
import hashlib

inputFile = open("cheese_list.txt","r")
outputFile = open("SHA256", "w")       

def generateSHA256(plaintext):
    '''Takes plaintext and returns the sha256 of it''' 
    h = hashlib.new('sha256') # Sha256 object hasher   
    h.update(plaintext)
    return h.hexdigest()

for cheese in inputFile:
    cheese = ("".join(cheese.strip())).lower().encode()
    for salt in range(256):
        # Salt at the end of plaintext
        salted_cheese = cheese + salt.to_bytes()
        hashed_salted_cheese = generateSHA256(salted_cheese)
        outputFile.write(f'{hashed_salted_cheese}\tPlaintext: {cheese}: {salt:02x}\n')

PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> Get-Content .\SHA256 | Select-Object -First 5 ⌨️
21916899cd43e3655ddddd7b041339285d0e0dc656e4df83d4d0640ba3af0f60        Plaintext: b'abbaye du mont des cats': 00
54f630ac882c460cad0f64da6da7883e9f08b904e051f6d6f4f897dd7ed26136        Plaintext: b'abbaye du mont des cats': 01
5fd89e7b4350bfe16abd60845202893c6567cce287c4dea0a78784731783d9bf        Plaintext: b'abbaye du mont des cats': 02
40946e98896b6546b8c1227dbc9276e316e9f09f539a7ede87be43cbbc65d223        Plaintext: b'abbaye du mont des cats': 03
cc6df8f84fa427026a97ed3775bee634cb64a8cbdb9b0effb4b8253e93176921        Plaintext: b'abbaye du mont des cats': 04
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> cat .\SHA256 | grep -e "a66e329b26635af5dacc15b418f05083563bdf8c1ad389cc90da012952647680" ⌨️⚠️
grep : The term 'grep' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a 
At line:1 char:16
+ cat .\SHA256 | grep -e "a66e329b26635af5dacc15b418f05083563bdf8c1ad38 ...
+                ~~~~
    + CategoryInfo          : ObjectNotFound: (grep:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> findstr a66e329b26635af5dacc15b418f05083563bdf8c1ad389cc90da012952647680 SHA256 ⌨️
a66e329b26635af5dacc15b418f05083563bdf8c1ad389cc90da012952647680        Plaintext: b'little rydings': 7e 👀
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> Get-Content .\SHA256 | Select-String "a66e329b26635af5dacc15b418f05083563bdf8c1ad389cc90da012952647680" ⌨️

a66e329b26635af5dacc15b418f05083563bdf8c1ad389cc90da012952647680        Plaintext: b'little rydings': 7e 👀
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> Select-String -Path .\SHA256 -Pattern "a66e329b26635af5dacc15b418f05083563bdf8c1ad389cc90da012952647680" ⌨️

SHA256:127871:a66e329b26635af5dacc15b418f05083563bdf8c1ad389cc90da012952647680  Plaintext: b'little rydings': 7e 👀
```

## Flag
picoCTF{cHeEsYfd97a77d}

## Continue
[Continue](./picoGym0407.md)