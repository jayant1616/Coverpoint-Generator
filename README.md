## **Coverpoints for add and mul instructions with N instructions between**

*Assumptions:* 

 - There are no hazards between add and the N instructions between and N instructions and mul instruction.
 - There are no data hazards between the N instructions.
 - As there are no hazards between N instructions and the first and last instructions, All the N instructions are assumed to be *Non updating*   .
 - The instructions are not taken as inputs. Only the number of instructions considered.
 
 *Inputs for program:*
 
 - N : The number of instructions in between add and mul.


**Manual Solution for one of the coverpoint:** 
 - Consider the coverpoint : 
 [add : ? : ? : mul ] :: [a=rd : ? : ? : ?] :: [? : rs1 != a and rs2 != a : rs1 != a and rs2 != a : rs1==a or rs2==a]
 There's a RAW data hazard in the coverpoint :
 
 - Solution : Assuming the solution for RISC-V architecture with forwarding available in the pipeline, 
	 
	 - Forwarding Condition :
	 - (EX/MEM.RegWrite || MEM/WB.RegWrite ) && (EX/MEM.RegisterRd ≠ 0 || – MEM/WB.RegisterRd ≠ 0)

	

	 - Control Signals : 
			 
       - if (EX/MEM.RegWrite and (EX/MEM.RegisterRd ≠ 0) and (EX/MEM.RegisterRd = ID/EX.RegisterRs)) ForwardA = 01
       - if (EX/MEM.RegWrite and (EX/MEM.RegisterRd ≠ 0)and (EX/MEM.RegisterRd = ID/EX.RegisterRt)) ForwardB = 01 
       - if (MEM/WB.RegWrite and (MEM/WB.RegisterRd ≠ 0) and (MEM/WB.RegisterRd = ID/EX.RegisterRs)) ForwardA = 10 
       - if (MEM/WB.RegWrite and (MEM/WB.RegisterRd ≠ 0) and (MEM/WB.RegisterRd = ID/EX.RegisterRt)) ForwardB = 10

 

 
