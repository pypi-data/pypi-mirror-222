Script ini untuk membuat jalurterbang Spraying untuk drone spraying FC JIYI, "memanfaatkan hasil waypoint dari avirplaner".
Data yang dihasilkan adalah berupa garis(.shp).

Data yang dibutuhkan adalah (.waypoint) hasil dari avirplaner. 
Bila menggunakan data DSM(.tif) boleh menggunakan koordinat WGS_1984, maupun koordinat UTM.

Data tersebut dilanjutkan di software Qgis, untuk diconvert menjadi (.kml), lalu di "dissolve".
Data hasil dissolve dapat digunakan dalam aplikasi "AgriAsistant"

Install
pip install avirtech_spraying_jiyi_waypoint_lib

Usage
from avirtech_spraying_jiyi_wp_lib.avirtech_spraying_jiyi_wp import autocorrect