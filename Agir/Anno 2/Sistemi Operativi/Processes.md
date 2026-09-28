How to provide the illusion of many CPUs?
# CPU virtualizing
The OS can promote the illusion that many virtual CPUs exist.
Time sharing: Running one process, then stopping it and running another
- The potential cost is performance. (Context switch)

A process is a running program.
Comprising of a process:
- Memory (address space)
	Instructions
	Data section
- Registers
	Program counter
	Stack pointer

# Process
## Process Creation
1. Load a program code into memory, into the address space of the process.
- Programs initially reside on disk as executables.
- OS perform the loading process lazily.
	Loading pieces of code or data only as they are needed during program execution.
2. The program’s run-time stack is allocated.
- Use the stack for local variables, function parameters, and return address.
- Initialize the stack with arguments -> argc and the argv array of main() function
3. The program’s heap is created.
- Used for explicitly requested dynamically allocated data.
- Program request such space by calling malloc() and free it by calling free().
4. The OS do some other initialization tasks.
- Input/output (I/O) setup
	Each process by default has three open file descriptors.
	Standard input, output and error
5. Start the program running at the entry point, namely main().
- The OS transfers control of the CPU to the newly-created process.

## Process States
A process can be one of three states.
 - Running
	A process is running on a processor.
- Ready
	A process is ready to run but for some reason the OS has chosen not to run it at this given moment.
- Blocked
	A process has performed some kind of operation.
	When a process initiates an I/O request to a disk, it becomes blocked and thus some other process can use the processor.