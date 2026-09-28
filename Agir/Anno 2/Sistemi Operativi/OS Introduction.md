# Operating system
Responsible for:
- Making it easy to run **programs**
- Allowing programs to **share** memory
- Enabling programs to **interact** with devices
The OS is in charge of making sure the system operates *correctly* and *efficiently*

The OS takes a **physical resource** and transforms it into a **virtual form** of itself.


System call allows the user to **tell the OS what to do**.
- The OS provides some interface (APIs, standard library)
- A typical OS exports a few hundred system calls:
	- Run programs
	- Access memory
	- Access devices
System calls allows the user to talk to the kernel.

The OS manages resources such as CPU, memory and disk.
The OS allows:
- Many programs to run | Sharing the CPU
- Many programs to *concurrently* access their own instructions and data | Sharing memory
- Many programs to access data | Sharing disk

## Virtualization

## Virtualizing the CPU
The system has a very large number of virtual CPUs
- Turning a single CPU into a seemingly infinite number of CPUs
- Allowing many programs to seemingly run at once

### Virtualizing Memory
The physical memory is an array of bytes
A program keeps all of its data structures in memory.
- Read memory (load):
	Specify an address to be able to access the data
- Write memory (store):
	Specify the data to be written to the given address

Each process accesses its own private virtual address space.
- The OS maps address space onto the physical memory.
- A memory reference within one running program does not affect the address space of other processes.
- Physical memory is a shared resource, managed by the OS.



The OS is juggling many things at once, first running one process, then another, and so forth.
Modern multi-threaded programs also exhibit the concurrency problem.

If you write a program with multiple threads, it's not guaranteed they'll sync properly if the instructions are not executed atomically
E.g. Increment a shared counter  take three instructions.
	1. Load the value of the counter from memory into register.
	2. Increment it
	3. Store it back into memory
These three instructions do not execute atomically. Problem of concurrency happen.

Devices such as DRAM store values in a volatile.
Hardware and software are needed to store data persistently.
- Hardware: I/O device such as a hard drive, solid-state drives(SSDs)
- Software:
	- File system manages the disk.
	- File system is responsible for storing any files the user creates.

The OS has some key data structures to track relevant pieces of information
- Process list
	- Ready processes
	- Blocked processes
	- Current running process
- Register context

PCB (Process control Block): A C-structure that contains information about each process