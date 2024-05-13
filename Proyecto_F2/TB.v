//TestBench Para probar modulos
`timescale 1ns/1ns

module TB();

reg [31:0] in;
wire [31:0] out;

Inst_Mem IM1(
    .add(in),
    .instruccion(out)
);

initial begin
    in = 32'd0;
    #100;

    in = 32'd4;
    #100;
end

endmodule
