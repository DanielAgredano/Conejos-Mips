`timescale  1ns/1ns
module Todo_TB( );

reg [31:0]instruccionTR;

wire once;

Todo t1(
	.Tr_zf(once),
	.instruccionTR(instruccionTR)
);


initial
	begin
	instruccionTR=32'b000000_00001_00010_00000_00000_100000;
	#100;
	
	instruccionTR=32'b000000_00100_00101_00011_00000_100010;
	#100;
	
	instruccionTR=32'b000000_00111_01000_00110_00000_101010 ;
	#100;
	
	instruccionTR=32'b000000_01010_01011_01001_00000_100100;
	#100;
	
	instruccionTR=32'b000000_01101_01110_01100_00000_100101 ;
	#100;
	$stop;
	end
	
endmodule