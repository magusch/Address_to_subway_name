import pandas as pd
import numpy as np
import requests


import os 

fileDir = os.path.dirname(os.path.realpath(__file__))

class get_subway_name():
	"""
	Example:
			from metro import get_subway_name
			q = get_subway_name(2) # 2 - Санкт петербург
			address = 'почтамтский пер.,'
			print(q.get_subway(address))

	"""

	R = 6371.0 #радиус Земли

	cities = {1: 'Москва', 2: 'Санкт-Петербург', 3: 'Екатеринбург', 66:'Нижний Новгород'}
	city_center = {1:(55.750683, 37.617496), 2:(59.939365, 30.315363), 3:(56.839104, 60.60825)}

	def __init__(self, city_id=2):
		"""
		Parametrs:
			city_id: Saint-Petersburg - 2, Moscow – 1, 

		"""
		if city_id not in self.cities:
			city_id = 2
		
		self.city = self.cities[city_id]
		
		if city_id in self.city_center:
			self.city_center = self.city_center[city_id]
		else:
			self.city_center = self.address_to_coord('')

		try:
			filename = f'{fileDir}/data/metro-{city_id}.csv' 
			metro = pd.read_csv(filename) 
		except: 
			from .metro_to_csv import get_pd_metro
			metro = get_pd_metro(city_id)
		metro.index = metro['name']
		self.metro = metro

	def polar_to_cartesian(self, lat, lng):
		theta = lat/360*2*np.pi
		phi = lng/360*2*np.pi

		x = self.R * np.cos(theta)*np.cos(phi)
		y = self.R * np.cos(theta)*np.sin(phi)
		z = self.R * np.sin(theta)

		return x, y, z

	def address_to_coord(self, address):
		#url = f"http://search.maps.sputnik.ru/search/addr?q={self.city}, {address}&format=JSON"
		url = f"https://nominatim.openstreetmap.org/search/{self.city}, {address}?format=json&addressdetails=1&limit=1&countrycodes=ru"
		answer = requests.get(url).json()
		if answer:
			lat = float(answer[0]['lat'])
			lng = float(answer[0]['lon'])
		else: 
			lat, lng = self.city_center #center of city, default coordinate
		return lat, lng

	def nearest_subway(self,x,y,z):	
		self.metro['distance'] = ((self.metro['x']-x)**2+(self.metro['y']-y)**2+(self.metro['z']-z)**2)**(1/2)
		return (self.metro['distance'].sort_values().index[0])

	def get_subway(self,address):
		try:
			lat, lng = self.address_to_coord(address)
			if (lat,lng)==self.city_center:
				return
			x, y, z = self.polar_to_cartesian(lat, lng)
			return (self.nearest_subway(x,y,z))
		except Exception as ex:
			print(ex)
			return



