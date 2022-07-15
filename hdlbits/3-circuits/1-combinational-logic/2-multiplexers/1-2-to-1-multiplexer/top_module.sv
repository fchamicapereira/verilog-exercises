module top_module(
    input a, b, sel,
    output out
  );

  assign out = sel ? b : a;

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
