module top_module(
    input a,
    input b,
    input c,
    input d,
    output out_sop,
    output out_pos
  );

  assign out_sop = (c&d) | (~a&~b&c&~d);
  assign out_pos = ~(~c | (a&c&~d) | (~a&b&c&~d));

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
