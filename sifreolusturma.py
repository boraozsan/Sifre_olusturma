import random

harfler = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
rakamlar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
semboller = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Güvenli Şifre Oluşturma Programına Hoşgeldiniz!")
nr_harfler= int(input("Şifrenizde kaç tane harf olsun?\n"))
nr_semboller = int(input("Şifrenizde kaç tane sembol olsun?\n"))
nr_rakamlar = int(input("Şifrenizde kaç tane rakam olsun?\n"))

toplam_karakter=nr_rakamlar+nr_semboller+nr_harfler
sifre_liste=[]
for harf in range(0,nr_harfler):
    x=random.randint(0,len(harfler)-1)
    sifre_liste.append(harfler[x])
for sembol in range(0,nr_semboller):
    x=random.randint(0,len(semboller)-1)
    sifre_liste.append(semboller[x])
for rakam in range(0,nr_rakamlar):
    x=random.randint(0,len(rakamlar)-1)
    sifre_liste.append(rakamlar[x])
random.shuffle(sifre_liste)
sifre=""
for n in range(0,toplam_karakter):
    sifre+=sifre_liste[n]

print(f"Güvenli şifreniz oluşturuldu.\nŞifreniz: {sifre}")