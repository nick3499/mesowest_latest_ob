#!/usr/bin/env bash

curl -s "http://api.mesowest.net/v2/stations/latest?&token=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&stids=AR794" > latest.json

printf '\e[31mTemperature-----------:\e[0m %.1f℉\n' $(echo | jq '(.STATION[0].OBSERVATIONS.air_temp_value_1.value * 1.8) + 32' latest.json)
printf '\e[34mHumidity--------------:\e[0m %.1f%%\n' $(echo | jq '.STATION[0].OBSERVATIONS.relative_humidity_value_1.value' latest.json)
printf '\e[34mDew point-------------:\e[0m %.1f℉\n' $(echo | jq '(.STATION[0].OBSERVATIONS.dew_point_temperature_value_1d.value * 1.8) + 32' latest.json)
printf '\e[31mSolar radiation-------:\e[0m %.1f W/㎡\n' $(echo | jq '.STATION[0].OBSERVATIONS.solar_radiation_value_1.value' latest.json)
printf "\e[34mWind Direction--------:\e[0m %s\n" $(echo | jq '.STATION[0].OBSERVATIONS.wind_cardinal_direction_value_1d.value' latest.json)
printf '\e[34mWind Direction (angle):\e[0m %.1f°\n' $(echo | jq '.STATION[0].OBSERVATIONS.wind_direction_value_1.value' latest.json)
printf '\e[34mWind Speed------------:\e[0m %.1f mph\n' $(echo | jq '.STATION[0].OBSERVATIONS.wind_speed_value_1.value * 1.1507794' latest.json)
printf '\e[34mWind Gust-------------:\e[0m %.1f mph\n' $(echo | jq '.STATION[0].OBSERVATIONS.wind_gust_value_1.value * 1.1507794' latest.json)
printf '\e[31mAir PSI---------------:\e[0m %.1f Mb\n' $(echo | jq '(.STATION[0].OBSERVATIONS.pressure_value_1d.value * 0.029529987507120267) * .01' latest.json)
printf '\e[31mSea Level Air PSI-----:\e[0m %.1f Mb\n' $(echo | jq '(.STATION[0].OBSERVATIONS.sea_level_pressure_value_1d.value * 0.029529987507120267) * .01' latest.json)
printf '\e[31mAltimeter-------------:\e[0m %.1f Mb\n' $(echo | jq '(.STATION[0].OBSERVATIONS.altimeter_value_1.value * 0.029529987507120267) * .01' latest.json)
printf '\e[34mPrecipitation---------:\e[0m %.1f\"\n' $(echo | jq '.STATION[0].OBSERVATIONS.precip_accum_24_hour_value_1.value * .0393700787' latest.json)
printf '\e[34mPrecip. since midnight:\e[0m %.1f\"\n' $(echo | jq '.STATION[0].OBSERVATIONS.precip_accum_since_local_midnight_value_1.value * .0393700787' latest.json)
printf '\e[31mQC--------------------:\e[0m %d\n' $(echo | jq '.STATION[0].OBSERVATIONS.qc_value_1.value' latest.json)
