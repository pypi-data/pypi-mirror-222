from datetime import datetime, timedelta
from itertools import combinations, product, repeat
from logging import Logger
from typing import Union

import swisseph as swe

from py_astrolab import CompositeAspects, KrInstance, NatalAspects
from py_astrolab.types import ZodiacType
from py_astrolab.utilities import calculate_position, for_every_planet


class Transit():
    iflag = swe.FLG_SWIEPH+swe.FLG_SPEED
    now = datetime.now()
    transit_planets = {'Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn'}

    def __init__(
            self,
            user: KrInstance,
            name="Now",
            year: int = now.year,
            month: int = now.month,
            day: int = now.day,
            hour: int = now.hour,
            minute: int = now.minute,
            city: str = "",
            nation: str = "",
            lng: Union[int, float] = 0,
            lat: Union[int, float] = 0,
            tz_str: str = "",
            logger: Union[Logger, None] = None,
            geonames_username: str = 'century.boy',
            zodiac_type: ZodiacType = "Tropic",
            house_method: str = "Vehlow",
            online: bool = True,
            settings: Union[str, None] = None,
    ):
        self.user = user
        self.radix = KrInstance(
            name=name,
            year=year,
            month=month,
            day=day,
            hour=hour,
            minute=minute,
            city=city,
            nation=nation,
            lng=lng,
            lat=lat,
            tz_str=tz_str,
            logger=logger,
            geonames_username=geonames_username,
            zodiac_type=zodiac_type,
            house_method=house_method,
            online=online
        )
        self.julday = swe.julday(year, month, day, hour, minute)
        self.settings = settings

    def get_all(self):
        self.natal_aspects()
        self.transit_aspects()
        self.lunar_phase()
        self.new_moon()
        
    def natal_aspects(self):
        composite_aspects = CompositeAspects(self.radix, self.user, self.settings)
        natal_aspects = composite_aspects.get_all_aspects()
        natal_aspects = [aspect for aspect in natal_aspects if aspect['p1_name'] in self.transit_planets]
        natal_aspects = [aspect for aspect in natal_aspects if abs(aspect['orbit']) <= composite_aspects.planets_settings[aspect['p1']]['orbit']]
        self.natal_aspects = natal_aspects
        self.points_in_houses = composite_aspects.get_points_in_houses()

    def transit_aspects(self):
        natal_aspects = NatalAspects(self.radix, self.settings)
        transit_aspects = natal_aspects.get_all_aspects()      
        transit_aspects = [aspect for aspect in transit_aspects if aspect['p1_name'] in self.transit_planets]
        transit_aspects = [aspect for aspect in transit_aspects if abs(aspect['orbit']) <= natal_aspects.planets_settings[aspect['p1']]['orbit']]
        self.transit_aspects = transit_aspects
    
    def lunar_phase(self):
        self.lunar_phase = self.radix.lunar_phase
    
    def new_moon(self):
        jd = self.julday
        sun_deg = swe.calc(jd, 0, self.iflag)[0][0]
        moon_deg = swe.calc(jd, 1, self.iflag)[0][0]
        while abs(sun_deg - moon_deg) > 0.1:
            jd -= 4/(24*60)
            sun_deg = swe.calc(jd, 0, self.iflag)[0][0]
            moon_deg = swe.calc(jd, 1, self.iflag)[0][0]
        new_moon = calculate_position(moon_deg, "New Moon", "Synod")
        new_moon = for_every_planet(self.user, new_moon, moon_deg)
        self.new_moon = new_moon

