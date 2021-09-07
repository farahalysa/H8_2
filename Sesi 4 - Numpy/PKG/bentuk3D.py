def balok():
    "Fungsi menghitung balok"
    panjang = int(input("Masukkan nilai panjang"))
    lebar = int(input("Masukkan nilai lebar"))
    tinggi = int(input("Masukkan nilai tinggi"))
    volume_balok = int(panjang) * int(lebar) * int(tinggi)
    luas_permukaan_balok = 2 * (panjang * tinggi + panjang * lebar + lebar * tinggi)
    print("Panjang balok = ", panjang)
    print("Lebar balok = ", lebar)
    print("Tinggi balok = ", tinggi)
    print("Volume balok = ", volume_balok)
    print("Luas permukaan balok = ", luas_permukaan_balok)
    
def kubus():
    "Fungsi menghitung kubus"
    sisi = int(input("Masukkan nilai sisi: "))
    volume_kubus = int(sisi) * int(sisi) * int(sisi)
    luas_permukaan_kubus = 6*int(sisi)*int(sisi)
    print("Sisi kubus = ", sisi)
    print("Volume kubus = ", volume_kubus)
    print("Luas permukaan kubus = ", luas_permukaan_kubus)

def tabung():
    "Fungsi menghitung tabung"
    jari_jari = int(input("Masukkan nilai jari-jari: "))
    tinggi = int(input("Masukkan nilai tinggi: "))
    volume_tabung = (22/7) * float(jari_jari) * float(jari_jari) * tinggi
    print("Jari-jari tabung = ", jari_jari)
    print("Tinggi tabung = ", tinggi)
    print("Volume tabung = ", volume_tabung)