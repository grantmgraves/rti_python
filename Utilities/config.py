import configparser
import os
import logging
import rti_python.Comm.adcp_serial_port as adcp_serial


class RtiConfig:
    """
    Read and Write a configuration.
    """

    def __init__(self, file_path='config.ini'):
        # File path to configuration
        self.config_file_path = file_path

        # Create a default config if no config exist
        if not os.path.exists('config.ini'):
            self.create_default_config()

        # Current configuration
        self.config = self.read()

    def write(self):
        """
        Write the configuration.
        :return:
        """
        # Load the configuration file
        try:
            with open(self.config_file_path, 'w') as f:
                self.config.write(f)
        except Exception as e:
            logging.error("Error writing configuration. " + str(e))

    def read(self):
        """
        Read latest configuration in the file.
        :return: Configuration
        """
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file_path)
        return self.config

    def create_default_config(self):
        self.config = configparser.ConfigParser()

        # Write the default config
        self.write()

    def init_terminal_config(self):
        """
        Default configuration for the terminal.
        Call this to add the terminal sections to the config.
        You can later add more to this section here or in your own code.
        :return:
        """
        ports = adcp_serial.get_serial_ports()

        # Verify the section exist
        if not 'Comm' in self.config:
            self.config['Comm'] = {}
            if ports:
                self.config['Comm']['Port'] = ports[0]
            else:
                self.config['Comm']['Port'] = ''
            self.config['Comm']['Baud'] = '115200'
            self.config['Comm']['output_dir'] = os.path.expanduser('~')

            self.write()

        # Verify each value exist
        if not self.config.has_option('Comm', 'Port'):
            if ports:
                self.config['Comm']['Port'] = ports[0]
            else:
                self.config['Comm']['Port'] = ''
            self.write()

        if not self.config.has_option('Comm', 'Baud'):
            self.config['Comm']['Baud'] = '115200'
            self.write()

        if not self.config.has_option('Comm', 'output_dir'):
            self.config['Comm']['output_dir'] = os.path.expanduser('~')
            self.write()

    def init_waves_config(self):
        """
        Default configuration for a waves setup.
        Call this to add the waves sections to the config.
        You can later add more to this section here or in your own code.
        :return:
        """

        # Verify the section exist
        if not 'Waves' in self.config:
            self.config['Waves'] = {}
            self.config['Waves']['output_dir'] = os.path.expanduser('~')
            self.config['Waves']['ens_in_burst'] = '2048'
            self.config['Waves']['selected_bin_1'] = '1'
            self.config['Waves']['selected_bin_2'] = '3'
            self.config['Waves']['selected_bin_3'] = '5'
            self.config['Waves']['corr_thresh'] = '0.25'
            self.config['Waves']['height_source'] = 'vertical'
            self.config['Waves']['pressure_sensor_height'] = '0.0'
            self.config['Waves']['pressure_sensor_offset'] = '0.0'
            self.config['Waves']['latitude'] = '0.0'
            self.config['Waves']['longitude'] = '0.0'

            self.write()

        # Verify each value exist
        if not self.config.has_option('Waves', 'output_dir'):
            self.config['Waves']['output_dir'] = os.path.expanduser('~')
            self.write()

        if not self.config.has_option('Waves', 'ens_in_burst'):
            self.config['Waves']['ens_in_burst'] = '2048'
            self.write()

        if not self.config.has_option('Waves', 'selected_bin_1'):
            self.config['Waves']['selected_bin_1'] = '1'
            self.write()

        if not self.config.has_option('Waves', 'selected_bin_2'):
            self.config['Waves']['selected_bin_2'] = '3'
            self.write()

        if not self.config.has_option('Waves', 'selected_bin_3'):
            self.config['Waves']['selected_bin_3'] = '5'
            self.write()

        if not self.config.has_option('Waves', 'corr_thresh'):
            self.config['Waves']['corr_thresh'] = '0.25'
            self.write()

        if not self.config.has_option('Waves', 'height_source'):
            self.config['Waves']['height_source'] = 'vertical'
            self.write()

        if not self.config.has_option('Waves', 'pressure_sensor_height'):
            self.config['Waves']['pressure_sensor_height'] = '0.0'
            self.write()

        if not self.config.has_option('Waves', 'pressure_sensor_offset'):
            self.config['Waves']['pressure_sensor_offset'] = '0.0'
            self.write()

        if not self.config.has_option('Waves', 'latitude'):
            self.config['Waves']['latitude'] = '0.0'
            self.write()

        if not self.config.has_option('Waves', 'longitude'):
            self.config['Waves']['longitude'] = '0.0'
            self.write()
