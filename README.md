# TMA4121
<h1>Numerical analysis of Poission equation</h1>

I denne numeriske analysen har jeg tatt for meg poissonligningen for å modellere det elektriske potensialet rundt en punktladning. 
Området jeg har sett på er sirkulært med da punktladningen i sentrum. Jeg har valgt å vise potensialet i 2D-figur ettersom jeg slet med å vise 3D figur i python...
Jeg begynte med å søke rundt på ulike PDE-er som ikke var direkte pensum og kom frem til Poisson-ligningen. Det var i tillegg spennende når jeg fant et eksempel direkte
knyttet opp mot elektronikk-studiene.

Så hvor begynte jeg? Vel, jeg fant noen gode kilder i blant annet: R. E. Hunt (2002), Cambridge university, http://ael.cbnu.ac.kr/lectures/graduate/adv-em-1/2018-1/lecture-notes/electrostatics-1/ch4-electrostatics-1-appendix-C-numerical-sol-poisson.pdf, og wikipediasiden om Poisson ligningen https://en.wikipedia.org/wiki/Poisson%27s_equation. Jeg brukte også litt mer indirekte denne siden for inspirasjon: https://www.studysmarter.co.uk/explanations/physics/electromagnetism/poisson-equation/.
Jeg fant også noen som numerisk hadde løst den: http://ael.cbnu.ac.kr/lectures/graduate/adv-em-1/2018-1/lecture-notes/electrostatics-1/ch4-electrostatics-1-appendix-C-numerical-sol-poisson.pdf, men jeg må si at jeg skjønte ikke mye av den numeriske løsningen her.

Hunt forklarte veldig nøye alt som trengtes å forstå for å løse problemet numerisk. Det var her jeg tok meste inspirasjonen fra, i tillegg til at den viktigste kodelinjen
hentet jeg herifra som er kommentert direkte i koden.

Når det gjelder selve python-kodingen og matplotlib bruken brukte jeg jevnlig matplotlib sin egen side: https://matplotlib.org/stable/, blant annet får å vise grafen og "colorbar"-en riktig og med farger jeg syntes passet. 




