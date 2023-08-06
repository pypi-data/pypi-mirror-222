// A very basic implementation of a stdio.h but in assembly.
// should(tm) work with riscemu.
//
// Copyright (c) 2023 Anton Lydike
// SPDX-License-Identifier: MIT

.data

// putchar buffer
_putc_buff:
.space          512
_putc_idx:
.byte           0x00

.text

.globl  putchar
.globl  flush

// putchar(int character)
// writes character to stdout
putchar:
        la      t0
