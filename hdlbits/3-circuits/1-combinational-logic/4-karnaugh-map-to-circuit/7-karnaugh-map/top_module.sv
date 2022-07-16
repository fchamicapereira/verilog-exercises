module top_module(
    input [4:1] x,
    output f
  );

  assign f = ~((x[2]&~x[3]&~x[4])|(~x[3]&x[4])|(x[1]&~x[2]&x[3]&x[4])|(x[1]&x[2]&x[3]&~x[4]));

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
