# Fysik-quiz-app
## 1. Beskrivelse af Projektets Formål og Målgruppe
Formålet med denne applikation er at tilbyde gymnasieelever en nem og tilgængelig måde at øve og forstå SI-enheder og SI-præfikser på. Målgruppen er gymnasieelever, der tager fysik som et fag, og som søger en interaktiv metode til at styrke deres kendskab til dette essentielle område inden for fysik. Appen er designet til at være intuitiv, hvilket gør den ideel for elever, der ønsker en hurtig og effektiv læringsressource.

## 2. Benyttede Designmønstre
Vi har valgt at benytte os af Command-mønstret, som er en del af de adfærdsmæssige designmønstre. Dette mønster er særligt effektivt til at håndtere funktionskald og operationer, hvilket gør det ideelt til en app, der kræver interaktivitet og responsivitet. Ved at anvende dette mønster, har vi øget appens modulære natur og gjort det lettere at vedligeholde og udvide funktionaliteten over tid.
Læs mere om mønstret her: https://refactoring.guru/design-patterns/command

Klassediagrammet nedenfor illustere Command-mønstret:
```mermaid
classDiagram
    class Command {
        <<abstract>>
        +execute()
    }
    class SelectAnswerCommand {
        -app
        -answer
        +execute()
    }
    class CheckAnswerCommand {
        -app
        +execute()
    }

    Command <|-- SelectAnswerCommand
    Command <|-- CheckAnswerCommand
```

## 3. Beskrivelse af udviklingsprocessen
Vi startede med at brainstom en masse idéer, om hvad vi ville lave en app til, hvor vi meget hurtigt fandt ud af, at vi ville lave en fysik app. Vi tænkte derefter på, hvilke emner inden for fysik, som vi ville basere vores app på, og da tænkte vi på det mest simple og mest brugte i fysik, som er SI-enheder og Præfikser. Vi overvejede også at implementere symboler, men mange af de samme symboler bruges til flere forskellige ting, så vi holdte det bare til de to valgte. 
Inden vi gang i gang med koden og "UI", så skitserede vi, hvordan vores UI skulle være. Vi valgte antal menuer, svarmuligheder, 
I koden begyndte vi først at designe vores UI, hvor vi designede og tilføjede vores "Tkinter labels" og "Tkinter buttons". Vi implementerede derefter forskellige metoder og klasser for at forbedre koden og gøre den mere anvendelig.
Vi har også lavet koden, så man nemt kan tilføje et ekstar spørgsmål og svar under vores data-sæt (dictionary).

## 4. Beskrivelse af brugergrænsefladen.
Flowdiagrammet nedenfor illustrerer brugergrænsefladen. Start/slut-punkterne er markeret med lilla cirkler. Brugerens valgmuligheder er repræsenteret af blå diamanter, hvor brugeren kan interagere ved at klikke på de knapper, der er angivet ved siden af med pile, som viser hvor de fører hentil. Den grønne proces er skjult for forbrugeren og anvendes til at illustrere, forskellige udfald afhængigt af om de har angivet det rigtige eller forkerte. Brugeren har mulighed for at afslutte programmet når som helst ved at bruge 'Alt+F4' eller lukkeknappen i øverste højre hjørne, hvis de foretrækker det frem for appens indbyggede afslutningsknap:

```mermaid
graph LR
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style D fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#9cf,stroke:#333,stroke-width:2px
    style C fill:#9cf,stroke:#333,stroke-width:2px
    style E fill:#9cf,stroke:#333,stroke-width:2px
    style F fill:#9cf,stroke:#333,stroke-width:2px
    style G fill:#6f6,stroke:#333,stroke-width:2px
    style H fill:#9cf,stroke:#333,stroke-width:2px

    A((Start)) --> B{Hovedmenu}
    B --> |Start| C{Emnevalg}
    B --> |Quit| D((Slut)) 
    C --> |SI-Enheder| E{Spilmode}
    C --> |Præfikser| E
    C --> |Tilbage| B
    E --> |Uendelig| F{Quiz spillet}
    E --> |Hardcore| F
    E --> |Tilbage| C
    F --> |Tjek svar| G[Validering]
    F --> |Afslut quiz, hvis spilmode uendelig| H{Resultat}
    G --> |Hvis rigtigt| F
    G --> |Hvis forkert & spilmode uendelig| F
    G --> |Hvis forkert & spilmode hardcore| H
    H --> |Tilbage til menu| B
```

