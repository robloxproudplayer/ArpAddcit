#(x) Preguntarle al usuario si quiere ver sus interfaces para checar su ip address
#(x) Hacer un menu principal con todas las funciones

import scapy.all as scapy

#Si una de las funciones dentro de esta no funciona basicamente el programa perdera mucha funcionalidad
def Main_functions():
    #Explicacion sobre que hace cada funcion dentro de las funciones

    def Ask_ip_address_range():
        #Input para que el usuario ponga el ip range a escanear deseado
        global ip_address
        ip_address = str(input("Enter ip address range\nExample: 192.168.100.1/24\n\nInput: "))
    Ask_ip_address_range()

    def Function_arp_request_packet():
        #Funcion de scapy que hace arp requests y mas adelante el rango preferido
        global arp_request_packet
        arp_request_packet = scapy.ARP(pdst=ip_address)
    Function_arp_request_packet()

    def Function_broadcast_packet():
        #Funcion de scapy que hace que aparte de agarrar la ip tambien agarre el mac address
        global broadcast_packet
        broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    Function_broadcast_packet()

    def Function_combined_packet():
        #Funcion de scapy que con "/" combina las dos funciones anteriores para que funcionen juntas y solo sean una
        global combined_packet
        combined_packet = broadcast_packet/arp_request_packet
    Function_combined_packet()

    def Function_filter_answered_filter_unanswered():
        #Funcion de scapy que filtra la answered_list osea las arp request que fueron respondidas y las que no, y esa informacion la filtra del
        #paquete combinado de arriba, y con "scapy.srp()" ejecuta su funcion mas con "timeout=" logra que si un paquete no responde
        #no se quede estancado intentandolo infinitamente.
        global answered_list
        global unanswered_list
        (answered_list,unanswered_list) = scapy.srp(combined_packet,timeout=1)
    Function_filter_answered_filter_unanswered()

    def Function_print_filter_relevant_information():
        #Funcion de scapy que da la informacion mas relevante y mas leeible para el usuario, automaticamente la imprime.
        answered_list.summary()
    Function_print_filter_relevant_information()
Main_functions()
