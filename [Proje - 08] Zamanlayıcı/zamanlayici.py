# coding=utf-8

"""
    Zamanlayıcı kullanımı
    Tarihi gösteren küçük bir uygulama
"""

import time

while True:
    zaman = time.localtime()
    yil = zaman[0]
    ay = zaman[1]
    gun = zaman[2]
    saat = zaman[3]
    dakika = zaman[4]
    saniye = zaman[5]
    
    time.sleep(1)

    print("""
        tarih: {}/{}/{}
        saat : {}:{}:{}
        """.format(gun, ay, yil, saat, dakika, saniye))
 
