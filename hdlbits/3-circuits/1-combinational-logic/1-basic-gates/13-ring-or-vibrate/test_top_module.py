import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

@cocotb.test()
async def test(dut):
    for ring in range(2):
        for vibrate_mode in range(2):
            dut.ring.value = ring
            dut.vibrate_mode.value = vibrate_mode

            await Timer(2, units="ns")
            assert dut.ringer.value == (1 if ring == 1 and vibrate_mode == 0 else 0), f"test failed with ring={dut.ring.value} vibrate_mode={dut.vibrate_mode.value} ringer={dut.ringer.value}"
            assert dut.motor.value == (1 if ring == 1 and vibrate_mode == 1 else 0), f"test failed with ring={dut.ring.value} vibrate_mode={dut.vibrate_mode.value} motor={dut.motor.value}"
            assert dut.ring.value == 0 or dut.ringer.value != dut.motor.value, f"test failed with ring={dut.ring.value} vibrate_mode={dut.vibrate_mode.value} ringer={dut.ringer.value} motor={dut.motor.value}"
