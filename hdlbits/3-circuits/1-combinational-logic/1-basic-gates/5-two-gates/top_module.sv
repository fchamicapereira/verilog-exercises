module top_module(
    input i1,
    input i2,
    input i3,
    output o
  );

  assign o = (~(i1 ^ i2)) ^ i3;

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
