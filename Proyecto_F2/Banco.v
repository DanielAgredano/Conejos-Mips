module REG_BANK(
	input [4:0]RDir1,
	input [4:0]RDir2,
	input [31:0]WData,
	input [4:0]WDir,

	input RW,
	
	output reg [31:0]ROut1,
	output reg [31:0]ROut2

);

reg [31:0] MEM [0:31];

assign ROut1 = MEM[RDir1];
assign ROut2 = MEM[RDir2];

initial begin
    $readmemb("Memory/BR1.txt",MEM);
end

always @(*) begin
    if(RW)
    MEM[WDir]=WData;
end

	
endmodule
		