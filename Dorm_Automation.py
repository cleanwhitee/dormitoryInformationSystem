from queue import Queue

class Dorm_Automation:
    def __init__(self):
        self.students_stack = []
        self.izin_kuyruklari = {}  

    def ogrenci_ekle(self):
        ad = input("Öğrenci adı: ")
        soyad = input("Öğrenci soyadı: ")
        oda_no = input("Oda numarası: ")
        izin_gunu = 0
        ucret_odendi = input("Ücret ödendi mi? (Evet/Hayır): ").lower() == "evet"

        ogrenci = {
            "ad": ad,
            "soyad": soyad,
            "oda_no": oda_no,
            "izin_gunu": izin_gunu,
            "ucret_odendi": ucret_odendi,
            "izin_aliyor": False,
            "yemek_yedi": False,
        }

        self.izin_kuyruklari[id(ogrenci)] = Queue()

        self.students_stack.append(ogrenci)
        print(f"{ad} {soyad} başarıyla eklendi.")

    def izin_gunu_azalt(self):
        if not self.students_stack:
            print("Dolulukta öğrenci bulunmamaktadır.")
            return

        index = len(self.students_stack) - 1
        ogrenci = self.students_stack[index]

        if ogrenci["izin_aliyor"]:

            ogrenci_id = id(ogrenci)
            if not self.izin_kuyruklari[ogrenci_id].empty():
                ogrenci["izin_gunu"] = self.izin_kuyruklari[ogrenci_id].get()
                print(f"{ogrenci['ad']} {ogrenci['soyad']} için izin günü azaltıldı. Yeni izin günü: {ogrenci['izin_gunu']}")
            else:
                print(f"{ogrenci['ad']} {ogrenci['soyad']} için kullanılabilir izin günü kalmadı.")
        else:
            print(f"{ogrenci['ad']} {ogrenci['soyad']} izin almadığı için izin günü azaltılamaz.")

    def izin_al(self):
        if not self.students_stack:
            print("Dolulukta öğrenci bulunmamaktadır.")
            return

        index = len(self.students_stack) - 1
        ogrenci = self.students_stack[index]

        ogrenci_id = id(ogrenci)
        self.izin_kuyruklari[ogrenci_id].put(ogrenci["izin_gunu"])
        ogrenci["izin_aliyor"] = True
        print(f"{ogrenci['ad']} {ogrenci['soyad']} izin aldı. İzin günü kuyruğa eklendi.")

    def ogrenci_cikisi(self):
        if not self.students_stack:
            print("Dolulukta öğrenci bulunmamaktadır.")
            return

        cikan_ogrenci = self.students_stack.pop()
        print(f"{cikan_ogrenci['ad']} {cikan_ogrenci['soyad']} çıkış yapıldı.")

    def ogrenci_bilgilerini_goster(self):
        if not self.students_stack:
            print("Dolulukta öğrenci bulunmamaktadır.")
            return

        index = len(self.students_stack) -1  
        ogrenci = self.students_stack[index]

        sorgula = Sorgula()
        print("Öğrenci Bilgileri:")
        print(f"Ad: {ogrenci['ad']}")
        print(f"Soyad: {ogrenci['soyad']}")
        print(f"Oda Numarası: {ogrenci['oda_no']}")
        print(f"İzin Günü: {ogrenci['izin_gunu']}")
        print(sorgula.ucret_odendi_mi(ogrenci))
        print(f"Yemek Yedi: {'Evet' if ogrenci['yemek_yedi'] else 'Hayır'}")

    def oda_bilgilerini_goster(self):
        if not self.students_stack:
            print("Dolulukta öğrenci bulunmamaktadır.")
            return

        print("Oda Bilgileri:")
        for i, ogrenci in enumerate(self.students_stack):
            print(f"Oda {i + 1} - {ogrenci['ad']} {ogrenci['soyad']}") #girilen oda bilgilerine göre düzelt
            
    def ogrenci_sil(self):
        if not self.students_stack:
            print("Dolulukta öğrenci bulunmamaktadır.")
            return

        index = len(self.students_stack) -1  
        silinen_ogrenci = self.students_stack.pop(index)
        print(f"{silinen_ogrenci['ad']} {silinen_ogrenci['soyad']} silindi.")

    def ucret_odendi_sorgula(self):
        if not self.students_stack:
            print("Dolulukta öğrenci bulunmamaktadır.")
            return

        index = len(self.students_stack) -1  
        if self.students_stack[index]["ucret_odendi"]:
            print("Ücret ödendi.")
        else:
            print("Ücret ödenmedi.")


    def yemek_yedi_olarak_isaretle(self):
        if not self.students_stack:
            print("Dolulukta öğrenci bulunmamaktadır.")
            return

        index = len(self.students_stack) -1  
        self.students_stack[index]["yemek_yedi"] = True
        print("Yemek yedi olarak işaretlendi.")

    def yemek_yiyenleri_goster(self):
        if not self.students_stack:
            print("Dolulukta öğrenci bulunmamaktadır.")
            return

        yemek_yiyenler = [ogrenci for ogrenci in self.students_stack if ogrenci["yemek_yedi"]]
        if not yemek_yiyenler:
            print("Yemek yiyen öğrenci bulunmamaktadır.")
        else:
            print("Yemek Yiyen Öğrenciler:")
            for ogrenci in yemek_yiyenler:
                print(f"{ogrenci['ad']} {ogrenci['soyad']}")
                                
    def ucret_odendi_olarak_isaretle(self):
        if not self.students_stack:
            print("Dolulukta öğrenci bulunmamaktadır.")
            return

        index = len(self.students_stack) -1  
        self.students_stack[index]["ucret_odendi"] = True
        print("Ücret ödendi olarak işaretlendi.")

    def ucret_odendi_olanlari_goster(self):
        if not self.students_stack:
            print("Dolulukta öğrenci bulunmamaktadır.")
            return

        ucret_odendi_olanlar = [ogrenci for ogrenci in self.students_stack if ogrenci["ucret_odendi"]]
        if not ucret_odendi_olanlar:
            print("Ücret ödemiş öğrenci bulunmamaktadır.")
        else:
            print("Ücret Ödemiş Öğrenciler:")
            for ogrenci in ucret_odendi_olanlar:
                print(f"{ogrenci['ad']} {ogrenci['soyad']}")

