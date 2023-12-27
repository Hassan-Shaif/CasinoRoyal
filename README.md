# CasinoRoyal

Beschrijving van het spel:
De deelnemer moet een getal raden onder de 10. Dat getal wordt random gegenereerd door het python programma.
Eerst moet de deelnemr een inzet (in coins) invoeren en daarna een getal waarmee hij het getal onder de 10 probeert te raden. Als hij het raadt wint hij en als hij het niet raadt verliest hij.
Hoe je het precies uitvoert kan in verschillende niveaus, ga minimaal tot niveau 2. Je bent verplicht om in je code één of meer functies te schrijven.
Niveau 1:
Het te raden getal (1-9) moet random worden gegenereerd.
Als het ingevoerde getal het juiste getal is krijgt de gebruiker de
melding: “inzet is verdubbeld, je hebt nu [bedrag]”. Als het niet zo is dan krijgt deze de melding: “inzet is helaas verloren”.
Je zorgt ervoor dat de gebruiker alleen maar een geheel getal onder de 10 kan invoeren (niet 0). Als iemand iets anders invult (tekst of ander getal) volgt er de melding: “je mag alleen hele getallen van 1 tot 9 invullen”. (maak hierbij gebruik van een list)
Niveau 2 - competent
De gebruiker mag zo vaak raden als hij wil. Het programma stopt pas als de gebruiker dat aangeeft. Je moet de gebruiker na iedere ronde dan ook steeds de vraag voorleggen: “wil je doorgaan [y, n]”. Als de gebruiker “y” invoert begint het hele spel opnieuw. Als hij “n” invoert stopt het spel en krijgt hij de mededeling: “Bedankt voor het spelen en tot ziens”.
Niveau 3 - Expert
Nu komt er iets bij: kapitaal.
Kapitaal wil zeggen: het totaalbedrag in coins wat de gebruiker bij dit spel tot zijn beschikking heeft. Het Casino probeert de speler een beetje te beschermen en stelt dat 1000 coins het maximum is. Onze speler heeft dan ook bij aanvang van het spel 1000 coins.
Je vraagt aan de speler bij iedere speelronde hoeveel coins hij “inzet”.
Als hij wint wordt de inzet vertiendubbeld en bij het kapitaal opgeteld.
Als hij verliest wordt de inzet van het kapitaal afgetrokken.
De gebruiker mag niet meer inzetten dan hij kan verliezen. Probeert hij dat wel dan volgt er een melding “inzet te hoog, u mag maximaal [bedrag] inzetten”.
De speler mag alleen verder gaan met raden als zijn kapitaal nog groter dan 0 is. Ook hier vraag je aan de speler na iedere speelronde of hj nog wil doorgaan y/n.
Niveau 4 – wauw geniaal!
Ieder verlies of winst van de gebruiker wordt in een csv file bijgeschreven.
Winst van de gebruiker wordt als een negatief getal uitgedrukt en verlies als een positief getal. (de csv file is vanuit het perspectief van het casino opgesteld.)
Na maximaal 20 gokbeurten stopt het spel en maken we de balans op: is het casino rijker geworden of de gebruiker? (lees de csv file uit)

