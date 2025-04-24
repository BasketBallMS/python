from pytest import *
from television import Television

def test___init__():
    tv = Television()
    assert tv.get_is_power_on() == False
    assert tv.get_is_muted() == False
    assert tv.get_channel() == 0
    assert tv.get_volume() == 0

def test_power():
    tv = Television()
    tv.power()
    assert tv.get_is_power_on() == True
    tv.power()
    assert tv.get_is_power_on() == False

def test_mute():
    tv = Television()
    tv.mute()
    assert tv.get_is_muted() == True
    tv.mute()
    assert tv.get_is_muted() == False

def test_channel_up():
    tv = Television()
    tv.power()
    current_channel = tv.get_channel()
    tv.channel_up()
    expected_channel = current_channel + 1 if current_channel < tv.MAX_CHANNEL else tv.MIN_CHANNEL
    assert tv.get_channel() == expected_channel

def test_channel_down():
    tv = Television()
    tv.power()
    current_channel = tv.get_channel()
    tv.channel_down()
    expected_channel = current_channel - 1 if current_channel > tv.MIN_CHANNEL else tv.MAX_CHANNEL
    assert tv.get_channel() == expected_channel

def test_volume_up():
    tv = Television()
    tv.power()
    current_volume = tv.get_volume()
    tv.volume_up()
    expected_volume = current_volume + 1  if current_volume < tv.MAX_VOLUME else tv.MAX_VOLUME
    assert tv.get_volume() == expected_volume

def test_volume_down():
    tv = Television()
    tv.power()
    current_volume = tv.get_volume()
    tv.volume_down()
    expected_volume = current_volume - 1 if current_volume - 1 > tv.MIN_VOLUME else tv.MIN_VOLUME
    assert tv.get_volume() == expected_volume

def test___str__():
    tv = Television()
    expect_output = "Power = False, Channel = 0, Volume = 0"
    assert str(tv) == expect_output
    tv.power()
    tv.channel_up()
    tv.volume_up()
    assert str(tv) == f'Power = True, Channel = {tv.get_channel()}, Volume = {tv.get_volume()}'

def test():
    pass