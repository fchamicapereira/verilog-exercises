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

  wire zero, ground, cin_add_msb;
  assign zero = 1'b0;

  add16 add_lsb(a[15:0], b[15:0], zero, sum[15:0], cin_add_msb);
  add16 add_msb(a[31:16], b[31:16], cin_add_msb, sum[31:16], ground);

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
