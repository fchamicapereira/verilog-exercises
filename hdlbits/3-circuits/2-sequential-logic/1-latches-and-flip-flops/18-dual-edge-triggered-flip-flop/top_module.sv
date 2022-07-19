module top_module(
    input clk,
    input d,
    output reg q
  );

  /* ***************************************************************
  // My initial solution, definitely not as elegant...

  reg on_pos, on_neg;

  always @(posedge clk)
    on_pos <= d;

  always @(negedge clk)
    on_neg <= d;

  wire on_neg_choice;

  always @(*)
  begin
    if (clk)
      q = on_pos;
    else
      q = on_neg;
  end
  ****************************************************************/

  // This was the provided solution:

  reg p, n;

  // A positive-edge triggered flip-flop
  always @(posedge clk)
    p <= d ^ n;

  // A negative-edge triggered flip-flop
  always @(negedge clk)
    n <= d ^ p;

  // Why does this work?
  // After posedge clk, p changes to d^n. Thus q = (p^n) = (d^n^n) = d.
  // After negedge clk, n changes to d^p. Thus q = (p^n) = (p^d^p) = d.
  // At each (positive or negative) clock edge, p and n FFs alternately
  // load a value that will cancel out the other and cause the new value of d to remain.
  assign q = p ^ n;

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
