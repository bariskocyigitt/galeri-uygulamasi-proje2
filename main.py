import os

def galeri_listesi_sec():
    list_name= input("Galeri adını giriniz(Örnek: BKmotors): ").strip()
    filename= list_name + ".txt"
    
    if os.path.exists(filename):
        print(f"{filename} bulundu. Bu liste kullanılacak. ")

    else:
        secim=input(f"{filename} bulunamadı. Yeni bir liste olusturulsun mu? (evet/hayır):").strip().lower()
        if secim=="evet":
            with open(filename,"w") as f:
                print(f"Yeni liste {filename} olusturuldu.")
        else:
            print("İslem iptal edildi. ")
            return None
        
    return filename

def araba_ekle(dosya_adi):
    marka=input("Arabanın markası: ").strip()
    model=input("Arabanın modeli: ").strip()
    fiyat=input("Arabanın fiyatı(TL)=").strip()
    
    if not marka or not model or not fiyat:
        print("Eksik bilgi girildi. Araba eklenemedi. ")
        return
    bilgi= f"{marka}-{model}-{fiyat}TL"
    
    with open(dosya_adi,"a") as f:
        f.write(bilgi+"\n")
    
    print(f"{bilgi} başarıyla eklendi.")

def araba_sil(dosya_adi):
    try:
        with open(dosya_adi,"r") as f:
            arabalar=f.readlines()
        
        if not arabalar:
            print("Galeride silinecek araba bulunamadı..")
            return
        
        print("\n Silinecek araba listesi: ")
        for i, araba in enumerate(arabalar,start=1):
            print(f"{i}. {araba.strip()}")
        
        secim=input("Silmek istediğiniz arabanın numarasını giriniz ").strip()
        
        if not secim.isdigit() or int(secim)<1 or int(secim)>len(arabalar):
            print("Gecersiz numara.")
            return
        
        silinecek=arabalar.pop(int(secim)-1)
        
        with open(dosya_adi,"w") as f:
            f.writelines(arabalar)
        print(f" {silinecek.strip()} başarıyla silindi..")
        
    except FileNotFoundError:
        print("Dosya bulunamadı.")
        
        
def arabalari_listele(dosya_adi):
            try:
                with open(dosya_adi,"r") as f:
                    arabalar=f.readlines()
                if not arabalar:
                    print("Galeride henuz kayıtlı araba yok. ")
                else:
                    print("\n Galerideki Arabalar: ")
                    for index,araba in enumerate(arabalar,start=1):
                        print(f"{index}.{araba.strip()}")
            except FileNotFoundError:
                print("Liste dosyası bulunamadı..")
        
        
        
        
        
        
def menu(dosya_adi):
    while True:
        print("\n ---------------Galeri Menusu------------")  
        print("1- Galeriye araba ekle")
        print("2- Galeriden araba cıkar")
        print("3- Galerideki arabaları listele")  
        print("4- Cıkıs")
        
        secim=input("Lutfen bir islem secin(1-4): ").strip()
        
        if secim=="1":
            araba_ekle(dosya_adi)
        elif secim=="2":
            araba_sil(dosya_adi)
        elif secim=="3":
            arabalari_listele(dosya_adi)
        elif secim=="4":
            print("Cıkıs yapılıyor... Hoscakal...")
            break
        else:
            print("Gecersiz secim lutfen 1 ile 4 arasında bir sey seciniz.")

dosya_adi= galeri_listesi_sec()

if dosya_adi:
    menu(dosya_adi)
