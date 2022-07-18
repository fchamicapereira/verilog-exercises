module top_module(
    input clk,
    input d,
    input ar,   // asynchronous reset
    output reg q
  );

  always @(posedge clk, posedge ar)
  begin
    if (ar)
      q <= 1'b0;
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
