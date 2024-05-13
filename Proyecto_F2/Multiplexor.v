module MUX(
    input [31:0]A,
    input [31:0]B,

    input Sel,

    output reg [31:0]Out
);

always @(*) begin
    if (Sel == 0)
        Out = A;
    else
        Out = B;
end

endmodule

module MUX_5(
    input [4:0]A,
    input [4:0]B,

    input Sel,
    
    output reg [4:0]Out
);

always @(*) begin
    if (Sel == 0)
        Out = A;
    else
        Out = B;
end

endmodule