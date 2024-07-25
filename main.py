class calculator():
  def __init__(self):
    self.calısmadurmu = True

  
  def menu(self):
    print('''
    ------------
    1. Toplama
    2. Cıkarma
    3. Carpma
    4. Bolme
    5. cıkıs
    6. baska hesaplamalar
    
    ------------\n
    ''')

    while True:
      try:
        secim = int(input("yapmak istediginiz islem num: "))
        if secim == 1:
          self.toplama()
          break

        if secim == 2:
          self.cıkarma()
          break

        if secim == 3:
          self.carpma()
          break

        if secim == 4:
          self.bolme()
          break

        if secim == 5:
          self.cıkıs()
          break

        if secim == 6:
          self.digerislemler()
          break


      except ValueError:
        print("hatalı giriş yaptınız tekrar deneytiniz")

      
  def toplama(self):
    while True:
      try:
        total = 0
        sayılar = input("toplanacak sayıları giriniz\n")
        sayılar = sayılar.split(" ")
        for i in sayılar:
          total += float(i)
        print("sonuc\n", total)
        break
        
      except ValueError:
        float(input("lütfen sayı giriniz!\n"))

  
  def cıkarma(self):
    while True:
      try:
        total = 0
        sayılar = input("cıkarılacak sayıları giriniz\n")
        sayılar = sayılar.split(" ")
        for i in sayılar:
          total -= float(i)
        print("sonuc\n", total)
        break

      except ValueError:
        float(input("lütfen sayı giriniz!\n"))

  
  def carpma(self):
    while True:
      try:
        total = 0
        sayılar = input("carpılacak sayıları giriniz\n")
        sayılar = sayılar.split(" ")
        for i in sayılar:
          total *= float(i)
        print("sonuc\n", total)
        break

      except ValueError:
        float(input("lütfen sayı giriniz!\n"))

  
  def bolme(self):
    while True:
      try:
        total = 0
        sayılar = input("bolunecek sayıları giriniz\n")
        sayılar = sayılar.split(" ")
        for i in sayılar:
          total /= float(i)
        print("sonuc\n", total)
        break

      except ValueError:
        sayılar = float(input("lütfen sayı giriniz!\n"))
    

  def cıkıs(self):
     self.calısmadurmu = False

  
  # DİGER İSLEMLER MENUSU IS STARTING HERE #


  def fizik(self):
    import fizik
    fizik = fizik.fizik()
    return fizik.menu()
  

  def digerislemler(self):

    print('''
    ------------
    1- Fizik
    2- geri don
    ------------\n
    ''')

    while True:
      try:
        secim = int(input("yapmak istediginiz islem num: "))
        if secim == 1:
          self.calısmadurmu = False
          self.fizik()
          break

        if secim == 2:
          self.menu()
          break

        else:
          print("hatalı giriş yaptınız tekrar deneytiniz")

      except ValueError:
        print("hatalı giriş yaptınız tekrar deneytiniz")


calculator = calculator()

while calculator.calısmadurmu:
  calculator.menu()

