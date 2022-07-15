module top_module(
    input a,
    input b,
    input c,
    input d,
    output out
  );

  wire n0,n1,n2,n3,n4,n5;

  assign n0 = a & b  & ~c & ~d;
  assign n1 = ~a & b & ~c & d;
  assign n2 = a & b & ~c & d;
  assign n3 = ~a & ~b & c & d;
  assign n4 = a & b & c & ~d;
  assign n5 = a & ~b & c & ~d;

  assign out = ~(n0 | n1 | n2 | n3 | n4 | n5);

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
