
import logging
from datetime import datetime
import json as json_lib

import requests

_logger = logging.getLogger("nec_beamer")

# Default values for the NEC Beamer
NAME="NEC Beamer"
IP_ADDRESS="192.168.0.175"

class Nec_Beamer:
    def __init__(self, ip_address, name) -> None:
        self._ip_address = ip_address if ip_address else IP_ADDRESS
        self._is_on = False
        self._name = name if isinstance(name, str) else "NEC Beamer"
        self._is_available = False
        self._lamp_life_remaining = 0  # top.statusF.document.stat.textfield.value='81';
        self._lamp_hours = 0  # top.statusF.document.stat.textfield2.value='0390';
        self._filter_hours = 0  # top.statusF.document.stat.textfield4.value='0396';
        self._projektor_hours_used = (
            0  # top.statusF.document.stat.textfield6.value='0019';
        )
        self.__json = False

        """
        - Power ON  `/scripts/IsapiExtPj.dll?D=%05%02%00%00%00%00`
        - Power OFF `/scripts/IsapiExtPj.dll?D=%05%02%01%00%00%00`

        - Select Source
        - 'src_rgb1','/scripts/IsapiExtPj.dll?D=%07%02%03%00%00%02%01%01'
        - 'src_rgb2','/scripts/IsapiExtPj.dll?D=%07%02%03%00%00%02%01%02'
        - 'src_rgb3','/scripts/IsapiExtPj.dll?D=%07%02%03%00%00%02%01%1A'
        - 'src_comp','/scripts/IsapiExtPj.dll?D=%07%02%03%00%00%02%01%10'
        - 'src_vidn','/scripts/IsapiExtPj.dll?D=%07%02%03%00%00%02%01%06'
        - 'src_svid','/scripts/IsapiExtPj.dll?D=%07%02%03%00%00%02%01%0B'
        - 'src_view','/scripts/IsapiExtPj.dll?D=%07%02%03%00%00%02%01%1F'
        - 'src_lann','/scripts/IsapiExtPj.dll?D=%07%02%03%00%00%02%01%20'

        - Picture Control
        - 'bri_up', '/scripts/IsapiExtPj.dll?D=%0A%03%10%00%00%05%00%FF%01%03%00'
        - 'cnt_up', '/scripts/IsapiExtPj.dll?D=%0A%03%10%00%00%05%01%FF%01%03%00'
        - 'col_up', '/scripts/IsapiExtPj.dll?D=%0A%03%10%00%00%05%02%FF%01%03%00'
        - 'hue_up', '/scripts/IsapiExtPj.dll?D=%0A%03%10%00%00%05%03%FF%01%03%00'
        - 'shp_up', '/scripts/IsapiExtPj.dll?D=%0A%03%10%00%00%05%04%FF%01%01%00'
        - 'bri_dw', '/scripts/IsapiExtPj.dll?D=%0A%03%10%00%00%05%00%FF%01%FD%FF'
        - 'cnt_dw', '/scripts/IsapiExtPj.dll?D=%0A%03%10%00%00%05%01%FF%01%FD%FF'
        - 'col_dw', '/scripts/IsapiExtPj.dll?D=%0A%03%10%00%00%05%02%FF%01%FD%FF'
        - 'hue_dw', '/scripts/IsapiExtPj.dll?D=%0A%03%10%00%00%05%03%FF%01%FD%FF'
        - 'shp_dw', '/scripts/IsapiExtPj.dll?D=%0A%03%10%00%00%05%04%FF%01%FF%FF'

        """

        self._commands = {
            "power_on": "/scripts/IsapiExtPj.dll?D=%05%02%00%00%00%00",
            "power_off": "/scripts/IsapiExtPj.dll?D=%05%02%01%00%00%00",
            "source_rgb1": "/scripts/IsapiExtPj.dll?D=%07%02%03%00%00%02%01%01",
            "source_rgb2": "/scripts/IsapiExtPj.dll?D=%07%02%03%00%00%02%01%02",
            "source_rgb3": "/scripts/IsapiExtPj.dll?D=%07%02%03%00%00%02%01%1A",
            "source_comp": "/scripts/IsapiExtPj.dll?D=%07%02%03%00%00%02%01%10",
            "source_vidn": "/scripts/IsapiExtPj.dll?D=%07%02%03%00%00%02%01%06",
            "source_svid": "/scripts/IsapiExtPj.dll?D=%07%02%03%00%00%02%01%0B",
            "source_view": "/scripts/IsapiExtPj.dll?D=%07%02%03%00%00%02%01%1F",
            "source_lann": "/scripts/IsapiExtPj.dll?D=%07%02%03%00%00%02%01%20",
            "bri_up": "/scripts/IsapiExtPj.dll?D=%0A%03%10%00%00%05%00%FF%01%03%00",
            "cnt_up": "/scripts/IsapiExtPj.dll?D=%0A%03%10%00%00%05%01%FF%01%03%00",
            "col_up": "/scripts/IsapiExtPj.dll?D=%0A%03%10%00%00%05%02%FF%01%03%00",
            "hue_up": "/scripts/IsapiExtPj.dll?D=%0A%03%10%00%00%05%03%FF%01%03%00",
            "shp_up": "/scripts/IsapiExtPj.dll?D=%0A%03%10%00%00%05%04%FF%01%01%00",
            "bri_dw": "/scripts/IsapiExtPj.dll?D=%0A%03%10%00%00%05%00%FF%01%FD%FF",
            "cnt_dw": "/scripts/IsapiExtPj.dll?D=%0A%03%10%00%00%05%01%FF%01%FD%FF",
            "col_dw": "/scripts/IsapiExtPj.dll?D=%0A%03%10%00%00%05%02%FF%01%FD%FF",
            "hue_dw": "/scripts/IsapiExtPj.dll?D=%0A%03%10%00%00%05%03%FF%01%FD%FF",
            "shp_dw": "/scripts/IsapiExtPj.dll?D=%0A%03%10%00%00%05%04%FF%01%FF%FF",
            # time in HHmmss
            "update": f"/scripts/IsapiExtPj.dll?S={datetime.now().strftime('%H%M%S')}",
        }

        # self.update()

    def __send_command(self, command):
        if command not in self._commands:
            _logger.error(f"Command %s not found", command)
            return
        _logger.info(f"Sending command to NEC Beamer: %s", command)
        command = self._commands[command] if command in self._commands else command
        url = f"http://{self._ip_address}{command}"
        _logger.info(f"with this URL: %s", url)

        try:
            response = requests.get(url, timeout=5)
            _logger.debug(f"Response from NEC Beamer: %s", response.text)

        except requests.exceptions.RequestException as e:
            _logger.error(f"Error sending command to NEC Beamer: %s", e)
            self._is_available = False
            # create a object with status_code 500 to return
            response = requests.models.Response()
            response.status_code = 500
            return response
            # return {"status_code": 500}
        self._is_available = True
        _logger.debug(f"set is_available to %s", self._is_available)
        return response

    def __check_response_status_and_update(self, response):
        if response.status_code != 200:
            _logger.error(
                f"Error sending command to NEC Beamer: %s", response.status_code
            )
            return False

        if "power_on_b.gif" and "power_off_g.gif" in response.text:
            self._is_on = False
        elif "power_on_g.gif" and "power_off_b.gif" in response.text:
            self._is_on = True
        else:
            _logger.error(f"Error updating NEC Beamer: %s", response.status_code)
            return False

        # parse response.text for lamp life remaining, lamp hours, filter hours, projector hours used
        # get line from response.text that contains "top.statusF.document.stat.textfield.value= and extract the value

        if "top.statusF.document.stat.textfield.value=" in response.text:
            self._lamp_life_remaining = response.text.split(
                "top.statusF.document.stat.textfield.value="
            )[1].split(";")[0]

        # get line from response.text that contains "top.statusF.document.stat.textfield2.value= and extract the value

        if "top.statusF.document.stat.textfield2.value=" in response.text:
            self._lamp_hours = response.text.split(
                "top.statusF.document.stat.textfield2.value="
            )[1].split(";")[0]

        # get line from response.text that contains "top.statusF.document.stat.textfield4.value= and extract the value

        if "top.statusF.document.stat.textfield4.value=" in response.text:
            self._filter_hours = response.text.split(
                "top.statusF.document.stat.textfield4.value="
            )[1].split(";")[0]

        # get line from response.text that contains "top.statusF.document.stat.textfield6.value= and extract the value

        if "top.statusF.document.stat.textfield6.value=" in response.text:
            self._projektor_hours_used = response.text.split(
                "top.statusF.document.stat.textfield6.value="
            )[1].split(";")[0]

        # clean up values and convert to int if possible (values are like: '81')

        def __clean_value(value):
            if isinstance(value, str):
                value = value.replace("'", "").replace(" ", "")
            if value == "true" or value == "True":
                return True
            elif value == "false" or value == "False":
                return False
            elif isinstance(value, bool):
                return value
            elif value.isnumeric():
                return int(value)
            else:
                _logger.debug(f"unrecognized Value: %s", value)
                return value

        self._lamp_life_remaining = __clean_value(self._lamp_life_remaining)
        self._lamp_hours = __clean_value(self._lamp_hours)
        self._filter_hours = __clean_value(self._filter_hours)
        self._projektor_hours_used = __clean_value(self._projektor_hours_used)
        self._is_available = __clean_value(self._is_available)
        self._is_on = __clean_value(self._is_on)

        return True

    @property
    def name(self):
        return self._name

    @property
    def is_on(self):
        return self._is_on

    @property
    def is_available(self):
        return self._is_available

    def turn_on(self):
        response = self.__send_command("power_on")

        if response.status_code == 200:
            self._is_on = True
        else:
            self._is_on = False
            _logger.error(f"Error turning on NEC Beamer: %s", response.status_code)

    def turn_off(self):
        response = self.__send_command("power_off")

        if response.status_code == 200:
            self._is_on = False
        else:
            self._is_on = True
            _logger.error(f"Error turning off NEC Beamer: %s", response.status_code)

