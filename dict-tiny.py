#!/usr/bin/python3

#############################################################
#
#                           PYTHON LAB
#############################################################
#                   tiny program for dictionary
#############################################################

import os
import sys

sunda = {"makan" : "tuang","saya":"abi"}
jawa = {"makan" : "dahar","saya":"kula"}

##bagian menu

def menu():
    menu = 0
    while(menu != 7) :
        print("""
                =========MENU=======
                1. Indonesia - Sunda
                2. Sunda - Indonesia
                3. Jawa - Indonesia
                4. Indonesia - Jawa
                5. Tambah data
                6. About
                7. Keluar
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
        tambah()

    elif (menu == 6) :
        about()

    elif (menu > 7) or (menu < 1) :
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

##tambah data
def tambah() :
    print("""
            ==============INPUT DATA===========
            1. Indo - Sunda
            2. Indo - Jawa
          """)
    bahasa = int(input("masukan bahasa (sesuai urutan)"))
    batas = int(input("berapa data yang ingin diinputkan"))
    if (bahasa == 1) :
        tambah_data("indo","sunda",batas)
    elif (bahas == 2) :
        tambah_data("indo","jawa",batas)
        
def tambah_data(awal,akhir,batas):
    for i in range(1,batas) :
        ky = input("masukan kata ("+awal+") : ")
        val = input("masukan kata ("+akhir+") : ")
        akhir[ky] = val
        print("data ditambahkan : "+awal+" berarti "+akhir)
    print("penginputan data selesai")
##translate menu
    
def translate(awal, akhir) :

    
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
