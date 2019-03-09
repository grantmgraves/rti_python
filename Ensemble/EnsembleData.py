import struct
from rti_python.Ensemble.Ensemble import Ensemble
import logging
from datetime import datetime


class EnsembleData:
    """
    Ensemble Data DataSet.
    Integer values that give details about the ensemble.
    """

    def __init__(self, num_elements=19, element_multiplier=1):
        self.ds_type = 20
        self.num_elements = num_elements
        self.element_multiplier = element_multiplier
        self.image = 0
        self.name_len = 8
        self.Name = "E000008\0"

        self.EnsembleNumber = 0
        self.NumBins = 0
        self.NumBeams = 0
        self.DesiredPingCount = 0
        self.ActualPingCount = 0
        self.SerialNumber = ""
        self.SysFirmwareMajor = 0
        self.SysFirmwareMinor = 0
        self.SysFirmwareRevision = 0
        self.SysFirmwareSubsystemCode = ""
        self.SubsystemConfig = 0
        self.Status = 0
        self.Year = 0
        self.Month = 0
        self.Day = 0
        self.Hour = 0
        self.Minute = 0
        self.Second = 0
        self.HSec = 0

    def decode(self, data):
        """
        Take the data bytearray.  Decode the data to populate
        the values.
        :param data: Bytearray for the dataset.
        """
        packet_pointer = Ensemble.GetBaseDataSize(self.name_len)

        self.EnsembleNumber = Ensemble.GetInt32(packet_pointer + Ensemble().BytesInInt32 * 0, Ensemble().BytesInInt32, data)
        self.NumBins = Ensemble.GetInt32(packet_pointer + Ensemble().BytesInInt32 * 1, Ensemble().BytesInInt32, data)
        self.NumBeams = Ensemble.GetInt32(packet_pointer + Ensemble().BytesInInt32 * 2, Ensemble().BytesInInt32, data)
        self.DesiredPingCount = Ensemble.GetInt32(packet_pointer + Ensemble().BytesInInt32 * 3, Ensemble().BytesInInt32, data)
        self.ActualPingCount = Ensemble.GetInt32(packet_pointer + Ensemble().BytesInInt32 * 4, Ensemble().BytesInInt32, data)
        self.Status = Ensemble.GetInt32(packet_pointer + Ensemble().BytesInInt32 * 5, Ensemble().BytesInInt32, data)
        self.Year = Ensemble.GetInt32(packet_pointer + Ensemble().BytesInInt32 * 6, Ensemble().BytesInInt32, data)
        self.Month = Ensemble.GetInt32(packet_pointer + Ensemble().BytesInInt32 * 7, Ensemble().BytesInInt32, data)
        self.Day = Ensemble.GetInt32(packet_pointer + Ensemble().BytesInInt32 * 8, Ensemble().BytesInInt32, data)
        self.Hour = Ensemble.GetInt32(packet_pointer + Ensemble().BytesInInt32 * 9, Ensemble().BytesInInt32, data)
        self.Minute = Ensemble.GetInt32(packet_pointer + Ensemble().BytesInInt32 * 10, Ensemble().BytesInInt32, data)
        self.Second = Ensemble.GetInt32(packet_pointer + Ensemble().BytesInInt32 * 11, Ensemble().BytesInInt32, data)
        self.HSec = Ensemble.GetInt32(packet_pointer + Ensemble().BytesInInt32 * 12, Ensemble().BytesInInt32, data)

        self.SerialNumber = str(data[packet_pointer+Ensemble().BytesInInt32*13:packet_pointer+Ensemble().BytesInInt32*21], "UTF-8")
        self.SysFirmwareRevision = struct.unpack("B", data[packet_pointer+Ensemble().BytesInInt32*21 + 0:packet_pointer+Ensemble().BytesInInt32*21 + 1])[0]
        self.SysFirmwareMinor = struct.unpack("B", data[packet_pointer+Ensemble().BytesInInt32*21 + 1:packet_pointer+Ensemble().BytesInInt32*21 + 2])[0]
        self.SysFirmwareMajor = struct.unpack("B", data[packet_pointer + Ensemble().BytesInInt32 * 21 + 2:packet_pointer + Ensemble().BytesInInt32 * 21 + 3])[0]
        self.SysFirmwareSubsystemCode = str(data[packet_pointer + Ensemble().BytesInInt32 * 21 + 3:packet_pointer + Ensemble().BytesInInt32 * 21 + 4], "UTF-8")

        self.SubsystemConfig = struct.unpack("B", data[packet_pointer + Ensemble().BytesInInt32 * 22 + 3:packet_pointer + Ensemble().BytesInInt32 * 22 + 4])[0]

        logging.debug(self.EnsembleNumber)
        logging.debug(str(self.Month) + "/" + str(self.Day) + "/" + str(self.Year) + "  " + str(self.Hour) + ":" + str(self.Minute) + ":" + str(self.Second) + "." + str(self.HSec))
        logging.debug(self.SerialNumber)
        logging.debug(str(self.SysFirmwareMajor) + "." + str(self.SysFirmwareMinor) + "." + str(self.SysFirmwareRevision) + "-" + str(self.SysFirmwareSubsystemCode))
        logging.debug(self.SubsystemConfig)

    def datetime_str(self):
        """
        Return the date and time as a string.
        :return: Date time string.  2013/07/30 21:00:00.00
        """
        return str(self.Year).zfill(4) + "/" + str(self.Month).zfill(2) + "/" + str(self.Day).zfill(2) + " " + str(self.Hour).zfill(2) + ":" + str(self.Minute).zfill(2) + ":" + str(self.Second).zfill(2) + "." + str(self.HSec).zfill(2)

    def datetime(self):
        return datetime(self.Year, self.Month, self.Day, self.Hour, self.Minute, self.Second, self.HSec * 10)

    def firmware_str(self):
        return "{0}.{1}.{2} - {3}".format(self.SysFirmwareMajor, self.SysFirmwareMinor, self.SysFirmwareRevision, self.SysFirmwareSubsystemCode)

    def encode(self):
        """
        Encode the data into RTB format.
        :return:
        """
        result = []

        # Generate header
        result += Ensemble.generate_header(self.ds_type,
                                           self.num_elements,
                                           self.element_multiplier,
                                           self.image,
                                           self.name_len,
                                           self.Name)

        # Add the data
        result += Ensemble.int32_to_bytes(self.EnsembleNumber)
        result += Ensemble.int32_to_bytes(self.NumBins)
        result += Ensemble.int32_to_bytes(self.NumBeams)
        result += Ensemble.int32_to_bytes(self.DesiredPingCount)
        result += Ensemble.int32_to_bytes(self.ActualPingCount)
        result += self.SerialNumber.encode("UTF-8")
        result += bytes([self.SysFirmwareMajor])
        result += bytes([self.SysFirmwareMinor])
        result += bytes([self.SysFirmwareRevision])
        result += self.SysFirmwareSubsystemCode.encode("UTF-8")
        result += bytes([0])
        result += bytes([0])
        result += bytes([0])
        result += bytes([self.SubsystemConfig])
        result += Ensemble.int32_to_bytes(self.Status)
        result += Ensemble.int32_to_bytes(self.Year)
        result += Ensemble.int32_to_bytes(self.Month)
        result += Ensemble.int32_to_bytes(self.Day)
        result += Ensemble.int32_to_bytes(self.Hour)
        result += Ensemble.int32_to_bytes(self.Minute)
        result += Ensemble.int32_to_bytes(self.Second)
        result += Ensemble.int32_to_bytes(self.HSec)

        return result

    def encode_csv(self, dt, ss_code, ss_config):
        """
        Encode into CSV format.
        :param dt: Datetime object.
        :param ss_code: Subsystem code.
        :param ss_config: Subsystem Configuration
        :return: List of CSV lines.
        """
        str_result = []

        # Create the CSV strings
        str_result.append(Ensemble.gen_csv_line(dt, Ensemble.CSV_STATUS, ss_code, ss_config, 0, 0, self.Status))

        return str_result
