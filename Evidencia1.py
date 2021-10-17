from collections import namedtuple

separador = "*" * 80
Articulo = namedtuple("Articulo", "descripcion cant_pzs precio_venta importe")
Ticket = namedtuple("Ticket", "fecha articulos monto_total iva_total ")
registro_ventas = {} # Diccionario que contendrá todos los tickets

while True:
    print(separador)
    print("Menú principal\n")
    print("1. Registrar una venta.\n")
    print("2. Consultar una venta.\n")
    print("3. Salir\n")
    
    print(separador)
    respuesta = int(input("Escribe el número con la opción que deseas realizar: \n"))
    print(separador)
    
    if respuesta == 1:
        print("Registrar una venta.\n")
        while True: #Validar que el folio no se repita
            folio = int(input("Folio: "))
            if folio in registro_ventas.keys():
                print('Este folio de venta ya existe, porfavor ingresa otro diferente.\n')
            else:
                break
        
        fecha = input("Fecha (DD/MM/YYYY): ")
        articulos = {} # Aqui se guardaran todos los articulos del ticket
        subtotal = 0
        num_art = 0  # Identificador de Articulos
        while True:
            num_art += 1
            descripcion = input("Descripción del Articulo: ")
            cant_pzs = int(input("Cantidad: "))
            precio_venta = float(input("Precio de venta: "))
            
            importe = round(cant_pzs * precio_venta,2)
            
            #Agregar el articulo registrado al ticket
            articulos[num_art] = Articulo(descripcion, cant_pzs, precio_venta, importe)
            
            subtotal += importe
            print(separador)
            print(f"Importe: ${importe}")
            print(separador)
            
            seguir_registrando = int(input("¿Seguir registrando articulos? Si=1, No=0: "))
            if seguir_registrando == 0:
                iva_total = round(subtotal * 0.16,2)
                monto_total = round(subtotal + iva_total,2)
                print(separador)
                print(f"Subtotal: ${subtotal}")
                print(f"+ IVA 16%: ${iva_total}")
                print(f"Monto total del ticket después de impuestos: ${monto_total}")
    
                #Agregar el ticket al registro de las ventas         
                registro_ventas[folio] = Ticket(fecha,articulos,monto_total,iva_total)
                break
     
    elif respuesta == 2:
        folio_consulta = int(input("Escriba el folio de la venta a consultar: "))
        print(separador)
        
        if folio_consulta in registro_ventas.keys():
            print(f"Folio del ticket: {folio_consulta}\n")
            print(f'Fecha: {registro_ventas[folio_consulta].fecha}')
            print(f'{"Cant pzs":<5} | {"Descripcion":<10} | {"Precio venta":<15} | {"Total":<20} \n')
            art_ticket = registro_ventas[folio_consulta].articulos
            for n in art_ticket.keys():
                print(f"{art_ticket[n].cant_pzs:<8} | {art_ticket[n].descripcion:<11} | ${art_ticket[n].precio_venta:<14} | ${art_ticket[n].importe:<20}")
            print(separador)
            print(f"IVA (16%): {(registro_ventas[folio_consulta].iva_total)}")
            print(f'Total de la venta: {registro_ventas[folio_consulta].monto_total}')
        else:
            print("El folio ingresado no existe, favor de verficarlo")
    elif respuesta == 3:
        break
    else:
        print("Respuesta no válida.")
