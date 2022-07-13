module top_module(
    input x3,
    input x2,
    input x1,  // three inputs
    output f   // one output
  );

  assign f = (~x1 & x2 & ~x3) | (x1 & x2 & ~x3) | (x1 & ~x2 & x3) | (x1 & x2 & x3);

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
