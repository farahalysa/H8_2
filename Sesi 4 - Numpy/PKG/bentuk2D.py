def segiempat():
    "Fungsi menghitung segiempat"
    panjang = int(input("Masukkan nilai panjang"))
    lebar = int(input("Masukkan nilai lebar"))
    keliling_segiempat = 2*int(panjang) + 2*int(lebar)
    luas_segiempat = int(panjang) * int(lebar)
    print("Panjang segiempat = ", panjang)
    print("Lebar segiempat = ", lebar)
    print("Keliling segiempat = ", keliling_segiempat)
    print("Luas segiempat = ", luas_segiempat)
    
def segitiga():
    "Fungsi menghitung segitiga"
    alas = int(input("Masukkan nilai alas: "))
    tinggi = int(input("Masukkan nilai tinggi: "))
    luas_segitiga = 1/2*int(alas)*int(tinggi)
    print("Alas segitiga = ", alas)
    print("Tinggi segitiga = ", tinggi)
    print("Luas segitiga = ", luas_segitiga)

def persegi():
    "Fungsi menghitung persegi"
    sisi = int(input("Masukkan nilai sisi: "))
    keliling_persegi = 4*int(sisi)
    luas_persegi = int(sisi)*int(sisi)
    print("Sisi persegi = ", sisi)
    print("Keliling persegi = ", keliling_persegi)
    print("Luas persegi = ", luas_persegi)
    
def lingkaran():
    "Fungsi menghitung lingkaran"
    jari_jari = int(input("Masukkan nilai jari-jari: "))
    keliling_lingkaran = 2*(22/7)*float(jari_jari)
    luas_lingkaran = (22/7)*float(jari_jari)*float(jari_jari)
    print("Jari-jari lingkaran = ", jari_jari)
    print("Keliling lingkaran = ", keliling_lingkaran)
    print("Luas lingkaran = ", luas_lingkaran)