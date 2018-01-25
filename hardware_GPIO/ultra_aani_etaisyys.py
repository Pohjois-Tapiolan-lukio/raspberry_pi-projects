#VCC an Pin 2 (VCC)
#GND an Pin 6 (GND)
#TRIG an Pin 12 (GPIO18)
#ECHO 330 ohm vastuskytkenta

#Tuodaan kirjastot kayttoon
import RPi.GPIO as GPIO
import time
 
#GPIO tila (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#GPIO kaytettavat  pinnit
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#GPIO-Pinnien toimintasuunta, asettaminen (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def etaisyys():
    # aseta Trigger  HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # aseta Trigger  0.01ms jalkeen  LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    AloitusAika = time.time()
    LopetusAika = time.time()
 
    #  tallenna AloitusAika
    while GPIO.input(GPIO_ECHO) == 0:
        AloitusAika = time.time()
 
    # tallenna LopetusAika
    while GPIO.input(GPIO_ECHO) == 1:
        LopetusAika = time.time()
 
    #  Aikaero
    KulunutAika = LopetusAika - AloitusAika
    # Aanennopeus (34300 cm/s) 
    # jaetaan 2:lla , edestakaisin  
    etaisyys = (KulunutAika * 34300) / 2
 
    return etaisyys
 
if __name__ == '__main__':
    try:
        while True:
            MitattuEtaisyys = etaisyys()
            print ("Mitattu etaisyys  {:.1f} cm".format(MitattuEtaisyys))
            time.sleep(1)
 
        # Keskeytys ctrl+C reset
    except KeyboardInterrupt:
        print("Mittaus pysaytetty.")
        GPIO.cleanup()