class Sorgula(Dorm_Automation):
    def ucret_odendi_mi(self, ogrenci):
        if ogrenci["ucret_odendi"]:
            return "Ücret ödendi."
        else:
            return "Ücret ödenmedi."

    def izin_alabilir_mi(self, ogrenci):
        if ogrenci["izin_aliyor"]:
            return "İzin alabilir."
        else:
            return "İzin alamaz."


girls_dorm = Dorm_Automation()

while True:
    print("\nGirls Dorm Automation Menu:")
    print("1. Öğrenci Ekle")
    print("2. Öğrenci Çıkışı")
    print("3. İzin Günü Azalt")
    print("4. Öğrenci Bilgilerini Göster")
    print("5. Oda Bilgilerini Göster")
    print("6. Öğrenci Sil")
    print("7. Ücret Ödendi Sorgula")
    print("8. İzin Al")
    print("9. Yemek Yedi Olarak İşaretle")
    print("10. Yemek Yiyenleri Göster")
    print("11. Ücret Ödendi Olarak İşaretle")
    print("12. Ücret Ödendi Olanları Göster")  
    print("0. Çıkış")

    choice = input("Seçiminizi yapınız: ").lower()

    if choice == "1":
        girls_dorm.ogrenci_ekle()
    elif choice == "2":
        girls_dorm.ogrenci_cikisi()
    elif choice == "3":
        girls_dorm.izin_gunu_azalt()
    elif choice == "4":
        girls_dorm.ogrenci_bilgilerini_goster()
    elif choice == "5":
        girls_dorm.oda_bilgilerini_goster()
    elif choice == "6":
        girls_dorm.ogrenci_sil()
    elif choice == "7":
        girls_dorm.ucret_odendi_sorgula()
    elif choice == "8":
        girls_dorm.izin_al()
    elif choice == "9":
        girls_dorm.yemek_yedi_olarak_isaretle()
    elif choice == "10":
        girls_dorm.yemek_yiyenleri_goster()
    elif choice == "11":
        girls_dorm.ucret_odendi_olarak_isaretle()
    elif choice == "12":
        girls_dorm.ucret_odendi_olanlari_goster()
    elif choice == "0":
        print("Programdan çıkılıyor.")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")



