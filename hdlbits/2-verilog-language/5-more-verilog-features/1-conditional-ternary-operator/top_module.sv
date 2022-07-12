module top_module(
    input [7:0] a, b, c, d,
    output [7:0] min
  );

  wire [7:0] smaller_a_b, smaller_c_d;

  assign smaller_a_b = (a<b) ? a : b;
  assign smaller_c_d = (c<d) ? c : d;
  assign min = (smaller_a_b<smaller_c_d) ? smaller_a_b : smaller_c_d;

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
