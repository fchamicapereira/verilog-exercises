module top_module(
    input a, b,
    output out_and,
    output out_or,
    output out_xor,
    output out_nand,
    output out_nor,
    output out_xnor,
    output out_anotb
  );

  assign out_and = a & b;
  assign out_or = a | b;
  assign out_xor = a ^ b;
  assign out_nand = ~out_and;
  assign out_nor = ~out_or;
  assign out_xnor = ~out_xor;
  assign out_anotb = a & ~b;

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
