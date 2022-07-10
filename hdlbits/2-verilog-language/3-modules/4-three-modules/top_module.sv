module d_flip_flop(
    input logic clk,
    input logic d,
    output logic q
  );

  // wire top_nand;
  // wire bottom_nand;
  // wire not_q;

  // assign top_nand = ~(d & clk);
  // assign bottom_nand = ~(clk & ~d);

  // assign not_q = ~(q & bottom_nand);
  // assign q = ~(top_nand & not_q);

  always @(posedge clk)
  begin
    q <= d;
  end
endmodule

module top_module(
    input clk,
    input d,
    output q
  );

  wire q1;
  wire q2;
  d_flip_flop dff1(clk,d,q1);
  d_flip_flop dff2(clk,q1,q2);
  d_flip_flop dff3(clk,q2,q);
  // d_flip_flop dff(clk,d,q);

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
