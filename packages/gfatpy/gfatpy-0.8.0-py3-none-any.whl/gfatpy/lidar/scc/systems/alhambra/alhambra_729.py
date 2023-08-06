# INSERT HERE THE SYSTEM PARAMETERS
general_parameters = {
    "System": "'ALHAMBRA'",
    "Laser_Pointing_Angle": 5,
    "Molecular_Calc": 0,  # Use US standard atmosphere
    "Latitude_degrees_north": 38.16,
    "Longitude_degrees_east": -3.60,
    "Altitude_meter_asl": 660.0,
    "Call sign": "gr",
}

# LINK YOUR LICEL CHANNELS TO SCC PARAMETERS. USE BT0, BC0 ETC AS NAMES (AS IN LICEL FILES).
channel_parameters = {
    "BT0": {
        "channel_ID": 2123,  # 1064fta
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
}
