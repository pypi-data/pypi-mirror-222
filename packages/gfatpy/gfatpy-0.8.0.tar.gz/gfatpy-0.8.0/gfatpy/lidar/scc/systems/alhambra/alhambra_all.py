# INSERT HERE THE SYSTEM PARAMETERS
general_parameters = {
    "System": "'ALHAMBRA'",
    "Laser_Pointing_Angle": 5,
    "Molecular_Calc": 0,  # Use US standard atmosphere
    "Latitude_degrees_north": 38.16,
    "Longitude_degrees_east": -3.60,
    "Altitude_meter_asl": 660,
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
    "S2A0": {
        "channel_ID": 9999,  # 1064fta
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "BT1": {
        "channel_ID": 9999,  # 1061fta
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2A1": {
        "channel_ID": 9999,  # 1061fta
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "BC1": {
        "channel_ID": 9999,  # 1061ftp
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2P1": {
        "channel_ID": 9999,  # 1061ftp
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "BT2": {
        "channel_ID": 9999,  # 532fta
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2A2": {
        "channel_ID": 9999,  # 532fta
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "BC2": {
        "channel_ID": 9999,  # 532ftp
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2P2": {
        "channel_ID": 9999,  # 532ftp
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "BT3": {
        "channel_ID": 9999,  # 531fta
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2A3": {
        "channel_ID": 9999,  # 531fta
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "BC3": {
        "channel_ID": 9999,  # 531ftp
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2P3": {
        "channel_ID": 9999,  # 531ftp
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "BT4": {
        "channel_ID": 9999,  # 355fpa
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2A4": {
        "channel_ID": 9999,  # 355fpa
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "BC4": {
        "channel_ID": 9999,  # 355fpp
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2P4": {
        "channel_ID": 9999,  # 355fpp
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "BT5": {
        "channel_ID": 9999,  # 355fsa
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2A5": {
        "channel_ID": 9999,  # 355fsa
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "BC5": {
        "channel_ID": 9999,  # 355fsp
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2P5": {
        "channel_ID": 9999,  # 355fsp
        "Laser_Shots": 1200,
        "DAQ_Range": 100.0,
    },
    "BT6": {
        "channel_ID": 9999,  # 354fta
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2A6": {
        "channel_ID": 9999,  # 354fta
        "Laser_Shots": 1200,
        "DAQ_Range": 100.0,
    },
    "BC6": {
        "channel_ID": 9999,  # 354ftp
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2P6": {
        "channel_ID": 9999,  # 354ftp
        "Laser_Shots": 1200,
        "DAQ_Range": 100.0,
    },
    "BT7": {
        "channel_ID": 9999,  # 408fta
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2A7": {
        "channel_ID": 9999,  # 408fta
        "Laser_Shots": 1200,
        "DAQ_Range": 100.0,
    },
    "BC7": {
        "channel_ID": 9999,  # 408ftp
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2P7": {
        "channel_ID": 9999,  # 408ftp
        "Laser_Shots": 1200,
        "DAQ_Range": 100.0,
    },
    "BT10": {
        "channel_ID": 9999,  # 1064nta
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2A10": {
        "channel_ID": 9999,  # 1064nta
        "Laser_Shots": 1200,
        "DAQ_Range": 100.0,
    },
    "BC10": {
        "channel_ID": 9999,  # 1064ntp
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2P10": {
        "channel_ID": 9999,  # 1064ntp
        "Laser_Shots": 1200,
        "DAQ_Range": 100.0,
    },
    "BT11": {
        "channel_ID": 9999,  # 532npa
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2A11": {
        "channel_ID": 9999,  # 532npa
        "Laser_Shots": 1200,
        "DAQ_Range": 100.0,
    },
    "BC11": {
        "channel_ID": 9999,  # 532npp
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2P11": {
        "channel_ID": 9999,  # 532npp
        "Laser_Shots": 1200,
        "DAQ_Range": 100.0,
    },
    "BT12": {
        "channel_ID": 9999,  # 532nsa
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2A12": {
        "channel_ID": 9999,  # 532nsa
        "Laser_Shots": 1200,
        "DAQ_Range": 100.0,
    },
    "BC12": {
        "channel_ID": 9999,  # 532nsp
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2P12": {
        "channel_ID": 9999,  # 532nsp
        "Laser_Shots": 1200,
        "DAQ_Range": 100.0,
    },
    "BT13": {
        "channel_ID": 9999,  # 355npa
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2A13": {
        "channel_ID": 9999,  # 355npa
        "Laser_Shots": 1200,
        "DAQ_Range": 100.0,
    },
    "BC13": {
        "channel_ID": 9999,  # 355npp
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2P13": {
        "channel_ID": 9999,  # 355npp
        "Laser_Shots": 1200,
        "DAQ_Range": 100.0,
    },
    "BT14": {
        "channel_ID": 9999,  # 355nsa
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2A14": {
        "channel_ID": 9999,  # 355nsa
        "Laser_Shots": 1200,
        "DAQ_Range": 100.0,
    },
    "BC14": {
        "channel_ID": 9999,  # 355nsp
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2P14": {
        "channel_ID": 9999,  # 355nsp
        "Laser_Shots": 1200,
        "DAQ_Range": 100.0,
    },
    "BT15": {
        "channel_ID": 9999,  # 387nta
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2A15": {
        "channel_ID": 9999,  # 387nta
        "Laser_Shots": 1200,
        "DAQ_Range": 100.0,
    },
    "BC15": {
        "channel_ID": 9999,  # 387ntp
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2P15": {
        "channel_ID": 9999,  # 387ntp
        "Laser_Shots": 1200,
        "DAQ_Range": 100.0,
    },
    "BT16": {
        "channel_ID": 9999,  # 607nta
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2A16": {
        "channel_ID": 9999,  # 607nta
        "Laser_Shots": 1200,
        "DAQ_Range": 100.0,
    },
    "BC16": {
        "channel_ID": 9999,  # 607ntp
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2P16": {
        "channel_ID": 9999,  # 607ntp
        "Laser_Shots": 1200,
        "DAQ_Range": 100.0,
    },
    "BT17": {
        "channel_ID": 9999,  # 408nta
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2A17": {
        "channel_ID": 9999,  # 408nta
        "Laser_Shots": 1200,
        "DAQ_Range": 100.0,
    },
    "BC17": {
        "channel_ID": 9999,  # 408ntp
        "Background_Low": 40000.0,
        "Background_High": 50000.0,
        "Laser_Shots": 1200,
        "LR_Input": 1,
        "DAQ_Range": 100.0,
    },
    "S2P17": {
        "channel_ID": 9999,  # 408ntp
        "Laser_Shots": 1200,
        "DAQ_Range": 100.0,
    },
}
