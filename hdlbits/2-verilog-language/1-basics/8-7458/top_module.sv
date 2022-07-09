module top_module(
    input p1a, p1b, p1c, p1d, p1e, p1f,
    output p1y,
    input p2a, p2b, p2c, p2d,
    output p2y
  );

  assign p2y = (p2c & p2d) | (p2a & p2b);
  assign p1y = (p1a & p1b & p1c) | (p1d & p1e & p1f);

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
