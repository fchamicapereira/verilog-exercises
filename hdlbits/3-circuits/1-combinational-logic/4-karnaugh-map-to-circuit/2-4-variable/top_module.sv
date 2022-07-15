module top_module(
    input a,
    input b,
    input c,
    input d,
    output out
  );

  assign out = ~((~a&~b&~c&~d) | (~a&~b&~c&d) | (~a&b&~c&d) | (~a&b&c&d) | (~a&b&c&~d));

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
