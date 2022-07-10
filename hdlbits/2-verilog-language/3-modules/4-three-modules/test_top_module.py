import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, RisingEdge, Timer

# @cocotb.test()
# async def dff_simple_test(dut):
#     """Test that d propagates to q"""

#     clock = Clock(dut.clk, 10, units="us")
#     cocotb.start_soon(clock.start())

#     # Synchronize with the clock
#     await FallingEdge(dut.clk)

#     for i in range(10):
#         d = rand(1)
#         dut.d.value = d
#         await FallingEdge(dut.clk)
#         assert dut.q.value == d, f"output q was incorrect on the {i}th cycle"

@cocotb.test()
async def test(dut):
    T = 1
    T_units = "ns"

    clock = Clock(dut.clk, T, units=T_units)
    cocotb.start_soon(clock.start())

    # Synchronize with the clock
    await FallingEdge(dut.clk)

    prev_d = 1
    for i in range(10):
        d = 1 if prev_d == 0 else 1
        dut.d.value = d

        await Timer(T, units=T_units)
        # await FallingEdge(dut.clk)
        assert dut.q.value == prev_d, f"randomized test failed with i={i}, T=1, prev={prev_d}, d={dut.d.value}, q={dut.q.value}"

        await Timer(T, units=T_units)
        # await FallingEdge(dut.clk)
        assert dut.q.value == prev_d, f"randomized test failed with i={i}, T=2, prev={prev_d}, d={dut.d.value}, q={dut.q.value}"

        await Timer(T, units=T_units)
        # await FallingEdge(dut.clk)
        assert dut.q.value == d, f"randomized test failed with i={i}, T=3, prev={prev_d}, d={dut.d.value}, q={dut.q.value}"

        prev_d = d
