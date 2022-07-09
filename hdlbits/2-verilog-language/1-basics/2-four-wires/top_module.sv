module top_module(
    input a,b,c,
    output w,x,y,z );

  assign w = a;
  assign x = b;
  assign y = b;
  assign z = c;

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
