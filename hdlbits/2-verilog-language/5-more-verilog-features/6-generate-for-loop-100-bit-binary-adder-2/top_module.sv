module full_adder (
    input a,
    input b,
    input cin,
    output sum,
    output cout
  );

  assign sum = a ^ b ^ cin;
  assign cout = (a & b) | (a & cin) | (b & cin);
endmodule

module top_module(
    input [99:0] a, b,
    input cin,
    output [99:0] cout,
    output [99:0] sum
  );
  wire [100:0] carries;

  assign carries[0] = cin;
  assign cout = carries[100:1];

  genvar i;
  generate
    for(i = 0; i < 100; i++)
    begin : generate_full_adders
      full_adder fa(a[i], b[i], carries[i], sum[i], carries[i+1]);
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
