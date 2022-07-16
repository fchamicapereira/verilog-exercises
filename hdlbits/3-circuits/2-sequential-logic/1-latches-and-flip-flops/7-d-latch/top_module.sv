module top_module(
    input d,
    input ena,
    output reg q
  );

  always @(ena)
  begin
    if (ena)
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
