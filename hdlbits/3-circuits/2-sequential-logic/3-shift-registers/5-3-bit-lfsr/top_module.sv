module top_module(
    input [2:0] SW,           // R
    input L,                  // KEY[1]
    input clk,                // KEY[0]
    output reg [2:0] LEDR);   // Q

  always @(posedge clk)
  begin
    LEDR[0] <= (L ? SW[0] : LEDR[2]);
    LEDR[1] <= (L ? SW[1] : LEDR[0]);
    LEDR[2] <= (L ? SW[2] : (LEDR[1] ^ LEDR[2]));
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
