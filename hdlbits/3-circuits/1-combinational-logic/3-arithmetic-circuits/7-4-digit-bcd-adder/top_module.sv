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

module bcd_fadd (
    input [3:0] a,
    input [3:0] b,
    input     cin,
    output   cout,
    output [3:0] sum
  );

  wire [4:0] c;
  assign c[0] = cin;
  assign cout = c[4];

  add1 add1_0 (a[0],  b[0],  c[0],  sum[0],  c[1]);
  add1 add1_1 (a[1],  b[1],  c[1],  sum[1],  c[2]);
  add1 add1_2 (a[2],  b[2],  c[2],  sum[2],  c[3]);
  add1 add1_3 (a[3],  b[3],  c[3],  sum[3],  c[4]);
endmodule

module top_module (
    input [15:0] a, b,
    input cin,
    output cout,
    output [15:0] sum
  );

  wire [2:0] carry;
  bcd_fadd bcd_fadd0(a[3:0], b[3:0], cin, carry[0], sum[3:0]);
  bcd_fadd bcd_fadd1(a[7:4], b[7:4], carry[0], carry[1], sum[7:4]);
  bcd_fadd bcd_fadd2(a[11:8], b[11:8], carry[1], carry[2], sum[11:8]);
  bcd_fadd bcd_fadd3(a[15:12], b[15:12], carry[2], cout, sum[15:12]);

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
