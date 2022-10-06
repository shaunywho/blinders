
from django.contrib.gis.geoip2 import GeoIP2
from django.conf import settings



def get_geolocation(request):
  ip = get_ip(request)

  g = GeoIP2()

  return g.city(ip)





def get_ip(request):
  x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
  if x_forwarded_for:
      ip = x_forwarded_for.split(',')[0]
  else:
      ip = request.META.get('REMOTE_ADDR')
  if ip== "127.0.0.1":
    ip = '77.98.66.170'
  return ip