## 5. Et skema med test.
| Titel | Test trin | Forventet resultat | Aktuelle resultat |
| ----------- | ----------- | ----------- | ----------- | 
| Initialisering af hovedmenuen | <ol> <li> Lav en instans af quiz appen </li> </ol> | Hovedmenuen med en 'start' og 'quit' knap vises | Som forventet |
| Afslutning af quiz | <ol> <li> Lav en instans af quiz appen. </li> <li> Klik på knappen 'quit'. | Quiz appen afsluttes | Som forventet |
| Initialisering af emnevalg | <ol> <li> Lav en instans af quiz appen </li> <li> Klik på knappen 'start' </li> </ol> | Emnevalgs menuen vises med 3 knapper 'SI-Enheder', 'Præfikser' og 'Tilbage' | Som forventet |
| Initialisering af spilmode | <ol> <li> Lav en instans af quiz appen </li> <li> Klik på knappen 'start' </li> <li> Klik på enten 'SI-Enheder' eller 'Præfikser' </ol> | Valg af spilmod vises med 3 knapper 'Uendelig', 'Hardcore' og 'Tilbage' | Som forventet |
| Initialisering af spilmode | <ol> <li> Lav en instans af quiz appen </li> <li> Klik på knappen 'start' </li> <li> Klik på enten 'SI-Enheder' eller 'Præfikser' </li> </ol> | Valg af spilmod vises med 3 knapper 'Uendelig', 'Hardcore' og 'Tilbage' | Som forventet |
| Initialisering af quizzen | <ol> <li> Lav en instans af quiz appen </li> <li> Klik på knappen 'start' </li> <li> Klik på enten 'SI-Enheder' eller 'Præfikser' </li> <li> Klik på enten 'Uendelig' eller 'Hardcore' </li> </ol> | Quizzen vises, med et spørgsmål øverst, under er 4 knapper med svar muligheder og nederst er en 'tjek svar' knap. Under står din score. Hvis du har valgt spilmoden 'uendelig' er der en knap 'afslut quiz' | Som forventet |
| Ved rigtigt svar i uendelig spilmode | <ol> <li> Følg trinene i 'Initialisering af quizzen', sørg for at vælge uendelig mode. </li> <li> Besvar spørgsmålet korrelt </li> </ol> | Tjek svar knappen bliver grøn, der bliver tilføjet adderet 1 til din score, og der kommer et nyt spørgsmål og svar muligheder | Som forventet |
| Ved forkert svar i uendelig spilmode | <ol> <li> Følg trinene i 'Initialisering af quizzen', sørg for at vælge uendelig mode. </li> <li> Besvar spørgsmålet forkert </li> </ol> | Tjek svar knappen bliver rød, og der kommer et nyt spørgsmål og svar muligheder | Som forventet |
| Ved rigtigt svar i hardcore spilmode | <ol> <li> Følg trinene i 'Initialisering af quizzen', sørg for at vælge hardcore mode. </li> <li> Besvar spørgsmålet korrelt </li> </ol> | Tjek svar knappen bliver grøn, der bliver tilføjet adderet 1 til din score og der kommer et nyt spørgsmål og svar muligheder | Som forventet |
| Ved forkert svar i hardcore spilmode | <ol> <li> Følg trinene i 'Initialisering af quizzen', sørg for at vælge hardcore mode. </li> <li> Besvar spørgsmålet forkert </li> </ol> | Tjek svar knappen bliver rød, og efterfølgende vises dit resultat, med en knap 'tilbage til menu'| Som forventet |
| Ved klik på 'tilbage til menu' | <ol> <li> Følg trinene i 'Ved forkert svar i hardcore spilmode'. </li> <li> Klik på 'tilbage til menu' </li> </ol> | Du bringes tilbage til hovedmenuen| Som forventet |
| Ved klik på 'afslut quiz' | <ol> <li> Følg trinene i 'Initialiserings af spilmode', sørg for at vælge uendelig mode. </li> <li> Klik på 'afslut quiz' </li> </ol> | Din score vises, under ses en knap 'tilbage til menu'| Som forventet bortset fra der vises antal ukorrekte svar ved siden af scoren |


## 6. Reflektion over brugen af design pattern
I dette projekt anvendte vi Command-mønstret som er under katagori af adfærdsmæssige designmønstre. Fordelen ved anvendelsen af dette er det er nemt og hurtigt at tilføje flere måder at udføre samme handling på, i programmet kan man tjekke svaret på to måder, ved at klikke på knappen 'Tjek svar' eller ved at klikke på tastatur knappen 'Enter'. Havde vi mere tid i projektet, kunne vi tilføje muligheden for at klikke på tasterne 1-4, for at vælge 1 af de 4 svar muligheder.
