#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

clone_code = "M17"

historical_folder_location = "/projects/0/aqueduct/users/edwinsut/pcrglobwb_runs_2016_oct_nov/pcrglobwb_4_land_covers_edwin_parameter_set_gfdl-esm2m/no_correction/non-natural/"

#~ edwinhs@fcn26.bullx:/projects/0/aqueduct/users/edwinsut/pcrglobwb_runs_2016_oct_nov/pcrglobwb_4_land_covers_edwin_parameter_set_gfdl-esm2m/no_correction/non-natural$ ls -lah */M17/netcdf/discharge_dailyTot_output.nc 
#~ -r-xr-xr-x 1 edwinsut aqueduct 700M Nov 16  2016 begin_from_1951/M17/netcdf/discharge_dailyTot_output.nc
#~ -r-xr-xr-x 1 edwinsut aqueduct 3.0G Nov 14  2016 continue_from_1958/M17/netcdf/discharge_dailyTot_output.nc
#~ -r-xr-xr-x 1 edwinsut aqueduct 219M Nov 16  2016 continue_from_1988/M17/netcdf/discharge_dailyTot_output.nc
#~ -r-xr-xr-x 1 edwinsut aqueduct 1.6G Nov 16  2016 continue_from_1990/M17/netcdf/discharge_dailyTot_output.nc

rcp_folder_location = "/projects/0/aqueduct/users/edwinsut/pcrglobwb_runs_2016_oct_nov/pcrglobwb_4_land_covers_edwin_parameter_set_gfdl-esm2m/no_correction/rcp8p5/"

#~ edwinhs@fcn26.bullx:/projects/0/aqueduct/users/edwinsut/pcrglobwb_runs_2016_oct_nov/pcrglobwb_4_land_covers_edwin_parameter_set_gfdl-esm2m/no_correction/rcp8p5$ ls -lah */M17/netcdf/discharge_dailyTot_output.nc
#~ -r-xr-xr-x 1 edwinsut aqueduct 2.4G Nov  7  2016 begin_from_2006/M17/netcdf/discharge_dailyTot_output.nc
#~ -r-xr-xr-x 1 edwinsut aqueduct 100M Nov  7  2016 continue_from_2030/M17/netcdf/discharge_dailyTot_output.nc
#~ -r-xr-xr-x 1 edwinsut aqueduct 862M Nov 16  2016 continue_from_2031/M17/netcdf/discharge_dailyTot_output.nc
#~ -r--r--r-- 1 edwinsut aqueduct 2.0G Dec 28  2016 continue_from_2039/M17/netcdf/discharge_dailyTot_output.nc
#~ -r--r--r-- 1 edwinsut aqueduct 223M Dec 28  2016 continue_from_2059/M17/netcdf/discharge_dailyTot_output.nc
#~ -r--r--r-- 1 edwinsut aqueduct 3.1G Dec 28  2016 continue_from_2061/M17/netcdf/discharge_dailyTot_output.nc
#~ -r--r--r-- 1 edwinsut aqueduct 783M Dec 26  2016 continue_from_2092/M17/netcdf/discharge_dailyTot_output.nc

# names of netcdf files that will be merged
netcdf_file_names = \
[
historical_folder_location +    "/begin_from_1951/" + clone_code + "/netcdf/discharge_dailyTot_output.nc", \
historical_folder_location + "/continue_from_1958/" + clone_code + "/netcdf/discharge_dailyTot_output.nc", \
historical_folder_location + "/continue_from_1988/" + clone_code + "/netcdf/discharge_dailyTot_output.nc", \
historical_folder_location + "/continue_from_1990/" + clone_code + "/netcdf/discharge_dailyTot_output.nc", \
rcp_folder_location        +    "/begin_from_2006/" + clone_code + "/netcdf/discharge_dailyTot_output.nc", \
rcp_folder_location        + "/continue_from_2030/" + clone_code + "/netcdf/discharge_dailyTot_output.nc", \
rcp_folder_location        + "/continue_from_2031/" + clone_code + "/netcdf/discharge_dailyTot_output.nc", \
rcp_folder_location        + "/continue_from_2039/" + clone_code + "/netcdf/discharge_dailyTot_output.nc", \
rcp_folder_location        + "/continue_from_2059/" + clone_code + "/netcdf/discharge_dailyTot_output.nc", \
rcp_folder_location        + "/continue_from_2061/" + clone_code + "/netcdf/discharge_dailyTot_output.nc", \
rcp_folder_location        + "/continue_from_2092/" + clone_code + "/netcdf/discharge_dailyTot_output.nc", \
]

# time period for each netcdf file
start_years = [1951, 1958, 1988, 1990, 2006, 2030, 2031, 2039, 2059, 2061, 2092]
end_years = []
for i in range(0, len(start_years)-1):
    end_years.append(start_years[i+1] - 1)
end_years.append(2099)

# output folder
output_folder = "/scratch-shared/edwinhs/daily_discharge_aqueduct_flood_analyzer/m17/gfdl-esm2m/rcp8p5/"
# - make and go to the output folder
os.system('rm -r ' + output_folder + "/*")
try:
	os.makedirs(output_folder)
except:
	pass
os.chdir(output_folder)

# output netcdf file
output_netcdf_file = "discharge_dailyTot_output_" + str(start_years[0]) + "-" + str(end_years[len(end_years)-1]) + ".nc4"

# cdo command for merging
cmd = 'cdo -L -f nc4 -z zip -mergetime '
for i in range(0, len(start_years)):
	cmd = cmd + '-selyear,' + str(start_years[i]) + "/" + str(end_years[i]) + " " + netcdf_file_names[i] + " "
cmd = cmd + output_netcdf_file
print(cmd)
os.system(cmd)

# Note that the total number of timesteps/days between 1951 and 2099 must be 54422. 
