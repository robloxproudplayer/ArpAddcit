#(x) Preguntarle al usuario si quiere ver sus interfaces para checar su ip address
#(x) Hacer un menu principal con todas las funciones

import scapy.all as scapy
import time
import subprocess

#Menu principal para que el usuario elija que funcion del programa usar
def Main_menu():
    subprocess.call(["clear"])
    print("Welcome to ArpAddictV0.2")
    time.sleep(2)
    subprocess.call(["clear"])
    def Main_menu_options():
        Selected_option = input("Choose an option\n\n(1) Arp network scanner\n(2) Exit\n\nInput: ")

        def Main_menu_selected_option_1():
            subprocess.call(["clear"])
            Option_1_are_you_sure = input("You selected option 1 (Arp network scanner), are you sure?\n\n(y) (n): ")
            if Option_1_are_you_sure == "y":
                subprocess.call(["clear"])
                print("Opening Arp network scanner...")
                time.sleep(1.5)
                subprocess.call(["clear"])
                Main_functions()
            elif Option_1_are_you_sure == "Y":
                subprocess.call(["clear"])
                print("Opening Arp network scanner...")
                time.sleep(1.5)
                subprocess.call(["clear"])
                Main_functions()
            elif Option_1_are_you_sure == "n":
                subprocess.call(["clear"])
                print("Going to main menu...")
                time.sleep(1.5)
                subprocess.call(["clear"])
                Main_menu_options()
            elif Option_1_are_you_sure == "N":
                subprocess.call(["clear"])
                print("Going to main menu...")
                time.sleep(1.5)
                subprocess.call(["clear"])
                Main_menu_options()
            else:
                subprocess.call(["clear"])
                print("Invalid option.")
                time.sleep(1.5)
                subprocess.call(["clear"])
                Main_menu_selected_option_1()
        def Main_menu_selected_option_2():
            Option_2_are_you_sure = input("You selected option 2 (Exit), are you sure?\n\n(y) (n): ")
            if Option_2_are_you_sure == "y":
                subprocess.call(["clear"])
                print("Exiting...")
                time.sleep(1.5)
                subprocess.call(["clear"])
                exit()
            elif Option_2_are_you_sure == "Y":
                subprocess.call(["clear"])
                print("Exiting...")
                time.sleep(1.5)
                subprocess.call(["clear"])
                exit()
            elif Option_2_are_you_sure == "n":
                subprocess.call(["clear"])
                print("Going to main menu...")
                time.sleep(1.5)
                subprocess.call(["clear"])
                Main_menu_options()
            elif Option_2_are_you_sure == "N":
                subprocess.call(["clear"])
                print("Going to main menu...")
                time.sleep(1.5)
                subprocess.call(["clear"])
                Main_menu_options()
            else:
                subprocess.call(["clear"])
                print("Invalid option.")
                time.sleep(1.5)
                subprocess.call(["clear"])
                Main_menu_selected_option_2()

        if Selected_option == "1":
            Main_menu_selected_option_1()
        elif Selected_option == "2":
            Main_menu_selected_option_2()
        else:
            subprocess.call(["clear"])
            print("Invalid option.")
            time.sleep(1.5)
            subprocess.call(["clear"])
            Main_menu_options()

    Main_menu_options()

#Si una de las funciones dentro de esta no funciona basicamente el programa perdera mucha funcionalidad
def Main_functions():
    #Explicacion sobre que hace cada funcion dentro de las funciones

    #This function is invoced inside "Ask_if_wanna_check_ip" function.
    def Ask_ip_address_range():
        #Input para que el usuario ponga el ip range a escanear deseado
        global ip_address
        ip_address = str(input("Enter ip address range\nExample: 192.168.100.1/24\n\nInput: "))

    #Con esta funcion se le pregunta al usuario si quiere ver que ip tiene
    def Ask_if_wanna_check_ip():
        subprocess.call(["clear"])
        Wanna_check_ip = input("Want to check your actual ip?\n\n(y) (n): ")
        if Wanna_check_ip == "y":
            subprocess.call(["clear"])
            subprocess.call(["ifconfig"])
            Close_ifconfig = input("\n\nPress enter to close.")
            if Close_ifconfig == "":
                subprocess.call(["clear"])
                Ask_ip_address_range()
            else:
                subprocess.call(["clear"])
                Ask_ip_address_range()
        elif Wanna_check_ip == "Y":
            subprocess.call(["clear"])
            subprocess.call(["ifconfig"])
            Close_ifconfig = input("\n\nPress enter to close.")
            if Close_ifconfig == "":
                subprocess.call(["clear"])
                Ask_ip_address_range()
            else:
                subprocess.call(["clear"])
                Ask_ip_address_range()
        elif Wanna_check_ip == "n":
            subprocess.call(["clear"])
            Ask_ip_address_range()
        elif Wanna_check_ip == "N":
            subprocess.call(["clear"])
            Ask_ip_address_range()
        else:
            subprocess.call(["clear"])
            print("Invalid option.")
            time.sleep(1.5)
            subprocess.call(["clear"])
            Ask_if_wanna_check_ip()
    Ask_if_wanna_check_ip()

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

#Con esta funcion arranca el programa
Main_menu()

