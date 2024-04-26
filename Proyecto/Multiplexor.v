module Multiplexor(
    input [31:0]a,
    input [31:0]b,
    input sel,
    output reg [31:0]salida
);

always @(*)
begin
    if (sel == 0)
        salida = a;
    else
        salida = b;
end

endmodule
