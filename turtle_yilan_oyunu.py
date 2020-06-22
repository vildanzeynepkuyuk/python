import turtle
import time
import random

# oyun hızı içi sabit bir başlangıç gecikme değeri belirleyelim
DELAY_FOR_SPEED = 0.1

# oyun alanı sınırlarına ilişkin sabitleri yaratalım
GAME_SCREEN_WIDTH = 800
GAME_SCREEN_HEIGHT = 800

# yılan ve yemlerin oyun sınırlarından 10 birim beriye yerleşmesi için
# emniyetli bölge sınırlarına ilişkin sabit değişkenlerimizi oluşturalım.
BORDER_SAFE_UP = GAME_SCREEN_HEIGHT / 2 - 10
BORDER_SAFE_DOWN = -1 * GAME_SCREEN_HEIGHT / 2 + 10
BORDER_SAFE_LEFT = -1 * GAME_SCREEN_WIDTH / 2 + 10
BORDER_SAFE_RIGHT = GAME_SCREEN_WIDTH / 2 - 10


# oyun hızını belirleyen gecikme değerimizi, başlangıç sabit gecikme değerine eşitleyelim
delay = DELAY_FOR_SPEED

# yılanın kuyruğu olsun, ama ilk başta kuyruğu olmasın
kuyruk = []

# score değerlerimizi başlangıçta sıfırlayalım
score = 0
bestScore = 0
currentScore = 0

#oyun ekranını oluşturalım
gameScreen = turtle.Screen()
gameScreen.title("Yılan Oyunu")
gameScreen.bgcolor("green")
gameScreen.setup(width = GAME_SCREEN_WIDTH, height = GAME_SCREEN_HEIGHT)
gameScreen.tracer(0); #ekran güncellemelerini kapatıyor

#Yılanın başını yaratalım, kare, ortada, siyah olsun, yönü olmasın dursun.
kafa = turtle.Turtle()
kafa.speed(0)
kafa.shape("square")
kafa.color("black")
kafa.penup()
kafa.goto(0,0)
kafa.direction= "stop"

# Hedefi(yemi) yaratalım, yuvarlak, ve kırmızı olsun, koordinatı rasgele yerleşsin
yem = turtle.Turtle()
yem.speed(0)
yem.shape("circle")
yem.color("dark blue")
yem.penup()
x = random.randint(BORDER_SAFE_LEFT, BORDER_SAFE_RIGHT)
y = random.randint(BORDER_SAFE_DOWN, BORDER_SAFE_UP)
yem.goto(x,y)

# skor tabelasını yaratalım
tabela = turtle.Turtle()
tabela.speed(0)
tabela.shape("square")
tabela.color("white")
tabela.penup()
tabela.hideturtle()
tabela.goto(0, BORDER_SAFE_UP - 30)
tabela.write("Score=0   Best Score=0", align="center", font=("courier", 24, "normal"))



# Yılanın kuyruğunu hareket ettiren fonksiyon
def kuyruk_hareket():

    # her kuyruk parçası bir öncekinin yerine geçsin
    for index in range(len(kuyruk)-1, 0, -1):
        x = kuyruk[index-1].xcor()
        y = kuyruk[index-1].ycor()
        kuyruk[index].goto(x,y)
        #kuyruk[index].getcanvas().create_text(text="S")
        #kuyruk[index].write("S", align="center", font=("courier", 8, "normal"))   

    # kuyruğun birinci elemanı da yılan kafasının yerine geçsin
    if len(kuyruk) > 0:
        x = kafa.xcor()
        y = kafa.ycor()
        kuyruk[0].goto(x,y) 



# Yılan kafasını yönüne göre hareket ettiren fonksiyon
def kafa_hareket():

    #eğer kafa yönü yukarı ise y koordinatını 20 artır, böylece kafa yukarı çıksın.
    if kafa.direction == "up":
        y = kafa.ycor()
        kafa.sety(y+20)
    
    #eğer kafa yönü aşağı ise y koordinatını 20 azalt, böylece kafa aşağı insin.    
    if kafa.direction == "down":
        y = kafa.ycor()
        kafa.sety(y-20)

    #eğer kafa'nın yönü sola ise x koordinatını 20 azalt, böylece kafa sola ilerlesin.       
    if kafa.direction == "left":
        x = kafa.xcor()
        kafa.setx(x-20)

    #eğer kafa'nın yönü sağa ise x koordinatını 20 artır, böylece kafa sağa ilerlesin.        
    if kafa.direction == "right":
        x = kafa.xcor()
        kafa.setx(x+20)



