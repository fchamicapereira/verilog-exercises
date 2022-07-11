module add16(
    input [15:0] a,
    input [15:0] b,
    input cin,
    output [15:0] sum,
    output cout
  );
  wire [16:0] c;	// carry bits

  assign c[0] = cin;	// carry input
  assign cout = c[16];	// carry output

  // assignment of 16-bit vectors
  assign sum[15:0] = (a[15:0] ^ b[15:0]) ^ c[15:0];
  assign c[16:1] = (a[15:0] & b[15:0]) | (a[15:0] ^ b[15:0]) & c[15:0];
endmodule

module top_module(
    input [31:0] a,
    input [31:0] b,
    output [31:0] sum
  );

  wire ignore, cout;
  wire [15:0] add16_msb_0_sum;
  wire [15:0] add16_msb_1_sum;

  add16 add16_lsb(a[15:0], b[15:0], 1'b0, sum[15:0], cout);

  add16 add16_msb_0(a[31:16], b[31:16], 1'b0, add16_msb_0_sum, ignore);
  add16 add16_msb_1(a[31:16], b[31:16], 1'b1, add16_msb_1_sum, ignore);

  assign sum[31:16] = (add16_msb_0_sum & {16{~cout}}) | (add16_msb_1_sum & {16{cout}});

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