#    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    def update(self):
        response = self.__send_command("update")
        try:
            if response.status_code == 200:
                self.__check_response_status_and_update(response)
            else:
                self._is_on = False
                self._is_available = False
                _logger.error(f"Error updating NEC Beamer: %s", response.status_code)
        except AttributeError as e:
            self._is_on = False
            self._is_available = False
            _logger.error(f"Error in updating NEC Beamer. Cannot connect.")
            _logger.debug(f"AttributeError: %s", e)
            _logger.debug(f"Response: %s", response)

    @property
    def lamp_life_remaining(self):
        return self._lamp_life_remaining

    @property
    def lamp_hours(self):
        return self._lamp_hours

    @property
    def filter_hours(self):
        return self._filter_hours

    @property
    def projektor_hours_used(self):
        return self._projektor_hours_used

    def source_rgb1(self):
        response = self.__send_command("source_rgb1")

    def source_rgb2(self):
        response = self.__send_command("source_rgb2")

    def source_rgb3(self):
        response = self.__send_command("source_rgb3")

    def source_comp(self):
        response = self.__send_command("source_comp")

    def source_vidn(self):
        response = self.__send_command("source_vidn")

    def source_svid(self):
        response = self.__send_command("source_svid")

    def source_view(self):
        response = self.__send_command("source_view")

    def source_lann(self):
        response = self.__send_command("source_lann")

    def bri_up(self):
        response = self.__send_command("bri_up")

    def cnt_up(self):
        response = self.__send_command("cnt_up")

    def col_up(self):
        response = self.__send_command("col_up")

    def hue_up(self):
        response = self.__send_command("hue_up")

    def shp_up(self):
        response = self.__send_command("shp_up")

    def bri_dw(self):
        response = self.__send_command("bri_dw")

    def cnt_dw(self):
        response = self.__send_command("cnt_dw")

    def col_dw(self):
        response = self.__send_command("col_dw")

    def hue_dw(self):
        response = self.__send_command("hue_dw")

    def shp_dw(self):
        response = self.__send_command("shp_dw")

    def __repr__(self) -> str:
        return f"Nec_Beamer({self._ip_address}, {self._name})"

    def __str__(self) -> str:
        return f"Nec_Beamer({self._ip_address}, {self._name})"

    def print_status(self, json=False):

        if json or self.__json:
            print(json_lib.dumps(self.__dict__, indent=4, sort_keys=True))
            _logger.debug(json_lib.dumps(self.__dict__, indent=4, sort_keys=True))
            return
        print(f"Name: {self._name}")
        print(f"IP Address: {self._ip_address}")
        print(f"Is On: {self._is_on}")
        print(f"Is Available: {self._is_available}")
        print(f"Lamp Life Remaining: {self._lamp_life_remaining}")
        print(f"Lamp Hours: {self._lamp_hours}")
        print(f"Filter Hours: {self._filter_hours}")
        print(f"Projektor Hours Used: {self._projektor_hours_used}")
