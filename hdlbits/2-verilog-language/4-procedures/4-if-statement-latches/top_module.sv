module top_module(
    input      cpu_overheated,
    output reg shut_off_computer,
    input      arrived,
    input      gas_tank_empty,
    output reg keep_driving
  );

  always @(*)
  begin
    shut_off_computer = cpu_overheated;
  end

  always @(*)
  begin
    if (~arrived)
      keep_driving = ~gas_tank_empty;
    else
      keep_driving = 0;
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
