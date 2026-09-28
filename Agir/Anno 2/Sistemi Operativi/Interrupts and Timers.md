The OS needs to chare the physical CPU by **time sharing**

Issue
- Performance: How can  we implement virtualization without adding excessive overhead to the system?
- Control: How can we run processes efficiently while retaining control over the CPU?

# Direct Execution
Just run the program directly on the CPU

| OS                                | Program                        |
| --------------------------------- | ------------------------------ |
| Create entry for process list     |                                |
| Allocate memory for program       |                                |
| Load program into memory          |                                |
| Set up stack with `argc` / `argv` |                                |
| Clear registers                   |                                |
| Execute call `main()`             |                                |
|                                   | Run `main()`                   |
|                                   | ...                            |
|                                   | Execute `return` from `main()` |
| Free memory of process            |                                |
| Remove from process list          |                                |
Without limits on running programs, the OS wouldn’t be in control of anything and thus would be “just a library"

What if a process wishes to perform some kind of restricted operation such as:
- Issuing an I/O request to a disk
- Gaining access to more system resources such as CPU or memory
Solution: Using protected control transfer
- User mode: Applications do not have full access to hardware resources.
- Kernel mode: The OS has access to the full resources of the machine

# System call
Allow the kernel to *carefully expose* certain **key pieces of functionality** to user program, such as:
- Accessing the file system
- Creating and destroying processes
- Communicating with other processes
- Allocating more memory

### Trap instruction
- Jump into the kernel
-  Raise the privilege level to kernel mode

### Return-from-trap instruction
- Return into the calling user program
- Reduce the privilege level back to user mode

| OS @ boot<br>(kernel mode) | Hardware                            |
| -------------------------- | ----------------------------------- |
| Initialize trap table      |                                     |
|                            | Remember address of syscall handler |

| OS @ boot<br>(kernel mode)        | Hardware                       | Program<br>(user mode) |
| --------------------------------- | ------------------------------ | ---------------------- |
| Create entry for process list     |                                |                        |
| Allocate memory for program       |                                |                        |
| Load program into memory          |                                |                        |
| Set up stack with `argc` / `argv` |                                |                        |
| Fill kernel stack with reg/PC     |                                |                        |
| **Return-from-trap**              |                                |                        |
|                                   | Restore regs from kernel stack |                        |
|                                   | Move to user mode              |                        |
|                                   | Jump to main                   |                        |
|                                   |                                | Run `main()`           |
|                                   |                                | ...                    |
|                                   |                                | Call system            |
|                                   |                                | **Trap** into OS       |
|                                   | Save regs to kernel stack      |                        |
|                                   | Move to kernel mode            |                        |
|                                   | Jump to trap handler           |                        |
| Handle trap                       |                                |                        |
| Do work of syscall                |                                |                        |
| **Return-from-trap**              |                                |                        |
|                                   | Restore regs from kernel stack |                        |
|                                   | Move to user mode              |                        |
|                                   | Jump to PC after trap          |                        |
|                                   |                                | ...                    |
|                                   |                                | Return from `main()`   |
|                                   |                                | **Trap** via `exit()`  |
| Free memory of process            |                                |                        |
| Remove from process list          |                                |                        |

# Switching between processes
How can the OS **regain control** of the CPU so that it can switch between processes?
- Cooperative Approach: **Wait** for syscalls
- Non-Cooperative Approach: The **OS** takes control

## Cooperative Approach
Processes periodically give up the CPU by making system calls such as `yield`.
- The OS decides to run some other task.
- Application also transfer control to the OS when they do something illegal.
	- Divide by zero
	- Try to access memory that it shouldn’t be able to access
E.G. Early versions of the Macintosh OS, The old Xerox Alto system

A program gets stuck in an infinite loop $\rightarrow$ Reboot the machine

## Non-Cooperative Approach
**Timer interrupt**

During the boot sequence, the OS starts the **timer**
The timer **raises an interrupt** every so many milliseconds
When the interrupt is raised:
1) The currently running process is halted.
2) Save enough of the state of the program.
3) A pre-configured interrupt handler in the OS runs.

A timer interrupt gives the OS the ability to run again on a CPU

The scheduler makes a decision:
- Whether to continue running the current process, or switch to a differentone.
- If the decision is made to switch, the OS executes context switch.
### Context Switch
A low-level piece of assembly code:
- Saves a few register values for the current process onto its kernel stack
	- General purpose registers
	- PC
	- Kernel stack pointer
- Restores a few for the soon-to-be-executing process from its kernel stack
- Switches to the kernel stack for the soon-to-be-executing process

| OS @ boot<br>(kernel mode)                                                                                                   | Hardware                        | Program<br>(user mode) |
| ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ---------------------- |
|                                                                                                                              |                                 | ...                    |
|                                                                                                                              |                                 | Process A              |
|                                                                                                                              | **Timer interrupt**             |                        |
|                                                                                                                              | Save regs(A) to k-stack(A)      |                        |
|                                                                                                                              | Move to kernel mode             |                        |
|                                                                                                                              | Jump to trap handler            |                        |
| Handle trap                                                                                                                  |                                 |                        |
| Call switch() routine<br>- Save regs(A) to proc-struct(A)<br>- Restore regs(B) from proc-struct(B)<br>- Switch to k-stack(B) |                                 |                        |
| **Return-from-trap** (into B)                                                                                                |                                 |                        |
|                                                                                                                              | Restore regs(B) from k-stack(B) |                        |
|                                                                                                                              | Move to user mode               |                        |
|                                                                                                                              | Jump to B's PC                  |                        |
|                                                                                                                              |                                 | Process B              |
|                                                                                                                              |                                 | ...                    |
#### Worried About Concurrency?
What happens if, during interrupt or trap handling, **another** interrupt occurs?
The **OS** handles these situations in one of two ways:
- Disable interrupts during interrupt processing.
- Use a number of sophisticate locking schemes to protect concurrent access to internal data structures.