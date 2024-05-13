module INS_MEM(
    input [31:0] Dir,

    output reg [31:0] Out
);

reg [7:0] MEM [0:255];

initial begin
    $readmemb("Memory/INS1.txt",MEM);
end

always @(*) begin
    Out = {
        MEM[Dir],
        MEM[Dir+1],
        MEM[Dir+2],
        MEM[Dir+3]
    };
end
endmodule
