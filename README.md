# Address_to_subway_name
Get subway name from address

Получение название метро из адресса

В классе используется api http://api.sputnik.ru/maps/geocoder/ для определение координат из адреса и https://api.hh.ru/metro/ для получение таблицы с названием и координатами всех станций метро определённого города

find_metro@git+https://github.com/magusch/Address_to_subway_name.git@8885a932ee11a2c93b827d40ac880710ef74a084

# Функции и классы:
  get_pd_metro(city_id=2) – функция для сохранение и возвращение таблицы для списка городов, для Москвы и Санкт-Петербурга csv файлы уже сохранены
  
  get_subway_name() – Класс для создания объекта определённого города, где будет проходить поиск метро
  
  self.get_subway(address) – возвращает название станции метро
  
  self.address_to_coord(address) – переводит строку адресса в полярные координаты
  
  self.polar_to_cartesian(lat, lng) – переводит полярные координаты в декартовы (x,y,z)
  
  self.nearest_subway(x,y,z) – рассчитывает расстояние от заданных декартовых координат до всех станций метро и возвращает название самой ближайшей


#	Example:
			from metro import get_subway_name
			q = get_subway_name(city_id = 2) # 2 - Санкт петербург
			address = 'почтамтский пер.,'
			print(q.get_subway(address))
      
# Parametrs
  city_id: INT value from dict {1: 'Москва', 2: 'Санкт-Петербург', 3: 'Екатеринбург', 66:'Нижний Новгород'}
