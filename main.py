class BankHisobi:
    def __init__(self, egasi, balans=0):
        self.egasi = egasi
        # __balans xususiy (private) deb belgilandi, tashqaridan to'g'ridan-to'g'ri o'zgartirib bo'lmaydi
        self.__balans = balans

    # Balansni ko'rish uchun getter metod
    def balansni_korish(self):
        return f"{self.egasi} ning hisobidagi mablag': {self.__balans} $"

    # Pul kiritish metodi
    def pul_kiritish(self, summa):
        if summa > 0:
            self.__balans += summa
            print(f"{summa} $ kiritildi.")
        else:
            print("Xato: Manfiy summa kiritish mumkin emas!")

    # Pul yechish metodi
    def pul_yechish(self, summa):
        if 0 < summa <= self.__balans:
            self.__balans -= summa
            print(f"{summa} $ yechib olindi.")
        else:
            print("Xato: Mablag' yetarli emas yoki noto'g'ri summa!")


# Meros olish (Inheritance): BankHisobi klassidan nusxa olamiz
class VIPBankHisobi(BankHisobi):
    def __init__(self, egasi, balans=0, keshbek_foiz=2):
        # Ota klassning __init__ metodini chaqirish
        super().__init__(egasi, balans)
        self.keshbek_foiz = keshbek_foiz

    # VIP mijozlar uchun xariddan keshbek qaytarish metodi
    def xarid_qilish(self, summa):
        keshbek = (summa * self.keshbek_foiz) / 100
        print(f"{summa} $ xarid qilindi. Keshbek: {keshbek} $")
        self.pul_kiritish(keshbek)
