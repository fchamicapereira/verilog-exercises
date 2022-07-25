module MUXDFF (
    input clk,
    input w, R, E, L,
    output reg Q
  );
  always @(posedge clk)
  begin
    Q <= (L ? R : (E ? w : Q));
  end
endmodule

module top_module(
    input clk,
    input [3:0] SW,
    input [3:1] KEY,
    output [3:0] LEDR
  );

  MUXDFF muxdff0(clk, LEDR[1], SW[0], KEY[1], KEY[2], LEDR[0]);
  MUXDFF muxdff1(clk, LEDR[2], SW[1], KEY[1], KEY[2], LEDR[1]);
  MUXDFF muxdff2(clk, LEDR[3], SW[2], KEY[1], KEY[2], LEDR[2]);
  MUXDFF muxdff3(clk, KEY[3],  SW[3], KEY[1], KEY[2], LEDR[3]);

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
