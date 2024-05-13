`timescale 1ns/1ns

module RMEM(
	input [31:0]WData,
	input [31:0]WDir,

	input Sel,
	
	output reg[31:0]Out

);

reg [31:0]MEM[63:0];

initial	begin
	$readmemb("Memory/MEM1.txt", MEM);
end

always @(*) begin
	if(Sel)
		MEM[WDir]=WData;
	else
		Out=MEM[WDir];
end
	
endmodule


