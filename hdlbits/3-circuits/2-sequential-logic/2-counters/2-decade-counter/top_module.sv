module top_module(
    input clk,
    input reset,        // Synchronous active-high reset
    output reg [3:0] q
  );

  always @(posedge clk)
  begin
    if (reset || (q == 4'b1001))
      q <= 4'b0;
    else
      q <= q + 4'b1;
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
