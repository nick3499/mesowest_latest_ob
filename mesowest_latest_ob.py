#!/usr/bin/env python3
'''
Copyright © 2018 nick3499@github
Title ⟹ 'Current Weather Conditions: MesoPy (MesoWest API Wrapper)'
Hosted ⟹ https://github.com/nick3499/mesowest_latest_ob
ISC License (ISC) ⟹ https://opensource.org/licenses/ISC
MesoWest Python wrapper ⟹ https://github.com/mesowx/MesoPy
API token required ⟹ https://synopticlabs.org/api/guides/?getstarted
Note: noticed data coming from more than one station, e.g. KILROMEO4, AR794.
'''

from MesoPy import Meso # import `Meso()`
m = Meso(token='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx') # pass API `token`
lat = m.latest(stid='AR794') # pass station ID, get `latest()` ob JSON data
s = lat['STATION'][0]['STID'] # station ID
s1 = lat['STATION'][0]['NAME'] # station name
ob = lat['STATION'][0]['OBSERVATIONS'] # JSON path prefix for current ob
s2 = ob['precip_accum_24_hour_value_1']['value'] # precip
s2 = "{0:.1f}".format(s2 * .0393700787) # mm to in
s3 = ob['solar_radiation_value_1']['value'] # solar rad
s4 = ob['wind_gust_value_1']['value'] # wind gust
s4 = "{0:.1f}".format(s4 * 1.1507794) # knots to mph
s5 = ob['dew_point_temperature_value_1d']['value'] # dew point
s5 = "{0:.1f}".format((1.8 * s5) + 32.0) # C to F
s6 = ob['wind_cardinal_direction_value_1d']['value'] # wind cardinal dir
s7 = ob['pressure_value_1d']['value'] # baro psi (KILROMEO4)
s7 = "{0:.1f}".format((s7 * 0.029529987507120267) * .01) # inHg to Mb
s8 = ob['wind_direction_value_1']['value'] # wind dir degrees
s9 = ob['sea_level_pressure_value_1d']['value'] # sea level psi (KILROMEO4)
s9 = "{0:.1f}".format((s9 * 0.029529987507120267) * .01) # inHg to Mb
s10 = ob['precip_accum_since_local_midnight_value_1']['value']
s10 = "{0:.1f}".format(s10 * .0393700787) # mm to in
s11 = ob['altimeter_value_1']['value'] # altimeter (KILROMEO4)
s11 = "{0:.1f}".format((s11 * 0.029529987507120267) * .01) # inHg to Mb
s12 = ob['air_temp_value_1']['value'] # air temp
s12 = "{0:.1f}".format((1.8 * s12) + 32.0) # C to F
s13 = ob['qc_value_1']['value'] # quality control
if s13 == 2.0:
    s13 = 'OK' # quality control returns 'OK' code
s14 = ob['wind_speed_value_1']['value'] # wind speed
s14 = "{0:.1f}".format(s14 * 1.1507794) # knots to mph
s15 = ob['relative_humidity_value_1']['value'] # humidity

# f-string format, print to CLI
print(f'\033[34mLatest Weather Observation \033[0m ({s1}, {s})\n\
\033[91mTemperature\033[0m: {s12}℉\n\
\033[34mHumidity\033[0m: {s15}%\n\
\033[34mDew point\033[0m: {s5}℉\n\
\033[91mSolar radiation\033[0m: {s3} watts/m²\n\
\033[34mWind direction\033[0m: {s6} - {s8}°\n\
\033[34mWind speed\033[0m: {s14} mph\n\
\033[34mWind gust\033[0m: {s4} mph\n\
\033[91mAir pressure\033[0m: {s7} inHg (KILROMEO4)\n\
\033[91mSea level pressure\033[0m: {s9} inHg (KILROMEO4)\n\
\033[91mAltimeter\033[0m: {s11} inHg (KILROMEO4)\n\
\033[34mPrecipitation\033[0m: {s2}\"\n\
\033[34mPrecipitation since midnight\033[0m: {s10}\"\n\
\033[91mQC\033[0m: {s13}\n\
')
