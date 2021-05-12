.global main
main:
_start:
	! set the default cacheable bit in the AJIT mmu so that
	! the ^%%#& cache is exercised.  The mmu stays disabled.
	set 0x100, %o0
        sta %o0, [%g0] 0x4      

	! Initialize PSR, enable traps.
	! set PSR with ET=1 PS=1 S=1, all other fields=0
	mov 0xE0, %l0	
	wr %l0, %psr
	nop	! insert nops here because
	nop	! writes to psr may be delayed 
	nop	
	
	
	!store base of trap table in TBR register
	set	trap_table_base, %l0
	wr	%l0, 0x0, %tbr
	nop	! insert nops here because
	nop	! writes to tbr may be delayed
	nop
	
	!Initialize g1. Upon a trap, g1 should be 
	!overwritten by the trap number
	mov 0xBAD, %g1