# Yılan kafasının sınıra çarpıp çarpmadığının kontrolü ve 
# çarptığında yapılacak işlere ilişkin fonksiyon
def borderControl():
    
    # Yılan kafasını dört sınır ile tek tek kontrol edelim 
    # (herhangibiri true ise isTouched true olur)
    solKontrol = kafa.xcor() < BORDER_SAFE_LEFT
    sagKontrol = kafa.xcor() > BORDER_SAFE_RIGHT
    yukariKontrol = kafa.ycor() > BORDER_SAFE_UP
    asagiKontrol = kafa.ycor() < BORDER_SAFE_DOWN
    isTouched = solKontrol or sagKontrol or yukariKontrol or asagiKontrol

    # Yılanın kafası sınıra değmiş ise
    if isTouched:

        # zaman 1 sn. dursun
        time.sleep(1)

        # kafayı ortaya gönderelim ve yönünü sıfırlayalım
        kafa.goto(0,0)
        kafa.direction = "stop"
        
        # kuyruğun her bir parçasını saklayalım, oyun alanı dışına gönderelim
        for parca in kuyruk:
            parca.goto(1000,1000)

        # yılanın kuyruğunu silelim, yılanın sadece kafası kalsın
        kuyruk.clear()

        global score, bestScore
        # en yüksek skoru  güncelleyelim
        if score > bestScore: 
            bestScore = score
        # yandığımız için skoru sıfırlayalım
        score = 0 

        global delay
        # oyun hızına ilişkin gecikme değerini başlangıç değerine getirelim
        delay = DELAY_FOR_SPEED



# Yılan kuruğuna bir parça ekleyen fonksiyon
def kuyruga_BirParcaEkle():

    #yılanı uzatacak parçayı oluşturalım, yılan kafası ile aynı ama gri renkli olsun
    parca = turtle.Turtle()
    parca.speed(0)
    parca.shape("square")
    parca.color("grey")
    parca.penup()
    
    # yılanın kuyruğuna parcayı ekleyelim
    kuyruk.append(parca)



# Yılan yemi yediğinde yapılacak işlere ilişkin fonksiyon
def targetControl():

    #yılanın başı yeme değerse
    if kafa.distance(yem) < 20:

        # yemin koordinatını rasgele bir koordinata yer değiştirelim.
        x = random.randint(BORDER_SAFE_LEFT, BORDER_SAFE_RIGHT)
        y = random.randint(BORDER_SAFE_DOWN, BORDER_SAFE_UP)
        yem.goto(x,y)       
        
        global score
        # yılan yemi yediği için skoru 1 artıralım, 
        score = score + 1   
              
        # Kuyruğa bir parça ekleyelim
        kuyruga_BirParcaEkle() 
        
        global delay
        #yılan her yeme değdiğinde delay'i biraz azaltarak hızın artmasını sağlayalım
        delay = delay - 0.005
    


# Yılan kafasının yönünü ayarlayan fonksiyonları yazalım
def set_direction_up():
    kafa.direction="up"

def set_direction_down():
    kafa.direction="down"

def set_direction_left():
    kafa.direction="left"
    
def set_direction_right():
    kafa.direction = "right"

#klavye bağlantıları
gameScreen.listen()
gameScreen.onkeypress(set_direction_up, "Up")
gameScreen.onkeypress(set_direction_down, "Down")
gameScreen.onkeypress(set_direction_left, "Left")
gameScreen.onkeypress(set_direction_right, "Right")



#oyunun ana döngüsü
while True:
    # her döngüde oyun sahasını update edelim ki son durumu görelim
    gameScreen.update()  

    # Yılanın kafası oyun alanı sınırlarına değip değmediğini kontrol edelim
    borderControl()

    # Yılanın yemi yiyip yemediğini kontrol edelim
    targetControl()

    # Skorda bir değişiklik varsa yeni skorları tabelaya yazalım
    if currentScore !=  score:
        tabela.clear() # tabelayı temizleyelim ki skoru temiz tabelaya yazsın.
        tabela.write("Score={}  Best Score={}".format(score, bestScore), align="center", font=("courier", 24, "normal")) 
    currentScore =  score

    # yılan kuyruğunu hareket ettirelim.
    kuyruk_hareket()

    # yılan kafasını hareket ettirelim.
    kafa_hareket()

    # delay değeri kadar bir süre gecikme olsun, yani hızı ayarlayalım
    time.sleep(delay)
    
gameScreen.mainloop()












