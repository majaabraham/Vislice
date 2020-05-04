print(2)
print(3)
for i in range(4, 200):
    je_prastevilo = True
    for mozni_delitelj in range(2, i):
        if i % mozni_delitelj == 0:
            je_prastevilo = False

    if je_prastevilo:
        print(i)