module add1 (
    input a,
    input b,
    input cin,
    output sum,
    output cout
  );
  assign sum = a ^ b ^ cin;
  assign cout = (a & b) | (a & cin) | (b & cin);
endmodule

module add16(
    input [15:0] a,
    input [15:0] b,
    input cin,
    output [15:0] sum,
    output cout
  );
  wire [15:0] c;	// carry bits

  assign c[0] = cin;	// carry input

  add1 add1_0 (a[0],  b[0],  c[0],  sum[0],  c[1]);
  add1 add1_1 (a[1],  b[1],  c[1],  sum[1],  c[2]);
  add1 add1_2 (a[2],  b[2],  c[2],  sum[2],  c[3]);
  add1 add1_3 (a[3],  b[3],  c[3],  sum[3],  c[4]);
  add1 add1_4 (a[4],  b[4],  c[4],  sum[4],  c[5]);
  add1 add1_5 (a[5],  b[5],  c[5],  sum[5],  c[6]);
  add1 add1_6 (a[6],  b[6],  c[6],  sum[6],  c[7]);
  add1 add1_7 (a[7],  b[7],  c[7],  sum[7],  c[8]);
  add1 add1_8 (a[8],  b[8],  c[8],  sum[8],  c[9]);
  add1 add1_9 (a[9],  b[9],  c[9],  sum[9],  c[10]);
  add1 add1_10(a[10], b[10], c[10], sum[10], c[11]);
  add1 add1_11(a[11], b[11], c[11], sum[11], c[12]);
  add1 add1_12(a[12], b[12], c[12], sum[12], c[13]);
  add1 add1_13(a[13], b[13], c[13], sum[13], c[14]);
  add1 add1_14(a[14], b[14], c[14], sum[14], c[15]);
  add1 add1_15(a[15], b[15], c[15], sum[15], cout);
endmodule

module top_module(
    input [31:0] a,
    input [31:0] b,
    output [31:0] sum
  );

  wire zero, ignore, add16_msb_cin;
  assign zero = 1'b0;

  add16 add16_lsb(a[15:0], b[15:0], zero, sum[15:0], add16_msb_cin);
  add16 add16_msb(a[31:16], b[31:16], add16_msb_cin, sum[31:16], ignore);

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
