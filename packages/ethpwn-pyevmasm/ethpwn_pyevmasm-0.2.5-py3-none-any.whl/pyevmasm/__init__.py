import functools

from .evmasm import instruction_tables, Instruction  # noqa: F401
from .evmasm import block_to_fork, DEFAULT_FORK
from .evmasm import assemble, assemble_all, assemble_hex, assemble_one

from .evmasm import disassemble_all as __disassemble_all_uncached
from .evmasm import disassemble_one as __disassemble_one_uncached
from .evmasm import disassemble_hex as __disassemble_hex_uncached
from .evmasm import disassemble as __disassemble_uncached

@functools.lru_cache(maxsize=64, typed=True)
def disassemble_all(bytecode, pc=0, fork='paris'):
    return list(__disassemble_all_uncached(bytecode, pc, fork))

@functools.lru_cache(maxsize=64, typed=True)
def disassemble_one(bytecode, pc=0, fork='paris'):
    return __disassemble_one_uncached(bytecode, pc, fork)

@functools.lru_cache(maxsize=64, typed=True)
def disassemble_hex(bytecode, pc=0, fork='paris'):
    return __disassemble_hex_uncached(bytecode, pc, fork)

@functools.lru_cache(maxsize=64, typed=True)
def disassemble(bytecode, pc=0, fork='paris'):
    return __disassemble_uncached(bytecode, pc, fork)