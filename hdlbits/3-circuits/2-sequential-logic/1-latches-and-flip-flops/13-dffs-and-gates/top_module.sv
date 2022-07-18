module my_dff(
    input clk,
    input reset,
    input D,
    output reg Q,
    output Qn
  );

  assign Qn = ~Q;

  always @(posedge clk)
  begin
    if (reset)
      Q <= 1'b0;
    else
      Q <= D;
  end
endmodule

module top_module(
    input clk,
    input reset,
    input x,
    output reg z
  );

  reg q0, q1, q2;
  wire qn0, qn1, qn2;

  my_dff dff0(clk, reset, x ^ q0, q0, qn0);
  my_dff dff1(clk, reset, x & qn1, q1, qn1);
  my_dff dff2(clk, reset, x | qn2, q2, qn2);

  assign z = ~(q0 | q1 | q2);

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
