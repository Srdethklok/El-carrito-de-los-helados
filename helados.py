apetece_helado_in = input("Te apetece un helado? (Si / No): ").upper()

if apetece_helado_in == "SI":
    apetece_helado = True

elif apetece_helado_in == "NO":
    apetece_helado = False

else:
    print("No entiendo lo que dices")

tienes_dinero_in = input("Tienes dinero para un helado? (Si / No): ").upper()

if tienes_dinero_in == "SI":
    tienes_dinero = True

elif tienes_dinero_in == "NO":
       tienes_dinero = False
       print("que te invite tu tia")


esta_tu_tia_in = input("Esta tu tia? (Si / No): ").upper()

if esta_tu_tia_in == "SI":
    esta_tu_tia_ = True

elif esta_tu_tia_in == "NO":
      esta_tu_tia = False

else:
    print("pues sin dinero ni a nadie que pueda invitarte...")



esta_el_senor_de_los_helados_in = input("Esta el señor de los helados? (Si / No): ").upper()

if esta_el_senor_de_los_helados_in == "SI":
    esta_el_senor_de_los_helados = True

elif esta_el_senor_de_los_helados_in == "NO":
     esta_el_senor_de_los_helados = False
     print("el heladero no esta, asi que vete a casa")


apetece_helado = apetece_helado_in == "SI"
tienes_dinero = tienes_dinero_in or esta_tu_tia_in == "SI"
esta_el_senor_de_los_helados = esta_el_senor_de_los_helados_in == "SI"


if apetece_helado and tienes_dinero and esta_el_senor_de_los_helados:
    print("Pues comete un helado")

else:
    print("vete ")
