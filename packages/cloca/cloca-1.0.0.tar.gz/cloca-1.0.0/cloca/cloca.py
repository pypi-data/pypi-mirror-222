class Cloca:
    """
    A global clock class that allows time incrementation, retrieval, and reset.

    Attributes
    ----------
    current_time : int
        The current time value.

    Methods
    -------
    increase(increment)
        Increase the current time by the specified increment.

    now()
        Get the current time value.

    reset()
        Reset the current time to 0.

    """
    _instance = None

    def __new__(cls):
        """
        Create a singleton instance of Clocca.

        Returns
        -------
        Cloca
            A singleton instance of Clocca.

        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.current_time = 0
        return cls._instance

    def increase(self, increment=1):
        """
        Increase the current time by the specified increment.

        Parameters
        ----------
        increment : int, optional
            The value by which to increase the current time. Default is 1.

        """
        self.current_time += increment

    def now(self):
        """
        Get the current time value.

        Returns
        -------
        int
            The current time value.

        """
        return self.current_time

    def reset(self):
        """
        Reset the current time to 0.

        """
        self.current_time = 0

