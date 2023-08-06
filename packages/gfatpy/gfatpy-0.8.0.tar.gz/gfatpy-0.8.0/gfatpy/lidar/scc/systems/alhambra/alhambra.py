from atmospheric_lidar.licel import LicelLidarMeasurement
from . import alhambra_729


class AlhambraLidarMeasurement(LicelLidarMeasurement):
    extra_netcdf_parameters = alhambra_729

    def __init__(self, file_list=None, use_id_as_name=True):
        super(AlhambraLidarMeasurement, self).__init__(file_list, use_id_as_name)

    def set_PT(self):
        """Sets the pressure and temperature at station level .
        The results are stored in the info dictionary.
        """

        self.info["Temperature"] = 25.0
        self.info["Pressure"] = 1020.0
