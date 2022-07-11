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
    input sub,
    output [31:0] sum
  );

  wire cout, ignore;
  wire [31:0] _b;

  assign _b = b ^ {32{sub}};

  add16 add16_lsb(a[15:0], _b[15:0], sub, sum[15:0], cout);
  add16 add16_msb(a[31:16], _b[31:16], cout, sum[31:16], ignore);

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