class Transits():
    def __init__(self, 
            user: KrInstance, 
            start: datetime, 
            end: datetime,
            city: str = "",
            nation: str = "",
            lng: Union[int, float] = 0,
            lat: Union[int, float] = 0,
            tz_str: str = "",
            logger: Union[Logger, None] = None,
            geonames_username: str = 'century.boy',
            zodiac_type: ZodiacType = "Tropic",
            house_method: str = "Vehlow",
            online: bool = True,
            settings: Union[str, None] = None,
            interval: timedelta = timedelta(minutes=1)):
        self.user = user
        self.start = start
        self.end = end
        self.city = city
        self.nation = nation
        self.lng = lng
        self.lat = lat
        self.tz_str = tz_str
        self.logger = logger
        self.geonames_username = geonames_username
        self.zodiac_type = zodiac_type
        self.house_method = house_method
        self.online = online
        self.settings = settings
        self.interval = interval
        self.natal_aspects_changes = {}
        self.transit_aspects_changes = {}
        self.previous_natal_aspects = None
        self.previous_transit_aspects = None

        self.planets = range(swe.SUN, swe.SATURN)
        self.aspects = [0, 60, 90, 120, 180]
        self.planet_names = {
            swe.SUN: {'name': 'Sun', 'orbit': 3, 'interval': timedelta(hours=1)}, # 6 giorni in aspetto
            # 365 giorni / 360 gradi = 1 giorni per grado
            # 3 gradi di orbita * 2 * 1 giorni = 6 giorni in aspetto
            swe.MOON: {'name': 'Moon','orbit': 1, 'interval': timedelta(minutes=5)}, # 3,6 ore in aspetto
            # 27.3 giorni / 360 gradi = 1 ora e 49 minuti per grado (109 minuti)
            # 1 gradi di orbita * 2 * 1 ora e 49 minuti = 3,6 ore
            swe.MERCURY: {'name': 'Mercury','orbit': 3, 'interval': timedelta(hours=1)}, # 1,5 giorni in aspetto
            # 88 giorni / 360 gradi = 5,9 ore per grado (351 minuti)
            # 3 gradi di orbita * 2 * 5,9 ore = 1,5 giorni
            swe.VENUS: {'name': 'Venus','orbit': 3, 'interval': timedelta(hours=1)}, # 3,75 giorni in aspetto
            # 225 giorni / 360 gradi = 15 ore per grado
            # 3 gradi di orbita * 2 * 15 ore = 3,75 giorni
            swe.MARS: {'name': 'Mars','orbit': 5, 'interval': timedelta(hours=1)}, # 38 giorni
            # 687 giorni / 360 gradi = 1.9 giorni per grado (45,6 ore)
            # 5 gradi di orbita * 2 * 1.9 giorni = 38 giorni
            swe.JUPITER: {'name': 'Jupiter','orbit': 5, 'interval': timedelta(hours=1)}, # 4 mesi in aspetto
            # (11.86 anni * 365.25 giorni/anno) / 360 gradi = 12 giorni per grado
            # 5 gradi di orbita * 2 * 12 giorni = 120 giorni (4 mesi)
            swe.SATURN: {'name': 'Saturn','orbit': 5, 'interval': timedelta(days=1)} # 10 mesi
            # (29.5 anni * 365.25 giorni/anno) / 360 gradi = 30 giorni per grado
            # 5 gradi di orbita * 2 * 30 giorni = 300 giorni (10 mesi)
        }
        self.aspect_names = {
            0: 'conjunction',
            60: 'sextile',
            90: 'square',
            120: 'trine',
            180: 'opposition',
        }
        self.times, self.positions = self.calculate_positions()
        self.angle_cache = dict()

    def calc_orb(self, jd, planet1, planet2, aspect, natal_planet_orb=None):
        cache_tuple = (jd, planet1, planet2, aspect)
        if cache_tuple in self.angle_cache:
            return self.angle_cache[cache_tuple]
        lon1 = swe.calc(jd, planet1)[0][0]
        lon2 = swe.calc(jd, planet2)[0][0] if not natal_planet_orb else natal_planet_orb
        angle = self.angle_difference(lon1, lon2)
        orb = abs(abs(angle) - aspect)
        self.angle_cache[cache_tuple] = orb
        return orb

    def aspects_transits_transits(self, look_for_planets = None):
        look_for_planets = set(self.planet_names.keys()) if look_for_planets is None else look_for_planets
        aspects = self.find_transit_transit_aspects(self.times, self.positions, look_for_planets)
        return aspects

    def aspects_natal_transits(self, look_for_planets = None):
        look_for_planets = set(self.planet_names.keys()) if look_for_planets is None else look_for_planets
        natal_positions = {planet_data['name']: planet_data['abs_pos'] for planet_data in self.user.planets_list}
        aspects = self.find_natal_transit_aspects(self.times, self.positions, natal_positions, look_for_planets)
        return aspects

    def angle_difference(self, angle1, angle2):
        return 180 - abs(abs(angle1 - angle2) - 180)

    def jd_to_datetime(self, jd):
        jd = jd + 0.5
        Z = int(jd)
        F = jd - Z
        alpha = int((Z - 1867216.25) / 36524.25)
        A = Z + 1 + alpha - int(alpha / 4.)
        B = A + 1524
        C = int((B - 122.1) / 365.25)
        D = int(365.25 * C)
        E = int((B - D) / 30.6001)
        day = B - D - int(30.6001 * E) + F
        month = E - 1 if E < 14 else E - 13
        year = C - 4716 if month > 2 else C - 4715
        day, fractional_day = divmod(day, 1)
        hour, fractional_hour = divmod(fractional_day * 24, 1)
        minute, _ = divmod(fractional_hour * 60, 1)
        minute = round(minute)
        return datetime(int(year), int(month), int(day), int(hour), int(minute))

    def binary_search(self, time1, time2, planet1, planet2, aspect, target_orb=None, natal_planet_orb=None):
        target_orb = target_orb if target_orb else min(self.planet_names[planet1]['orbit'], self.planet_names[planet2]['orbit'])
        jd1 = swe.julday(time1.year, time1.month, time1.day, time1.hour + time1.minute/60)
        jd2 = swe.julday(time2.year, time2.month, time2.day, time2.hour + time2.minute/60)
        while jd2 - jd1 > 6.94e-4:  # 1 minuto in giorni.
            jd = jd1 + (jd2 - jd1) / 2
            orb = self.calc_orb(jd, planet1, planet2, aspect, natal_planet_orb)  # Calcola l'orbita
            if abs(orb - target_orb) < 0.01:  # Se l'orbita è vicina a target_orb
                jd = round(jd * 1440) / 1440  # Arrotonda al minuto più vicino
                return self.jd_to_datetime(jd), orb
            if orb > target_orb:
                jd1 = jd
            else:
                jd2 = jd
        jd1 = round(jd1 * 1440) / 1440  # Arrotonda al minuto più vicino
        orb = self.calc_orb(jd1, planet1, planet2, aspect, natal_planet_orb)  # Calcola l'orbita
        return self.jd_to_datetime(jd1), orb

    def backward_binary_search(self, planet1, planet2, aspect, orbit_tolerance, natal_planet_orb=None):
        # Prima, trova il giorno in cui l'aspetto non è presente.
        interval = min(self.planet_names[planet1]['interval'], self.planet_names[planet2]['interval'])
        current_time = self.start
        while True:  # Loop finché l'aspetto è presente
            jd = swe.julday(current_time.year, current_time.month, current_time.day, current_time.hour + current_time.minute/60)
            angle_current_time = self.calc_orb(jd, planet1, planet2, aspect, natal_planet_orb)
            if angle_current_time > orbit_tolerance:  # Se l'aspetto non è presente, esci dal loop
                break
            current_time -= interval  # Vai indietro di un intervallo di tempo
        # Ora abbiamo il tempo in cui l'aspetto non era presente, cerchiamo il minuto esatto nell'intervallo di tempo successivo.
        lower_bound = current_time + interval  # L'inizio dell'intervallo successivo
        upper_bound = lower_bound + interval
        # Ora utilizza binary_search tra lower_bound e upper_bound
        return self.binary_search(lower_bound, upper_bound, planet1, planet2, aspect, orbit_tolerance, natal_planet_orb)

    def forward_binary_search(self, planet1, planet2, aspect, target_orb, current_time, natal_planet_orb=None):
        interval = min(self.planet_names[planet1]['interval'], self.planet_names[planet2]['interval'])
        while True:
            jd = swe.julday(current_time.year, current_time.month, current_time.day, current_time.hour + current_time.minute/60)
            angle_current_time = self.calc_orb(jd, planet1, planet2, aspect, natal_planet_orb)
            if angle_current_time > target_orb + 0.1:
                break
            current_time += interval
        upper_bound = current_time
        lower_bound = current_time - interval
        return self.binary_search(lower_bound, upper_bound, planet1, planet2, aspect, target_orb, natal_planet_orb)

    def calculate_positions(self):
        minutes_diff = int((self.end - self.start).total_seconds() / 60)
        times = [self.start + timedelta(minutes=i) for i in range(0, minutes_diff, 5)]
        positions = {planet: [] for planet in self.planets}
        for time in times:
            jd = swe.julday(time.year, time.month, time.day, time.hour + time.minute/60)
            for planet in self.planets:
                lon = swe.calc(jd, planet)[0][0]
                positions[planet].append(lon)
        return times, positions

    def find_transit_transit_aspects(self, times, positions, look_for_planets):
        aspects = {}
        current_aspects = set()
        for planet1, planet2 in combinations(self.planets, 2):
            if planet1 not in look_for_planets:
                continue
            orbit_tolerance = min(self.planet_names[planet1]['orbit'], self.planet_names[planet2]['orbit'])
            for time1, time2, lon1_1, lon1_2, lon2_1, lon2_2 in zip(times, times[1:], positions[planet1], positions[planet1][1:], positions[planet2], positions[planet2][1:]):
                for a in self.aspects:
                    p1_name = self.planet_names[planet1]['name']
                    p2_name = self.planet_names[planet2]['name']
                    aspect_name = self.aspect_names[a]
                    aspect_tuple = (p1_name, p2_name, aspect_name)
                    diff1 = self.angle_difference(lon1_1, lon2_1)
                    diff2 = self.angle_difference(lon1_2, lon2_2)
                    if ((diff1 - a) * (diff2 - a) <= 0) or (abs(diff1 - a) <= orbit_tolerance) or (abs(diff2 - a) <= orbit_tolerance):
                        if aspect_tuple not in current_aspects:
                            if time1 == self.start:
                                start_time, orb = self.backward_binary_search(planet1, planet2, a, orbit_tolerance)
                            else:
                                start_time, orb = self.binary_search(time1, time2, planet1, planet2, a, orbit_tolerance)
                            finish_time, _ = self.forward_binary_search(planet1, planet2, a, orbit_tolerance, start_time)
                            aspect_dict = {'p1_name': p1_name, 'p2_name': p2_name, 'aspect': aspect_name, 'start': start_time, 'finish': finish_time, 'duration': finish_time-start_time, 'orb': orb}
                            aspects.setdefault(start_time, []).append(aspect_dict)
                            current_aspects.add(aspect_tuple)
                    else:
                        current_aspects.discard(aspect_tuple)
        return aspects

    def find_natal_transit_aspects(self, times, positions, natal_positions, look_for_planets):
        aspects = {}
        current_aspects = set()
        for planet1, planet2 in product(self.planets, natal_positions.keys()):
            if planet1 not in look_for_planets:
                continue
            planet2_number = next((planet for planet, info in self.planet_names.items() if info['name'] == planet2), None)
            if planet2_number is None:
                continue
            orbit_tolerance = self.planet_names[planet1]['orbit']
            natal_position = natal_positions[planet2]
            for time1, time2, lon1_1, lon1_2 in zip(times, times[1:], positions[planet1], positions[planet1][1:]):
                for a in self.aspects:
                    p1_name = self.planet_names[planet1]['name']
                    p2_name = planet2
                    aspect_name = self.aspect_names[a]
                    aspect_tuple = (p1_name, p2_name, aspect_name)
                    diff1 = self.angle_difference(lon1_1, natal_position)
                    diff2 = self.angle_difference(lon1_2, natal_position)
                    if ((diff1 - a) * (diff2 - a) <= 0) or (abs(diff1 - a) <= orbit_tolerance) or (abs(diff2 - a) <= orbit_tolerance):
                        if aspect_tuple not in current_aspects:
                            if time1 == self.start:
                                start_time, orb = self.backward_binary_search(planet1, planet2_number, a, orbit_tolerance, natal_position)
                            else:
                                start_time, orb = self.binary_search(time1, time2, planet1, planet2_number, a, orbit_tolerance, natal_position)
                            finish_time, _ = self.forward_binary_search(planet1, planet2_number, a, orbit_tolerance, start_time, natal_position)
                            aspect_dict = {'p1_name': p1_name, 'p2_name': p2_name, 'aspect': aspect_name, 'start': start_time, 'finish': finish_time, 'duration': finish_time-start_time, 'orb': orb}
                            aspects.setdefault(start_time, []).append(aspect_dict)
                            current_aspects.add(aspect_tuple)
                    else:
                        current_aspects.discard(aspect_tuple)
        return aspects