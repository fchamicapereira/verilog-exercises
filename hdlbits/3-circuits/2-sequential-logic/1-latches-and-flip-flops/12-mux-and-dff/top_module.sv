module top_module(
    input clk,
    input w, R, E, L,
    output reg Q
  );

  always @(posedge clk)
  begin
    Q <= (L ? R : (E ? w : Q));
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
