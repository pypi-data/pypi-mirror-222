import pytest
from enum import IntEnum, auto
from uun_iot_libledstrip import LedStrip, LedStripSegment, StripOverlayBundle
from uun_iot_libledstrip.devices import DebugLedDev

class Overlays(IntEnum):
    FIRST = auto()
    SECOND = auto()

class TestLedStrip:
    """ Switching between two LED strip layouts using StripBundle. """
    n = 24

    @pytest.fixture(scope="class")
    def dev(self):
        return DebugLedDev(self.n)

    @pytest.fixture(scope="class")
    def sbundle(self, dev):
        segments = {
                Overlays.FIRST:  { i: LedStripSegment(dev, list(range(2*i, 2*i+2)), autoshow=True) for i in range(self.n//2) },
                Overlays.SECOND: { i: LedStripSegment(dev, list(range(3*i, 3*i+3)), autoshow=True) for i in range(self.n//3) }
            }
        strip1 = LedStrip(
                device=dev,
                segments=segments[Overlays.FIRST]
            )
        strip2 = LedStrip(
                device=dev,
                segments=segments[Overlays.SECOND]
            )

        sbundle = StripOverlayBundle({
            Overlays.FIRST: strip1,
            Overlays.SECOND: strip2
        })

        return sbundle

    def test_set_clear_first(self, sbundle, dev):
        color = (255,255,255)
        empty = (0,0,0)

        sbundle.set_strip(Overlays.FIRST)
        sbundle.strip.set_color(color, 2)
        assert dev[2*2] == color and dev[2*2+1] == color

        sbundle.strip.clear()
        assert dev[2*2] == empty and dev[2*2+1] == empty

    def test_set_clear_second(self, sbundle, dev):
        color = (100,0,0)
        empty = (0,0,0)

        sbundle.set_strip(Overlays.SECOND)
        sbundle.strip.set_color(color, 1)
        assert dev[3*1] == color and dev[3*1+1] == color and dev[3*1+2] == color

        sbundle.strip.clear()
        assert dev[3*1] == empty and dev[3*1+1] == empty and dev[3*1+2] == empty
        
    def test_set_entangled(self, sbundle, dev):
        color1 = (255,0,100)
        color2 = (0,255,100)
        empty = (0,0,0)

        sbundle.set_strip(Overlays.FIRST)
        sbundle.strip.set_color(color1, 4)
        assert dev[2*4] == color1 and dev[2*4+1] == color1

        sbundle.set_strip(Overlays.SECOND)
        sbundle.strip.set_color(color2, 2)
        assert dev[3*2] == color2 and dev[3*2+1] == color2 and dev[3*2+2] == color2

        sbundle.set_strip(Overlays.FIRST)
        sbundle.strip.clear()
        assert dev[2*4] == empty and dev[2*4+1] == empty

        sbundle.set_strip(Overlays.SECOND)
        sbundle.strip.clear()
        assert dev[3*2] == empty and dev[3*2+1] == empty and dev[3*2+2] == empty
