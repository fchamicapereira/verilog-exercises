# Verilog exercies

Verilog exercises based on [hdlbits.01xz.net/](hdlbits.01xz.net/).

## Verilog simulators

## Icarus

Run the tests:

```
$ make
```

Visualize the wave signal:

```
$ gtkwave top_module.vcd
```

## ModelSim

Run the tests:

```
$ make SIM=modelsim
```

Visualize the wave signal

```
$ make SIM=modelsim GUI=1
```