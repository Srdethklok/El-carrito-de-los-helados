apetece_helado_in = input("Te apetece un helado? (Si / No): ").upper()

if apetece_helado_in == "SI":
    apetece_helado = True

elif apetece_helado_in == "NO":
    apetece_helado = False

else:
    print("No se que me estas contando pero adios")

tienes_dinero_in = input("Tienes dinero para un helado? (Si / No): ").upper()
esta_tu_tia_in = input("Esta tu tia? (Si / No): ").upper()
esta_el_senor_de_los_helados_in = input("Esta el señor de los helados? (Si / No): ").upper()

apetece_helado = apetece_helado_in == "SI"
tienes_dinero = tienes_dinero_in or esta_tu_tia_in == "SI"
esta_el_senor_de_los_helados = esta_el_senor_de_los_helados_in == "SI"


if apetece_helado and tienes_dinero and esta_el_senor_de_los_helados:
    print("Pues comete un puto helado")

else:
    print("Pues vete a tomar por el culo")
