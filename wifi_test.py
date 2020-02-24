import pywifi
from pywifi import const
def gic():
   wifi=pywifi.PyWiFi()
   ifaces = wifi.interfaces()[0]
   print(ifaces.name())
# gic()

def scan():
   wifi = pywifi.PyWiFi()
   ifaces = wifi.interfaces()[0]
   ifaces.scan()
   bessis = ifaces.scan_results()
   for name in bessis:
       print(name.ssid)

scan()

