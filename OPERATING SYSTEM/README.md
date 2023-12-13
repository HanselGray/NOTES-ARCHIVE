# CHAPTER 2 - PROCESS MANAGEMENT

### 1. PROCESS

1. Notion of process:

- A program is a piece of executable machine language that is stored on the disk. 

- Process is a running instance of a programm.

- Processes state:

| Name |  Description |
| ---- | ---- |
| New | In this step, the process is about to be created but not yet created. <br>It is the program that is present in secondary memory that will be picked up by OS to create the process.|
| Ready | New -> Ready to run. The process is loaded into the main memory and <br>  waiting to get the CPU time for its execution|
| Running | The process is chosen from the ready queue by the CPU for execution and the instructions within the process are executed by any one of the available CPU cores. |
| Blocked | Whenever the process requests access to I/O or needs input from the user or needs access to a critical region(the lock for which is already acquired) it enters the blocked or waits for the state.|
| Ready suspend | Process that was initially in the ready state but was swapped out of main memory and placed onto external storage by the scheduler|
| Blocked suspend |  Similar to suspend ready but uses the process which was performing I/O operation and lack of main memory caused them to move to secondary memory. |
| Terminated | Process is killed as well as Process Control Block (PCB) is deleted. |

![States of processes and transition](seven_process_states.png)

- Process control block (PCB): an information structure allows identify **only 1 process**.

![Structure of a PCB](process_control_block.png)

> [!NOTE]
> | Single-threaded process | Multi-threaded process |
> | ---- | ---- |
> | A running process with only one thread | Have multiple threads that can run simultaneously |

2. Process scheduling:

- **Purpose**: Maximize CPU's usage time.

- Types of process queue:

| Name |  Description |
| ---- | ---- |
| Job-queue | Set of processes in the system |
| Ready-Queue | Set of processes exist in the memory, ready to run |
| Device queues | Set of processes waiting for an I/O device. <br>Queues for each device are different |

- Process cycle:

    - Process selected and running

            1. process issue an I / O request, and then be placed in an I / O queue
            2. process create a new sub-process and wait for its termination
            3. process removed forcibly from the CPU, as a result of an interrupt, and be put back in the ready queue 

    - In case (1&2) after the waiting event is finished:

            1. Process eventually switches from waiting →ready state
            2. Process is then put back to ready queue
    
    - Process continues this cycle (ready, running, waiting) until it terminates.

            1. It’s removed from all queues
            2. Its PCB and resources deallocated

- Job Scheduler:

    - Select processes from program queue stored in disk and put into memory to execute
    - Not frequently (seconds/minutes) 
    - Control the degree of the multi-programming (number of process in memory) 
    - When the degree of multi-programming is stable, the scheduler may need to be invoked when a process leaves the system
> [!WARNING]
> Job selection’s problem: The job scheduler should select a mix of both types of process ( heavy CPU / IO bound ) to ensure optimal performance.

- CPU Scheduler:

    - Selects from processes that are ready to execute, and allocates the CPU to 1 of them.
    - Frequently work (example: at least 100ms/once).
    - the short-term scheduler must be fast (e.g.: ***10ms to decide ⇒10/(110)=9% CPU time is wasted***)

- Context switch: act of switching CPU from 1 process to another. (Medium-term scheduler)

3. Operation on process:

- Process may create several new processes
    - The creating process: parent-process
    - The new process: child-process
- Child-process may create new process ⇒ Tree of process

![Tree of processes](a_tree_of_processes.png)

- Resource allocation in a process tree:
    - Child receives resource from
        - OS
        - parent-process (2 case like below block)
            
                - All of the resource 
                - a subset of the resources of the parent process (to prevent a process from creating too many children)
    - When a process creates a new process, two possibilities exist in terms of execution: 
        1. The parent continues to execute concurrently with its children
        2. The parent waits until some or all of its children have terminated 

- Child process termination: 
    - Finishes executing its final statement and asks the OS to delete (exit) 
        - Return data to parent process
        - Allocated resources are returned to the system
    - Parent process may terminate the execution of child process
        - Parent must know child process’s id <br>⇒ child process has to send its id to parent process when created
        - Use the system call (abort)
    - Parent process terminate child process when

            1. The child has exceeded its usage of some of the resources 
            2. The task assigned to the child is no longer required 
            3. The parent is exiting, and the OS does not allow a child to continue 
            4. Cascading termination.

4. Process cooperation:

- Process relation: 

        1. Independence: Not affect or affected by other running process in the system
        2. Cooperation: affect or affected by other running process in the system

- Reason why process wants to cooperate: 

        1. Share Information
        2. Speedup Computation
        3. Provide Modularity 
        4. Increase the convenience
- Process collaborate requires mechanism that allow process to:

        1. Communicate with each other
        2. Synchronize their actions

> [!TIP]
> For more information on this you can read page 43-45 of Chapter 2 <br> ( or just google producer - consumer problem)

5. Inter-process communication:

- Memory sharing model:
    - Process share a common memory area
    - Implementation codes are written explicitly by application programmer
    - Example: Producer-Consumer problem

