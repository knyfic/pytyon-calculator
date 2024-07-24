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

    (sayıların arasında bosluk bıraklmasınız. orenk = "1 2 3"
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
        float(input("lütfen sayı giriniz!\n"))
    

  def cıkıs(self):
     self.calısmadurmu = False


calculator = calculator()

while calculator.calısmadurmu:
  calculator.menu()  
