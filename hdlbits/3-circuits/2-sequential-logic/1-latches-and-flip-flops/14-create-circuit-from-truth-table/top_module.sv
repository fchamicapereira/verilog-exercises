module top_module(
    input clk,
    input j,
    input k,
    output reg Q
  );

  always @(posedge clk)
  begin
    if (j & k)
      Q <= ~Q;
    else if (j ^ k)
      Q <= j;
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
