module top_module(
    input clk,
    input d,
    input r,   // synchronous reset
    output reg q
  );
  always @(posedge clk)
  begin
    if (r)
      q <= 0;
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
