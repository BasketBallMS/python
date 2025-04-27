class Television:
    """
    A class representing a basic Television with power, volume, channel, and mute functionality
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Initializes a Television objects with default values
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__prev_volume = self.__volume

    def power(self) -> None:
        """
        Turns the Television on or off
        """
        self.__status = not self.__status

    def mute(self)-> None:
        """
        Mutes or unmutes the television, but only if the TV is on.
        """
        if self.__status:
            if not self.__muted:
                self.__muted = True
                self.__prev_volume = self.__volume
                self.__volume = Television.MIN_VOLUME
            else:
                self.__muted = False
                self.__volume = self.__prev_volume

    def channel_up(self)-> None:
        """
        Brings the channel up in increments of 1
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self)-> None:
        """
        Brings the channel down in increments of 1
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self)-> None:
        """
        Brings the volume up in increments of 1
        """
        if self.__status:
            if self.__muted:
                self.__volume = self.__prev_volume
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
                self.__prev_volume = self.__volume
            else:
                self.__volume = Television.MAX_VOLUME

    def volume_down(self)-> None:
        """
        Brings the volume down in increments of 1
        """
        if self.__status:
            if self.__muted:
                self.__volume = self.__prev_volume
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
                self.__prev_volume = self.__volume
            else:
                self.__volume = Television.MIN_VOLUME

    def __str__(self)-> str:
        """
        Returns a string representation of the Television's current state

        :return: A formatted string showing the power status, current channel, and volume level
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'