- Message passing system:
    - Require two basic operations:
            
            1. Send (msg) msg has fixed or variable size
            2. Receive (msg)
    
    - If 2 processes P and Q want to communicate, they need to:

        Establish a communication link (physical/logical) between them
        **OR** Exchange messages via operations: send/receive

    1. Direct communication: 
        - Each process that wants to communicate must explicitly name the recipient or sender of the communication

        - Communication link’s properties:

                + A link is established automatically 
                + A link is associated with exactly 2 processes
                + Exactly 1 link exists between each pair of processes
                + Link can be 1 direction but often 2 directions 
        
        - Operations:

                1. Send (to a process)
                2. Receive (from a process)
    2. Indirect communication:

        - Messages are sent to and received from mailboxes, or ports    
        - Communication link’s properties:

                + Established only if both members of the pair have a shared mailbox
                + A link may be associated with more than 2 processes
                + Each pair of communicating processes may have many links
        
        - Opeations:

                1. Create a new mailbox
                2. Send (to mailbox)
                3. Receive (from mailbox)
                4. Delete mailbox

- Buffering:
    -  Messages exchanged by communicating processes reside in a temporary queue
    - A queue can be implemented in 3 ways:

        1. Zero capacity: 
            - maximum length 0 => the link cannot have any messages waiting in it
        
        2. Bounded capacity:
            - Queue has finite length n ⇒ store at most n messages
            - If the queue is not full, message is placed in the queue and the sender can continue execution without waiting
            - If the link is full, the sender must block until space is available in the queue 

        3. Unbound capacity:
            - The sender never blocks

- Sockets:
    - Socket is defined as an endpoint for communication, each process has 1 socket.
    - Structure:

            1. IP Address: Computer address in the network
            2. Port: identifies a specific process
    
    - Socket types:

                1. Stream Socket: Based on TCP/IP protocol → Reliable data transfer
                2. Datagram Socket: based on UDP/IP protocol → Unreliable data transfer


### 2. THREADS

1. What is a thread? 
    - Basic CPU using unit, consists of

            1. Thread ID
            2. Program Counter 
            3. Registers 
            4. Stack space
    
    - Sharing between threads in the same process

            1. Code segment
            2. Data segment (global objects) 
            3. Other OS’s resources (opening file…)

    - Thread can run same code segment with different context (Register set, program counter, stack)

    - **EACH** process has at least one thread

![Distinguishing between process and thread](process_and_thread.png)

2. Benefits of using threads:

    - Responsiveness: 
        - allow a program to continue running even if part of it is blocked or is performing a long operation. Example: A multi-threaded Web browser 

                • 1 thread interactives with user
                • 1 thread downloads data

    - Resource sharing:
        - threads share the memory and the resources of the process

                • Good for parallel algorithms (share data structures) 
                • Threads communicate via sharing memory
        - Allow application to have many threads act in the same address space
    
    - Economy
        - Create, switch, terminate threads is less expensive than process
    
    - Utilization of multiprocessor architectures
        - each thread may be running in parallel on a different processor.

![Benefits of multithreading](benefits_of_multithreading.png)

3. User and kernel level threads:

- User-level threads:

    - Thread management is done by application
    - Kernel does not know about thread existence
    - Process scheduled like a single unit
    - User threads are supported above the kernel and are implemented by a thread library
    - Library support creation, scheduling and management...

> [!IMPORTANT]
> **Advantage**: Fast to create and manage
>
> **Disadvantage**: if a thread perform blocking system call , the entire process will be 
blocked ⇒ Cannot make use of multi-thread.

- Kernel-level threads:
    - Kernel keeps information of process and threads
    - Threads management is performed by kernel
        - No thread management code inside application
    - Thread scheduling is done by kernel
    - OSs support kernel thread: Windows NT/2000/XP, Linux, OS/2,..


> [!IMPORTANT]
> **Advantage**: 
>
> 1 thread perform system call (e.g. I/O request), other threads are not affected
>
> In a multiprocessor environment, the kernel can schedule threads on different processors
>
> **Disadvantage**: Slow in thread creation and management

4. Multithreading model:

- Many-to-one model:

    - Maps many user-level threads to 1 kernel thread. 
    - Thread management is done in user space
    -  implemented on OSs that do not support kernel threads use the many-to-one model
    - Properties:

            1. Efficient
            2. the entire process will block if a thread makes a blocking system call
            3. multiple threads are unable to run in parallel on multi processors

- Many-to-one model:

    - Maps each user thread to a kernel thread
    - Allow another thread to run when a thread makes a blocking system call
    - Creating a user thread requires creating the corresponding kernel thread

            • the overhead of creating kernel threads can burden the 
            performance of an application
            ⇒ restrict the number of threads supported by the system

    - Implemented in Window NT/2000/XP

- Many-to-many model:

    - Multiplexes many user-level threads to a smaller or equal number of kernel threads
    - Number of kernel threads: specific to either a particular application or a particular machine
    - Combine advantages of previous models:

            • Developers can create as many user threads as necessary
            • kernel threads can run in parallel on a multiprocessor
            • when a thread performs a blocking system call, the kernel can schedule another thread for execution

    - Supported in: UNIX

- Two-level model: 
    - A variation of many to many
    - Allow favor process with higher priority

>[!WARNING]
> Threading problem: The result of parallel running threads depends on the order of accessing the sharing variable
