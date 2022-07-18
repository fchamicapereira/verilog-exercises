module top_module(
    input clk,
    input areset,   // active high asynchronous reset
    input [7:0] d,
    output reg [7:0] q
  );

  always @(posedge clk, posedge areset)
  begin
    if (areset)
      q <= 8'b0;
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
