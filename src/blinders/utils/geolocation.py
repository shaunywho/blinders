
from django.contrib.gis.geoip2 import GeoIP2
from django.conf import settings
import mpu


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


def get_distance(lat1,lon1, lat2,lon2):
  dist = mpu.haversine_distance((lat1, lon1), (lat2, lon2))
  return dist
