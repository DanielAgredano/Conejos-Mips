`timescale 1ns/1ns

module Memoria(
	input [31:0]dato,
	input [31:0]direccion,
	input sel,
	
	output reg[31:0]salida

);

reg [31:0]registro[0:63];

	initial	
		begin
			$readmemb("data.txt", registro);
		end

	always @*
	begin
	
		if(sel)
		begin
		registro[direccion]=dato;
		end
		
		else
		begin 
		salida=registro[direccion];
		end
		
	end
	
endmodule


