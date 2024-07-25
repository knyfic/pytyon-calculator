class fizik():
  def __init__(self):
    self.calısmadurmu = True


  def menu(self):
    print('''
    ------------
    1- alınan yol (hız, zaman)
    2- geri don
    ------------\n
    ''')

    while True:
      try:
        secim = int(input("yapmak istediginiz islem num: "))
        if secim == 1:
          self.yol()
          break

        if secim == 2:
          self.calısmadurmu = False
          self.anamenu()
          break

      except ValueError:
        print("hatalı giriş yaptınız tekrar deneytiniz")

  def yol(self):
    while True:
      try:
        hız = float(input("hızı giriniz (metre/x): "))
        zaman = float(input("zamanı giriniz(x): "))
        yol = hız * zaman
        print("yol: ", yol, "metre")
        break

      except ValueError:
        print("lütfen sayı giriniz!\n")
        return self.yol()

  
  def anamenu(self):
    import main
    calculator = main.calculator()
    return calculator.digerislemler()



fizik = fizik()

while fizik.calısmadurmu:
  fizik.menu()


