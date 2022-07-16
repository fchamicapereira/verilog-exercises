module top_module(
    input clk,
    input reset,            // Synchronous reset
    input [7:0] d,
    output reg [7:0] q
  );

  always @(posedge clk)
  begin
    if (reset)
      q = 0;
    else
      q <= d;
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
