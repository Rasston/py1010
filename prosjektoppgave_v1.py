"""
Prosjektoppgave PY1010
Sander Ryen Sundt
sandersundt@outlook.com
@author: Sander
"""

# %% import av pakker

import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta

# %% del a - import av fil

support_uke_24 = pd.read_excel('support_uke_24.xlsx')

u_dag = support_uke_24['Ukedag'].to_numpy()
kl_slett = support_uke_24['Klokkeslett'].to_numpy()
varighet = support_uke_24['Varighet'].to_numpy()
score = support_uke_24['Tilfredshet'].to_numpy()

# %% del b - visualisering antall henvendelser pr dag

antall_pr_dag = support_uke_24['Ukedag'].value_counts()

plt.figure(figsize=(8, 5))
antall_pr_dag.plot(kind='bar')
plt.xlabel('Ukedag')
plt.ylabel('Antall henvendelser')
plt.title('Antall henvendelser uke 24, fordelt på ukedager')
plt.show()

# %% del c - minste og lengste samtaletid

korteste_samtale = min(varighet)
print('Korteste samtale i uke 24 varte', korteste_samtale)

lengste_samtale = max(varighet)
print('Lengste samtale i uke 24 varte', lengste_samtale)

# %% del d - gjennomsnittlig samtaletid

# omformattere array til timedelta-objekter
samtalelengde = [timedelta(hours=int(t.split(':')[0]),
                           minutes=int(t.split(':')[1]),
                           seconds=int(t.split(':')[2]))
                 for t in varighet]

# regne ut gjennomsnittlig samtalevarighet
gjennomsnittlig_lengde = sum(samtalelengde, timedelta()) / len(varighet)

# formattere ut-data
timer, rest = divmod(gjennomsnittlig_lengde.total_seconds(), 3600)
minutter, sekunder = divmod(rest, 60)

print(f'Gjennomsnittlig samtalevarighet er{int(minutter):2} minutter og\
 {int(sekunder):2} sekunder.')

# %% del e - samtaler pr vakt

forste_vakt = 0
andre_vakt = 0
tredje_vakt = 0
siste_vakt = 0

tidspunkt = pd.to_datetime(support_uke_24['Klokkeslett'], format='%H:%M:%S')

for a in tidspunkt:
    if (pd.to_datetime('08:00:00', format='%H:%M:%S')) < a < \
       (pd.to_datetime('10:00:00', format='%H:%M:%S')):
        forste_vakt += 1
    elif (pd.to_datetime('10:00:00', format='%H:%M:%S')) < a < \
         (pd.to_datetime('12:00:00', format='%H:%M:%S')):
        andre_vakt += 1
    elif (pd.to_datetime('12:00:00', format='%H:%M:%S')) < a < \
         (pd.to_datetime('14:00:00', format='%H:%M:%S')):
        tredje_vakt += 1
    else:
        siste_vakt += 1

vakter = ([forste_vakt, andre_vakt, tredje_vakt, siste_vakt])
navn = (['kl 8 - 10', 'kl 10 - 12', 'kl 12 - 14', 'kl 14 - 16'])

plt.pie(vakter)
plt.legend(title='Vakt:', labels=navn)
plt.show()

# %% del f - tilfredshet
negative = 0
noytrale = 0
positive = 0
antall = 0

for i in score:
    if 1 <= i <= 6:
        negative += 1
        antall += 1
    if 7 <= i <= 8:
        noytrale += 1
        antall += 1
    if 9 <= i:
        positive += 1
        antall += 1

nps = (positive/antall) - (negative/antall)

print(f'NPS for supportavdelingen i uke 24 er {nps*100:.1f} %')
