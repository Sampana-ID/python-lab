#!/usr/bin/python3

#############################################################
#
#                           PYTHON LAB
#############################################################
#                   tiny program for dictionary
#############################################################

import os
import sys

##bagian menu

def menu():
    menu = 0
    while(menu != 6) :
        print("""
                =========MENU=======
                1. Indonesia - Sunda
                2. Sunda - Indonesia
                3. Jawa - Indonesia
                4. Indonesia - Jawa
                5. About
                6. Keluar
                """)
        menu = int(input("masukan menu yang anda inginkan : "))
        arah(menu)

##pengarahan menu

def arah(menu):
    if (menu == 1) :
        translate("indo","sunda")
        
    elif (menu == 2) :
        translate("sunda","indo")
        
    elif (menu == 3) :
        translate("jawa","indo")
        
    elif (menu == 4) :
        translate("indo","jawa")
        
    elif (menu == 5) :
        about()

    elif (menu > 6) or (menu < 1) :
        print("masukan anda salah")
        menu()

##about menu

def about():
    print("""
            ================ABOUT==============
            aplikasi ini dibuat untuk percobaan
            dalam persiapan untuk pembuatan indo
            translator
        """)

##translate menu
    
def translate(awal, akhir) :
    sunda = {"makan" : "tuang","saya":"abi"}
    jawa = {"makan" : "dahar","saya":"kula"}
    
    frase = input("masukan kalimat : ")
    arrayfrase = frase.split(" ")

    for i in range(0, len(arrayfrase)) :
        if (awal == "indo") and (akhir == "sunda") :
            for j in sunda :
                if arrayfrase[i] == j :
                    arrayfrase[i] = sunda[j]

        elif (awal == "indo") and (akhir == "jawa"): 
            for j in jawa :
                if arrayfrase[i] == j :
                    arrayfrase[i] = jawa[j]
                    
        elif (awal == "sunda") and (akhir == "indo"): 
            for key in sunda :
                if arrayfrase[i] == sunda[key] :
                    arrayfrase[i] = key
                    
        elif (awal == "jawa") and (akhir == "indo"): 
             for key in jawa :
                if arrayfrase[i] == jawa[key] :
                    arrayfrase[i] = key

    frase = ' '.join(arrayfrase)
    print(frase)

##kerangka utama
    
def main():
    menu()
    
if __name__ == "__main__":
    main()
