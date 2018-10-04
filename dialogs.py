#!/usr/bin/python
# -*- coding: utf-8 -*-
a = input("Cienījamais lietotāji, lūdzu, ievadi skaitli: ")
#3. python'ā visi input rezultāti ir as str datu tipu
#tapēc ievadīta lieluma datu tips vēlāk
a = int(a)
print("Liet., Tu esi iavadījis skaitli: %d"%(a))
aa = a * a
print  ("Tavs skaitlis kvadrātā ir: %d"%(aa))
