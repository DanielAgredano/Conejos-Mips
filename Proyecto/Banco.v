module Bancoreg(
	input [4:0]ra1,
	input [4:0]ra2,
	input [31:0]di,
	input [4:0]dir,
	input reg_write,
	
	output reg [31:0]dr1,
	output reg [31:0]dr2

);


reg [31:0] banco [0:31];

assign dr1 = banco[ra1];
assign dr2 = banco[ra2];

initial begin
    $readmemh("memoria.txt",banco);
end

always @(*) begin
    if(reg_write)
    banco[dir]=di;
end

	
endmodule
		