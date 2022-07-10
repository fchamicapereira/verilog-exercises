module mod_a(
    output o1,
    output o2,
    input a,
    input b,
    input c,
    input d
  );

  assign o1 = a | b;
  assign o2 = c & d;

endmodule

module top_module(
    input a,
    input b,
    input c,
    input d,
    output o1,
    output o2
  );

  mod_a inst1 (o1,o2,a,b,c,d);

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
