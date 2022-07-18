module top_module(
    input clk,
    input L,
    input r_in,
    input q_in,
    output reg Q
  );

  always @(posedge clk)
  begin
    Q <= (L ? r_in : q_in);
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
