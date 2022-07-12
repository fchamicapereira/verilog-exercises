import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

def priority_encoder(d):
    for i,b in enumerate(bin(d)[2:].zfill(4)[::-1]):
        if b == "1":
            return i
    return 0

@cocotb.test()
async def test(dut):
    LEFT  = 0xe06b
    DOWN  = 0xe072
    RIGHT = 0xe074
    UP    = 0xe075

    codes = [ LEFT, DOWN, RIGHT, UP ]

    for _ in range(100):
        choose_from_code = rand(1)

        if choose_from_code == 1:
            scancode = random.choice(codes)
        else:
            scancode = rand(16)

        dut.scancode.value = scancode
        await Timer(2, units="ns")

        if scancode == LEFT:
            assert dut.left.value  == 1, f"randomized test failed with scancode={dut.scancode.value} left={dut.left.value}"
            assert dut.down.value  == 0, f"randomized test failed with scancode={dut.scancode.value} down={dut.down.value}"
            assert dut.right.value == 0, f"randomized test failed with scancode={dut.scancode.value} right={dut.right.value}"
            assert dut.up.value    == 0, f"randomized test failed with scancode={dut.scancode.value} up={dut.up.value}"
        elif scancode == DOWN:
            assert dut.left.value  == 0, f"randomized test failed with scancode={dut.scancode.value} left={dut.left.value}"
            assert dut.down.value  == 1, f"randomized test failed with scancode={dut.scancode.value} down={dut.down.value}"
            assert dut.right.value == 0, f"randomized test failed with scancode={dut.scancode.value} right={dut.right.value}"
            assert dut.up.value    == 0, f"randomized test failed with scancode={dut.scancode.value} up={dut.up.value}"
        elif scancode == RIGHT:
            assert dut.left.value  == 0, f"randomized test failed with scancode={dut.scancode.value} left={dut.left.value}"
            assert dut.down.value  == 0, f"randomized test failed with scancode={dut.scancode.value} down={dut.down.value}"
            assert dut.right.value == 1, f"randomized test failed with scancode={dut.scancode.value} right={dut.right.value}"
            assert dut.up.value    == 0, f"randomized test failed with scancode={dut.scancode.value} up={dut.up.value}"
        elif scancode == UP:
            assert dut.left.value  == 0, f"randomized test failed with scancode={dut.scancode.value} left={dut.left.value}"
            assert dut.down.value  == 0, f"randomized test failed with scancode={dut.scancode.value} down={dut.down.value}"
            assert dut.right.value == 0, f"randomized test failed with scancode={dut.scancode.value} right={dut.right.value}"
            assert dut.up.value    == 1, f"randomized test failed with scancode={dut.scancode.value} up={dut.up.value}"
        else:
            assert dut.left.value  == 0, f"randomized test failed with scancode={dut.scancode.value} left={dut.left.value}"
            assert dut.down.value  == 0, f"randomized test failed with scancode={dut.scancode.value} down={dut.down.value}"
            assert dut.right.value == 0, f"randomized test failed with scancode={dut.scancode.value} right={dut.right.value}"
            assert dut.up.value    == 0, f"randomized test failed with scancode={dut.scancode.value} up={dut.up.value}"
