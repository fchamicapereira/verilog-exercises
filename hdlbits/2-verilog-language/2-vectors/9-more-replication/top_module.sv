module top_module(
    input a, b, c, d, e,
    output [24:0] o
  );

  wire [24:0] top, bottom;
  assign top = { {5{a}}, {5{b}}, {5{c}}, {5{d}}, {5{e}} };
  assign bottom = {5{a,b,c,d,e}};
  assign o = ~top ^ bottom;

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
