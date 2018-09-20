# mesowest_latest_ob
## Python 3 Version: MesoPy (MesoWest API Wrapper): Current Weather Conditions

![img_py]

### Run Script in Bash

```sh
$ ./mesowest_latest_ob.py
```

### Import the Meso function from the MesoPy Module

```py
from MesoPy import Meso
```

### Get Latest Weather Observation from MesoWest Station

```py
lat = m.latest(stid='AR794')
```

### Get Station ID

```py
s = lat['STATION'][0]['STID']
```

### Get Air Temperature

```py
t = lat['STATION'][0]['OBSERVATIONS']['air_temp_value_1']['value']
```

### Test Script in Python Interactive Mode

```py
$  sudo python3 -i mesowest_latest_AR794.py 
Latest Weather Observation  (KC9DNQ-3 Coal City, AR794)
Temperature: 64.0℉
Humidity: 84.0%
Dew point: 59.0℉
Solar radiation: 0.0 watts/m²
Wind direction: E
Wind direction: 89.0°
Wind speed: 0.5 mph
Wind gust: 2.6 mph
Air pressure: 29.5 inHg (KILROMEO4)
Sea level pressure: 30.1 inHg (KILROMEO4)
Altimeter: 30.1 inHg (KILROMEO4)
Precipitation: 0.0"
Precipitation since midnight: 0.0"
QC: OK

>>> s
'AR794'
>>> s1
'KC9DNQ-3 Coal City'
>>> ob
{'precip_accum_24_hour_value_1': {'date_time': '2018-09-14T03:40:00Z', 'value': 0.0}, 'solar_radiation_value_1': {'date_time': '2018-09-14T03:40:00Z', 'value': 0.0}, 'wind_gust_value_1': {'date_time': '2018-09-14T03:40:00Z', 'value': 2.23}, 'dew_point_temperature_value_1d': {'date_time': '2018-09-14T03:40:00Z', 'value': 15.02}, 'wind_cardinal_direction_value_1d': {'date_time': '2018-09-14T03:40:00Z', 'value': 'E'}, 'pressure_value_1d': {'date_time': '2018-09-14T03:40:00Z', 'value': 99981.4}, 'wind_direction_value_1': {'date_time': '2018-09-14T03:40:00Z', 'value': 89.0}, 'sea_level_pressure_value_1d': {'date_time': '2018-09-14T03:40:00Z', 'value': 101870.6}, 'precip_accum_since_local_midnight_value_1': {'date_time': '2018-09-14T03:40:00Z', 'value': 0.0}, 'altimeter_value_1': {'date_time': '2018-09-14T03:40:00Z', 'value': 101896.38}, 'air_temp_value_1': {'date_time': '2018-09-14T03:40:00Z', 'value': 17.78}, 'qc_value_1': {'date_time': '2014-10-06T23:36:00Z', 'value': 2.0}, 'wind_speed_value_1': {'date_time': '2018-09-14T03:40:00Z', 'value': 0.45}, 'relative_humidity_value_1': {'date_time': '2018-09-14T03:40:00Z', 'value': 84.0}}
>>> s2
'0.0'
>>> s5
'59.0'
>>> t = lat['STATION'][0]['OBSERVATIONS']['air_temp_value_1']['value']
>>> t
17.78
```

### Bash Version: Current Weather Conditions

![img_sh]

This shell script teams up [Bash](https://www.gnu.org/software/bash/) with [jq](https://stedolan.github.io/jq/) and [cURL](https://curl.haxx.se/). cURL is used to get the JSON data from the MesoWest server, then saves that blob to a `.json` file locally. Each line of the display shown above comes from a single `printf` call, where the format string can be found after the text string. Then the JSON weather data blob is piped to jq which processes the JSON. Also, `jq` has math operators which were used to convert the values to preferred units of measure, e.g. mm to in, etc. Americanized, basically. So, if you are in Europe, you can remove the conversion calculation for precipitation, for example, and use the default value, which is in mm. Basic mult. and div. factors were applied. Easy peasy.

[img_sh]: https://github.com/nick3499/mesowest_latest_ob/blob/master/latest_ar794_bash.png "display of script in Bash"
[img_py]: https://github.com/nick3499/mesowest_latest_ob/blob/master/display_example.png "display of script in Bash"
