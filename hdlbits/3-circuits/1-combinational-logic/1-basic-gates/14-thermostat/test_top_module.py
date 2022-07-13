import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

def heater(too_cold, too_hot, mode, fan_on):
    return mode & too_cold

def aircon(too_cold, too_hot, mode, fan_on):
    return ~mode & too_hot

def fan(too_cold, too_hot, mode, fan_on):
    return heater(too_cold, too_hot, mode, fan_on) \
        | aircon(too_cold, too_hot, mode, fan_on) \
        | fan_on

@cocotb.test()
async def test(dut):
    for _ in range(100):
        too_cold = rand(1)
        too_hot = rand(1)
        mode = rand(1)
        fan_on = rand(1)

        dut.too_cold.value = too_cold
        dut.too_hot.value = too_hot
        dut.mode.value = mode
        dut.fan_on.value = fan_on

        await Timer(2, units="ns")

        assert dut.heater.value == heater(too_cold, too_hot, mode, fan_on), f"heater test failed with too_cold={dut.too_cold.value} too_hot={dut.too_hot.value} mode={dut.mode.value} fan_on={dut.fan_on.value}"
        assert dut.aircon.value == aircon(too_cold, too_hot, mode, fan_on), f"aircon test failed with too_cold={dut.too_cold.value} too_hot={dut.too_hot.value} mode={dut.mode.value} fan_on={dut.fan_on.value}"
        assert dut.fan.value == fan(too_cold, too_hot, mode, fan_on), f"fan test failed with too_cold={dut.too_cold.value} too_hot={dut.too_hot.value} mode={dut.mode.value} fan_on={dut.fan_on.value}"
