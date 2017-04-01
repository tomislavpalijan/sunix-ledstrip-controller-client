class Controller:
    """
    Device class that represents a single controller
    """

    DEFAULT_PORT = 5577

    def __init__(self, host: str, port: int, hardware_id: str, model: str):
        """
        Creates a new controller device object
        
        :param host: host address of the controller device
        :param port: the port on which the controller device is listening
        """

        self._host = host
        if not port:
            self._port = 5577
        else:
            self._port = port
        self._hardware_id = hardware_id
        self._model = model

    def __str__(self):
        return ("Host: " + self.get_host() + "\n" +
                "Port: " + str(self.get_port()) + "\n" +
                "Hardware ID: " + self.get_hardware_id() + "\n" +
                "Model: " + self.get_model())

    def get_host(self) -> str:
        """
        :return: The IP/Host address of this device  
        """
        return self._host

    def get_port(self) -> int:
        """
        :return: The port of this device 
        """
        return self._port

    def get_hardware_id(self) -> str:
        """
        :return: The hardware ID of this device (f.ex. 'F0FE6B2333C6') 
        """
        return self._hardware_id

    def get_model(self) -> str:
        """
        :return: The model of this device 
        """
        return self._model
