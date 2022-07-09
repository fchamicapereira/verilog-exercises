module top_module(
    input a,
    input b,
    output o
  );

  assign o = !(a || b);

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
