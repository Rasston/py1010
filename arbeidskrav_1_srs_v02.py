"""
Created on Sat Oct 26 15:47:31 2024

@author: Sander Ryen Sundt, epost: sandersundt@outlook.com

Arbeidskrav 1 PY 1010

Sist oppdatert 1.11.24
"""
# %% Faste verdier for begge kjoeretoey

K = 10000  # Kjoerelengde
TAD = 8.38  # Trafikkforsikringsavgift pr dag
TAA = TAD*365  # Trafikkforsikringsavgift pr år

# %% Utgifter elbil

FE = 5000  # Aerlig utgift forsikring elbil
SF = 0.2  # Stroemforbruk i kWh pr km elbil
SP = 2.00  # Stroempris pr kWh
DUE = SF*SP*K  # Aerlig utgift drivstoff elbil
BE = 0.1  # Utgift bomavgift pr km elbil
BEK = BE*K  # Utgift bomavgift pr aer elbil
SUE = FE + DUE + BEK + TAA  # Samlede utgifter pr aer elbil

# %% Utgifter bensinbil

FB = 7500  # Aerlig utgift forsikring bensinbil
DB = 1.0  # Utgift drivstoff pr km bensinbil
DUB = DB*K  # Aerlig utgift drivstoff bensinbil
BB = 0.3  # Utgift bomavgift pr km bensinbil
BBK = BB*K  # Utgift bomavgift pr aer bensinbil
SUB = FB + DUB + BBK + TAA  # Samlede utgifter pr aer bensinbil

# %% Utskrift og sammenligning

print("Samlede aerlige utgifter elbil:", SUE)
print("Samlede aerlige utgifter bensinbil:", SUB)
print("Forskjell samlede utgifter:", SUB - SUE)

print("Utgifter drivstoff pr aer bensinbil:", DUB)
print("Utgifter drivstoff pr aer elbil:", DUE)
print("Forskjell drivstoffutgifter:", DUB - DUE)

print("Utgifter bomavgift pr aer bensinbil:", BB*K)
print("Utgifter bomavgift pr aer elbil:", BE*K)
print("Forskjell utgifter bomavgift:", BB*K - BE*K)

print("Utgift forsikring bensinbil:", FB)
print("Utgift forsikring elbil:", FE)
print("Forskjell utgift forsikring:", FB - FE)
