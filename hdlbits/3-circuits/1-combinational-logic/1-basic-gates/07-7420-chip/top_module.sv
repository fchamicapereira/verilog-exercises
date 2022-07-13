module top_module(
    input p1a, p1b, p1c, p1d,
    output p1y,
    input p2a, p2b, p2c, p2d,
    output p2y
  );

  assign p1y = ~(p1a & p1b & p1c & p1d);
  assign p2y = ~(p2a & p2b & p2c & p2d);

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
