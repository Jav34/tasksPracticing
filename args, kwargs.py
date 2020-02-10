def kalkulator_malowania(farba_litr_per_m2, *pokoje):

    powierzchnia_cakowita = sum(pokoje)
    malowanie = powierzchnia_cakowita * farba_litr_per_m2
    return malowanie

print(kalkulator_malowania(0.25, 42, 28, 30))

pokoje = [42, 28, 30]
print(kalkulator_malowania(0.25, *pokoje))