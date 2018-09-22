apetece_helado_in = input("Te apetece un helado? (Si / No): ")
tienes_dinero_in = input("Tienes dinero para un helado? (Si / No): ")
esta_tu_tia_in = input("Esta tu tia? (Si / No): ")
esta_el_senor_de_los_helados_in = input("Esta el señor de los helados? (Si / No): ")

apetece_helado = apetece_helado_in == "Si"
tienes_dinero = tienes_dinero_in or esta_tu_tia_in == "Si"
esta_el_senor_de_los_helados = esta_el_senor_de_los_helados_in == "Si"


if apetece_helado and tienes_dinero and esta_el_senor_de_los_helados:
    print("Pues comete un puto helado")

else:
    print("Pues vete a tomar por el culo")
