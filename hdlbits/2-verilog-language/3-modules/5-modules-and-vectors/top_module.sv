module my_dff8(
    input logic clk,
    input logic [7:0] d,
    output logic [7:0] q
  );

  always @(posedge clk)
  begin
    q <= d;
  end
endmodule

module multiplexer(
    input [1:0] sel,
    input [7:0] d0,
    input [7:0] d1,
    input [7:0] d2,
    input [7:0] d3,
    output [7:0] q
  );
  wire [7:0] sel_d0;
  wire [7:0] sel_d1;
  wire [7:0] sel_d2;
  wire [7:0] sel_d3;

  assign sel_d0 = d0 & {8{~sel[1] && ~sel[0]}};
  assign sel_d1 = d1 & {8{~sel[1] &&  sel[0]}};
  assign sel_d2 = d2 & {8{ sel[1] && ~sel[0]}};
  assign sel_d3 = d3 & {8{ sel[1] &&  sel[0]}};

  assign q = sel_d0 | sel_d1 | sel_d2 | sel_d3;
endmodule

module top_module(
    input clk,
    input [7:0] d,
    input [1:0] sel,
    output [7:0] q
  );
  wire [7:0] q0,q1,q2;

  my_dff8 my_dff8_inst1(clk, d, q0);
  my_dff8 my_dff8_inst2(clk, q0, q1);
  my_dff8 my_dff8_inst3(clk, q1, q2);

  multiplexer mul(sel, d, q0, q1, q2, q);

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
