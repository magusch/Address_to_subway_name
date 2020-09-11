import pandas as pd
import numpy as np
import requests


import os
fileDir = os.path.dirname(os.path.realpath(__file__))

R = 6371.0

def get_pd_metro(city_id=2):
	url = f'https://api.hh.ru/metro/{city_id}'
	r = requests.get(url)

	json_answer = r.json()

	name, lat, lng = [], [], []

	for line in json_answer['lines']:
		for station in line['stations']:
			name.append(station['name'])
			lat.append(station['lat'])
			lng.append(station['lng'])

	df = pd.DataFrame({
		'name':name, 'lat': lat, 'lng': lng, 
		})

	df['theta'] = df['lat']/360*2*np.pi
	df['phi'] = df['lng']/360*2*np.pi
	df['x'] = R * np.cos(df['theta'])*np.cos(df['phi'])
	df['y'] = R * np.cos(df['theta'])*np.sin(df['phi'])
	df['z'] = R * np.sin(df['theta'])

	df = df.drop(['lat','lng','theta','phi'], axis=1)
	filename = f'{fileDir}/data/metro-{city_id}.csv' 
	df.to_csv(filename)

	return df
