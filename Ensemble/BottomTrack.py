from rti_python.Ensemble.Ensemble import Ensemble
import logging


class BottomTrack:
    """
    Ensemble Data DataSet.
    Integer values that give details about the ensemble.


    """

    def __init__(self, num_elements=74, element_multiplier=1):
        """
        Initialize the object
        :param num_elements:  Number of elements.  74 for 4 Beam system, 59 for 3 beam, 29 for 1 beam
        :param element_multiplier: Element mulitplier = 1 always
        """
        self.ds_type = 10                                   # Float
        self.num_elements = num_elements
        self.element_multiplier = element_multiplier
        self.image = 0
        self.name_len = 8
        self.Name = "E000010\0"

        self.FirstPingTime = 0.0
        self.LastPingTime = 0.0
        self.Heading = 0.0
        self.Pitch = 0.0
        self.Roll = 0.0
        self.WaterTemp = 0.0
        self.SystemTemp = 0.0
        self.Salinity = 0.0
        self.Pressure = 0.0
        self.TransducerDepth = 0.0
        self.SpeedOfSound = 0.0
        self.Status = 0.0
        self.NumBeams = 0.0
        self.ActualPingCount = 0.0
        self.Range = []
        self.SNR = []
        self.Amplitude = []
        self.Correlation = []
        self.BeamVelocity = []
        self.BeamGood = []
        self.InstrumentVelocity = []
        self.InstrumentGood = []
        self.EarthVelocity = []
        self.EarthGood = []
        self.SNR_PulseCoherent = []
        self.Amp_PulseCoherent = []
        self.Vel_PulseCoherent = []
        self.Noise_PulseCoherent = []
        self.Corr_PulseCoherent = []

        """
        for beams in range(element_multiplier):
            self.Range.append(Ensemble().BadVelocity)
            self.SNR.append(Ensemble().BadVelocity)
            self.Amplitude.append(Ensemble().BadVelocity)
            self.Correlation.append(Ensemble().BadVelocity)
            self.BeamVelocity.append(Ensemble().BadVelocity)
            self.BeamGood.append(Ensemble().BadVelocity)
            self.InstrumentVelocity.append(Ensemble().BadVelocity)
            self.InstrumentGood.append(Ensemble().BadVelocity)
            self.EarthVelocity.append(Ensemble().BadVelocity)
            self.EarthGood.append(Ensemble().BadVelocity)
        """

    def decode(self, data):
        """
        Take the data bytearray.  Decode the data to populate
        the velocities.
        :param data: Bytearray for the dataset.
        """
        packet_pointer = Ensemble.GetBaseDataSize(self.name_len)

        self.FirstPingTime = Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * 0, Ensemble().BytesInFloat, data)
        self.LastPingTime = Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * 1, Ensemble().BytesInFloat, data)
        self.Heading = Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * 2, Ensemble().BytesInFloat, data)
        self.Pitch = Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * 3, Ensemble().BytesInFloat, data)
        self.Roll = Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * 4, Ensemble().BytesInFloat, data)
        self.WaterTemp = Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * 5, Ensemble().BytesInFloat, data)
        self.SystemTemp = Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * 6, Ensemble().BytesInFloat, data)
        self.Salinity = Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * 7, Ensemble().BytesInFloat, data)
        self.Pressure = Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * 8, Ensemble().BytesInFloat, data)
        self.TransducerDepth = Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * 9, Ensemble().BytesInFloat, data)
        self.SpeedOfSound = Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * 10, Ensemble().BytesInFloat, data)
        self.Status = Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * 11, Ensemble().BytesInFloat, data)
        self.NumBeams = Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * 12, Ensemble().BytesInFloat, data)
        self.ActualPingCount = Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * 13, Ensemble().BytesInFloat, data)

        index = 14
        numBeam = int(self.NumBeams)
        for beams in range(numBeam):
            self.Range.append(Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * index, Ensemble().BytesInFloat, data))
            index += 1

        for beams in range(numBeam):
            self.SNR.append(Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * index, Ensemble().BytesInFloat, data))
            index += 1

        for beams in range(numBeam):
            self.Amplitude.append(Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * index, Ensemble().BytesInFloat, data))
            index += 1

        for beams in range(numBeam):
            self.Correlation.append(Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * index, Ensemble().BytesInFloat, data))
            index += 1

        for beams in range(numBeam):
            self.BeamVelocity.append(Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * index, Ensemble().BytesInFloat, data))
            index += 1

        for beams in range(numBeam):
            self.BeamGood.append(Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * index, Ensemble().BytesInFloat, data))
            index += 1

        for beams in range(numBeam):
            self.InstrumentVelocity.append(Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * index, Ensemble().BytesInFloat, data))
            index += 1

        for beams in range(numBeam):
            self.InstrumentGood.append(Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * index, Ensemble().BytesInFloat, data))
            index += 1

        for beams in range(numBeam):
            self.EarthVelocity.append(Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * index, Ensemble().BytesInFloat, data))
            index += 1

        for beams in range(numBeam):
            self.EarthGood.append(Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * index, Ensemble().BytesInFloat, data))
            index += 1

        if self.num_elements > 54:
            for beams in range(numBeam):
                self.SNR_PulseCoherent.append(Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * index, Ensemble().BytesInFloat, data))
                index += 1

            for beams in range(numBeam):
                self.Amp_PulseCoherent.append(Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * index, Ensemble().BytesInFloat, data))
                index += 1

            for beams in range(numBeam):
                self.Vel_PulseCoherent.append(Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * index, Ensemble().BytesInFloat, data))
                index += 1

            for beams in range(numBeam):
                self.Noise_PulseCoherent.append(Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * index, Ensemble().BytesInFloat, data))
                index += 1

            for beams in range(numBeam):
                self.Corr_PulseCoherent.append(Ensemble.GetFloat(packet_pointer + Ensemble().BytesInFloat * index, Ensemble().BytesInFloat, data))
                index += 1
        else:
            # Fill in with 0.0
            for beams in range(numBeam):
                self.SNR_PulseCoherent.append(0.0)

            for beams in range(numBeam):
                self.Amp_PulseCoherent.append(0.0)

            for beams in range(numBeam):
                self.Vel_PulseCoherent.append(0.0)

            for beams in range(numBeam):
                self.Noise_PulseCoherent.append(0.0)

            for beams in range(numBeam):
                self.Corr_PulseCoherent.append(0.0)

        logging.debug(self.FirstPingTime)
        logging.debug(self.LastPingTime)
        logging.debug(self.Heading)
        logging.debug(self.Pitch)
        logging.debug(self.Roll)
        logging.debug(self.Salinity)
        logging.debug(self.SpeedOfSound)
        logging.debug(self.EarthVelocity)

    def avg_range(self):
        # Average the ranges
        #range_count = 0
        #range_accum = 0.0
        #for beam in range(int(self.NumBeams)):
        #    if self.Range[beam] > 0.0:
        #        range_count += 1
        #        range_accum += self.Range[beam]
        #if range_count > 0:
        #    return range_accum / range_count
        #else:
        #    return 0.0
        return Ensemble.get_avg_range(self.Range)

    def status_str(self):
        """
        Convert the status value to a string.
        :return: Status value as a string.
        """
        BT_LONG_LAG = 0x0001;
        BT_BT_3BEAM_SOLUTION = 0x0002;
        BT_HOLD = 0x0004;
        BT_SEARCHING = 0x0008;
        BT_LR = 0x0010;
        BT_COAST = 0x0020;
        BT_PROOF = 0x0040;
        OVERTEMP = 0x0020;
        BT_LOWGAIN = 0x0080;
        ERR_HEADING_SENSOR = 0x0100;
        ERR_PRESSURE_SENSOR = 0x0200;
        ERR_POWER_DOWN_FAILURE = 0x0400;
        ERR_NONVOLATILE_DATA = 0x0800;
        ERR_RTC = 0x1000;
        ERR_TEMPERATURE = 0x2000;
        ERR_RCVR_DATA = 0x4000;
        ERR_RCVR_TIMEOUT = 0x8000;
        ERR_LOW_VOLTAGE = 0xFFFF;

        result_str = ""
        if self.Status & BT_LONG_LAG:
            result_str += "Bottom Track Long Lag, "
        if self.Status & BT_BT_3BEAM_SOLUTION:
            result_str += "Bottom Track 3 Beam Solution"
        if self.Status & BT_HOLD:
            result_str += "Bottom Track Search: HOLD, "
        if self.Status & BT_SEARCHING:
            result_str += "Bottom Track Search: SEARCHING, "
        if self.Status & BT_LR:
            result_str += "Bottom Track Long Range [Narrowband Mode], "
        if self.Status & BT_COAST:
            result_str += "Bottom Track Coast, "
        if self.Status & BT_PROOF:
            result_str += "Bottom Track Search: PROOF, "
        if self.Status & OVERTEMP:
            result_str += "Over Temperature, "
        if self.Status & BT_LOWGAIN:
            result_str += "Bottom Track Low Gain (Shallow Water Mode), "
        if self.Status & ERR_HEADING_SENSOR:
            result_str += "Heading Sensor Error, "
        if self.Status & ERR_PRESSURE_SENSOR:
            result_str += "Pressure Sensor Error, "
        if self.Status & ERR_POWER_DOWN_FAILURE:
            result_str += "Error Powering Down, "
        if self.Status & ERR_NONVOLATILE_DATA:
            result_str += "Error in NonVolatile Data: "
        if self.Status & ERR_RTC:
            result_str += "RTC Error, "
        if self.Status & ERR_TEMPERATURE:
            result_str += "Temperature Error, "
        if self.Status & ERR_RCVR_DATA:
            result_str += "Receiver Data Error, "
        if self.Status & ERR_RCVR_TIMEOUT:
            result_str += "Receiver Timeout, "
        if self.Status == ERR_LOW_VOLTAGE:
            result_str += "Low Voltage, "

        return result_str

    def encode(self):
        """
        Encode the data into RTB format.
        :return:
        """
        result = []

        self.num_elements = (15 * int(self.NumBeams)) + 14

        # Generate header
        result += Ensemble.generate_header(self.ds_type,
                                           self.num_elements,
                                           self.element_multiplier,
                                           self.image,
                                           self.name_len,
                                           self.Name)

        # Add the data
        result += Ensemble.float_to_bytes(self.FirstPingTime)
        result += Ensemble.float_to_bytes(self.LastPingTime)
        result += Ensemble.float_to_bytes(self.Heading)
        result += Ensemble.float_to_bytes(self.Pitch)
        result += Ensemble.float_to_bytes(self.Roll)
        result += Ensemble.float_to_bytes(self.WaterTemp)
        result += Ensemble.float_to_bytes(self.SystemTemp)
        result += Ensemble.float_to_bytes(self.Salinity)
        result += Ensemble.float_to_bytes(self.Pressure)
        result += Ensemble.float_to_bytes(self.TransducerDepth)
        result += Ensemble.float_to_bytes(self.SpeedOfSound)
        result += Ensemble.float_to_bytes(self.Status)
        result += Ensemble.float_to_bytes(self.NumBeams)
        result += Ensemble.float_to_bytes(self.ActualPingCount)

        for beam in range(len(self.Range)):
            result += Ensemble.float_to_bytes(self.Range[beam])

        for beam in range(len(self.SNR)):
            result += Ensemble.float_to_bytes(self.SNR[beam])

        for beam in range(len(self.Amplitude)):
            result += Ensemble.float_to_bytes(self.Amplitude[beam])

        for beam in range(len(self.Correlation)):
            result += Ensemble.float_to_bytes(self.Correlation[beam])

        for beam in range(len(self.BeamVelocity)):
            result += Ensemble.float_to_bytes(self.BeamVelocity[beam])

        for beam in range(len(self.BeamGood)):
            result += Ensemble.float_to_bytes(self.BeamGood[beam])

        for beam in range(len(self.InstrumentVelocity)):
            result += Ensemble.float_to_bytes(self.InstrumentVelocity[beam])

        for beam in range(len(self.InstrumentGood)):
            result += Ensemble.float_to_bytes(self.InstrumentGood[beam])

        for beam in range(len(self.EarthVelocity)):
            result += Ensemble.float_to_bytes(self.EarthVelocity[beam])

        for beam in range(len(self.EarthGood)):
            result += Ensemble.float_to_bytes(self.EarthGood[beam])

        for beam in range(len(self.SNR_PulseCoherent)):
            result += Ensemble.float_to_bytes(self.SNR_PulseCoherent[beam])

        for beam in range(len(self.Amp_PulseCoherent)):
            result += Ensemble.float_to_bytes(self.Amp_PulseCoherent[beam])

        for beam in range(len(self.Vel_PulseCoherent)):
            result += Ensemble.float_to_bytes(self.Vel_PulseCoherent[beam])

        for beam in range(len(self.Noise_PulseCoherent)):
            result += Ensemble.float_to_bytes(self.Vel_PulseCoherent[beam])

        for beam in range(len(self.Corr_PulseCoherent)):
            result += Ensemble.float_to_bytes(self.Vel_PulseCoherent[beam])

        return result

    def encode_csv(self, dt, ss_code, ss_config, blank=0, bin_size=0):
        """
        Encode into CSV format.
        :param dt: Datetime object.
        :param ss_code: Subsystem code.
        :param ss_config: Subsystem Configuration
        :param blank: Blank or first bin position in meters.
        :param bin_size: Bin size in meters.
        :return: List of CSV lines.
        """
        str_result = []

        # Create the CSV strings
        str_result.append(Ensemble.gen_csv_line(dt, Ensemble.CSV_BT_HEADING, ss_code, ss_config, 0, 0, blank, bin_size, self.Heading))
        str_result.append(Ensemble.gen_csv_line(dt, Ensemble.CSV_BT_PITCH, ss_code, ss_config, 0, 0, blank, bin_size, self.Pitch))
        str_result.append(Ensemble.gen_csv_line(dt, Ensemble.CSV_BT_ROLL, ss_code, ss_config, 0, 0, blank, bin_size, self.Roll))
        str_result.append(Ensemble.gen_csv_line(dt, Ensemble.CSV_BT_PRESSURE, ss_code, ss_config, 0, 0, blank, bin_size, self.Pressure))
        str_result.append(Ensemble.gen_csv_line(dt, Ensemble.CSV_BT_XDCR_DEPTH, ss_code, ss_config, 0, 0, blank, bin_size, self.TransducerDepth))
        str_result.append(Ensemble.gen_csv_line(dt, Ensemble.CSV_BT_STATUS, ss_code, ss_config, 0, 0, blank, bin_size, self.Status))

        for beams in range(len(self.Range)):
            str_result.append(Ensemble.gen_csv_line(dt, Ensemble.CSV_BT_RANGE, ss_code, ss_config, 0, beams, blank, bin_size, self.Range[beams]))

        for beams in range(len(self.BeamVelocity)):
            str_result.append(Ensemble.gen_csv_line(dt, Ensemble.CSV_BT_BEAM_VEL, ss_code, ss_config, 0, beams, blank, bin_size, self.BeamVelocity[beams]))

        for beams in range(len(self.BeamGood)):
            str_result.append(Ensemble.gen_csv_line(dt, Ensemble.CSV_BT_BEAM_GOOD, ss_code, ss_config, 0, beams, blank, bin_size, self.BeamGood[beams]))

        for beams in range(len(self.InstrumentVelocity)):
            str_result.append(Ensemble.gen_csv_line(dt, Ensemble.CSV_BT_INSTR_VEL, ss_code, ss_config, 0, beams, blank, bin_size, self.InstrumentVelocity[beams]))

        for beams in range(len(self.InstrumentGood)):
            str_result.append(Ensemble.gen_csv_line(dt, Ensemble.CSV_BT_INSTR_GOOD, ss_code, ss_config, 0, beams, blank, bin_size, self.InstrumentGood[beams]))

        for beams in range(len(self.EarthVelocity)):
            str_result.append(Ensemble.gen_csv_line(dt, Ensemble.CSV_BT_EARTH_VEL, ss_code, ss_config, 0, beams, blank, bin_size, self.EarthVelocity[beams]))

        for beams in range(len(self.EarthGood)):
            str_result.append(Ensemble.gen_csv_line(dt, Ensemble.CSV_BT_EARTH_GOOD, ss_code, ss_config, 0, beams, blank, bin_size, self.EarthGood[beams]))

        return str_result
