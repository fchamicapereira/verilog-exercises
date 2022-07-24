module top_module(
    input clk,
    input load,
    input [1:0] ena,
    input [99:0] data,
    output reg [99:0] q
  );

  always @(posedge clk)
  begin
    if (load)
      q <= data;
    else if (ena == 2'b01)
      q <= { q[0], q[99:1] };
    else if (ena == 2'b10)
      q <= { q[98:0], q[99] };
  end

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
