"""
Onko annettu vuosi karkausvuosi?

Algoritmi 1:
JOS vuosi on jaollinen 400:lla ->
    ON karkausvuosi
MUUTEN JOS vuosi on jaollinen 100:lla ->
    EI ole karkausvuosi
MUUTEN JOS vuosi on jaollinen 4:lla ->
    ON karkausvuosi
MUUTEN ->
    EI ole karkausvuosi

Algoritmi 2:
JOS vuosi on jaollinen 400:lla TAI
(vuosi EI ole jaollinen 100:lla JA vuosi ???)  ->
    vuosi ON karkausvuosi
MUUTEN
    vuosi EI ole karkausvuosi
"""

# Testaa ratkaisusi ainakin arvoilla:
# 1900 -> EI ole
# 2000 -> KYLLÄ
# 2024 -> KYLLÄ
# 2026 -> EI