# Nokia_verseny_2023
 Ónodi-Kiss Viktor megoldásai a 2023-as Nokia versenyre


 # Bevezetés

 A programok megírásához és teszteléséhez a Pycharm Professional 2022.2.4-es verzióját használtam, amihez a JetBrains nagylelkű ingyenes tanulói licenszének köszönhetően jutottam hozzá. Továbbá fontos megemlítenem, hogy a programokat egy Windows 10-es AMD x64-es operációs rendszer architecktúrán írtam meg, a Python 3.11.0-ás verziójával írtam meg, melyet azért választottam, mert bár már tartalmazza a fontosabb funkciókat(gyorsabb futásidő) a 3.11-es verziónak köszönhetően, de már nem annyira friss, hogy ritka legyen.

 A programok tesztelése kizárólag a Pycharm beépített konzolán keresztül történt meg, de elméletben a parancssorban is lefutnak, a Dobble futtatásánál lehetőséget is adtam a felhasználónak, hogy a "dobble.py" beírása után egy integer bevitelével adja meg a kártyapakli méretét.


 # Snake

 ## Felhasználói dokumentáció

 A program elindításakor a felhasználó előtt megjelenik a feladatleírásban megadott 60 (+ 2 a határral) egység magas és 30 (+ 2 a határral) egység széles pálya.
 Illetve a felhasználót megkérdezi a program, hogy merre szeretne tovább lépni.

 ![Ábra 1.1, Snake start](Kepek/Snake/1_1_start.PNG)


 Ezt követően a felhasználó a "balra", "jobbra", "fel" és "le" parancsokkal tud haladni, melyeket kedv szerint ki is egészítheti egy számmal, mely esetben a program annyiszor hajtja végre a lépést.

 ![Ábra 1.2, Snake bemenet_1](Kepek/Snake/1_2_Bemenet_1.PNG)

 Illetve a "meguntam" parancs beírásával a felhasználó ki is tud lépni a játékból.

 ![Ábra 1.3, Snake bemenet_2](Kepek/Snake/1_3_Bemenet_2.PNG)

 Fontos megemlíteni, hogy a bemenetnél nem számít a kis- és nagybetű. A program mind a kettő formájában végrehajtja az utasítást.


 A navigációval a felhasználó el tudja érni a "$" szimbólummal jelölt cseresznyéket, melyek érintésével a kígyó mérete megnő egyel.

 ![Ábra 1.4, Snake Cseresznye](Kepek/Snake/1_4_cseresznye.PNG)


Ezt követően a játék egészen addig megy, amíg a felhasználó vagy nekimegy a pálya szélét jelző "\*"-nak, vagy a "meguntam" szó beírásával befejezi a játékot. (Értelemszerűen a program leállítható az ablak bezárásával, vagy a "stop" gombra kattinttással)


## Fejlesztői dokumentáció

![Ábra 1.5, Snake Usecase](Kepek/Snake/1_5_use_case.png)

A program megírásánál figyelembe vettem a feladatleírásban megadott követelményeket.

A programot kettő részre bontottam a tervezés fázisánál. 

Az első rész, a "snake_main.py" felel a felhasználótól való adat kezelésre, illetve a szükséges függvények meghívásáért.

A második rész, a "map.py" felel a pályán végrehajtott műveletekért. Itt található a kígyó részeit tartalmazó "snakes" lista, a mozgatáshoz szükéges "MoveSnake" függvény és minden más is.


# Dobble

## Felhasználói dokumentáció

A program paraméterét a felhasználó megadhatja a konzolon keresztül, parancssori paraméterként.

![Ábra 2.1, Dobble paraméter_1](Kepek/Dobble/2_1_parameter.PNG)

Illetve megadhatja a konzolban megjelenő kérdére válaszolva is.

![Ábra 2.2, Dobble paraméter_2](Kepek/Dobble/2_2_parameter_2.PNG)

Fontos megjegyezni, hogy a kettő verzió nem működik egy időben. Egyszerre csak az egyik módon kap a program paramétert.

Ezt követően a program legenerálja a paraméterül megadott számnyi kártyából álló Dobble kártyapaklit.

![Ábra 2.3, Dobble eredmény](Kepek/Dobble/2_3_results.PNG)


## Fejlesztői dokumentáció

A programot kettő részre bontottam a tervezéskor.
A "dobble.py" tartalmazza a felhasználó adatbekérést, a "dobble_generator.py" pedig az alapján legenerálja a kártya paklit, melyet visszaad a "dobble.py"-nak, hogy kinyomtassa.


# Pizzarendelés


