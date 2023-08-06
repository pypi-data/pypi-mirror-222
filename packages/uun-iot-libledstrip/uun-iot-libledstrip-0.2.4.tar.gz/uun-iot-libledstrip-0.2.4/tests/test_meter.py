import pytest
from enum import IntEnum, auto
from uun_iot_libledstrip import LedStrip, MeterStripSegment, Action, ActionType
from uun_iot_libledstrip.devices import DebugLedDev

red = (255,0,0)
green = (0,255,0)
empty = (0,0,0)

class Overlays(IntEnum):
    FIRST = auto()
    SECOND = auto()

class TestMeterSegmentHook:
    """ Test correct execution of :func:`hook_set_value` function in :meth:`MeterStripSegment.set_value` of :class:`MeterStripSegment`. """
    n = 24

    @pytest.fixture(scope="class")
    def dev(self):
        return DebugLedDev(self.n)

    @staticmethod
    def hook(value, leds, action):
        if value > 100:
            action = Action(ActionType.SOLID, color=(255,0,0))
        else:
            action = Action(ActionType.SOLID, color=(0,255,0))
        return leds, action

    @pytest.fixture(scope="class")
    def segment(self, dev):
        return MeterStripSegment(
                dev, autoshow=True, leds=list(range(self.n)),
                value_min=0, value_max=200,
                hook_set_value=TestMeterSegmentHook.hook
            )

    def test_green(self, segment, dev):
        segment.set_value(20)
        segment.activate()
        assert dev[0] == green and dev[-1] == empty

    def test_red(self, segment, dev):
        segment.set_value(150)
        segment.activate()
        assert dev[0] == red and dev[-1] == empty

    def test_red_full(self, segment, dev):
        segment.set_value(200)
        segment.activate()
        assert dev[0] == red and dev[-1] == red
