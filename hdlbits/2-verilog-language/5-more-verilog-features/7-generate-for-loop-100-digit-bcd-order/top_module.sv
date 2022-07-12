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

module top_module(
    input [399:0] a, b,
    input cin,
    output cout,
    output [399:0] sum
  );
  wire [100:0] carries;

  assign carries[0] = cin;
  assign cout = carries[100];

  genvar i;
  generate
    for(i = 0; i < 100; i++)
    begin : generate_bcd_fadders
      bcd_fadd bcd_fadd_inst(a[i*4+3:i*4], b[i*4+3:i*4], carries[i], carries[i+1], sum[i*4+3:i*4]);
    end
  endgenerate

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
