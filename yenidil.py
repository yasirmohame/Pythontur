
class Tip:
    def __init__(self,obje_şey) -> None:
        self.obje_şey=obje_şey
    def __str__(self) -> None:
        return str(type(self.obje_şey))
class ondalık(int):
    def __float__(self) -> float:
        return super().__float__()
class Tamsayı(int):
    def __int__(self) -> int:
        return super().__int__()
def yaz(yazı):
    print(yazı)
class AÇ:
    def __init__(self,dosyaadı,mod) -> None:
        self.mod=mod
        self.dosyaadı=dosyaadı
        if mod=='o':
            self.bos=open(dosyaadı,'r')
        if mod=='y':
            self.bos=open(dosyaadı,'w')
    def yaz(self,yazı):
        return self.bos.write(yazı)
    def oku(self):
        return self.bos.read()