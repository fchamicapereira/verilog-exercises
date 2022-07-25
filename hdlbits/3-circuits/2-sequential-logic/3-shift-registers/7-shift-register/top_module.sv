module top_module(
    input clk,
    input resetn,   // synchronous reset
    input i,
    output reg o
  );

  reg q1, q2, q3;
  always @(posedge clk)
  begin
    if (~resetn)
    begin
      q3 <= 1'b0;
      q2 <= 1'b0;
      q1 <= 1'b0;
      o <= 1'b0;
    end
    else
    begin
      q3 <= i;
      q2 <= q3;
      q1 <= q2;
      o <= q1;
    end
  end

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
