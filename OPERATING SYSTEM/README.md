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

### 3. CPU SCHEDULING

1. Basic concepts:

    - System only have 1 processor: only 1 process running at a time. <br>
    Process is executed until it must wait, typically for the completion of some I/O request

        - In a simple system: CPU is not utilized during this time -> wasted CPU time.       
        - Multiprogramming system: try to use this time productively, give CPU for another process

> [!NOTE]  
> Scheduling is a fundamental OS’s function
>
> Switching CPU between processes means utilizing the system more efficiently

- Typical process execution cycle:
    - Process execution consists of a cycle of CPU execution and I/O wait
    - Begins with a CPU burst
    - followed by an I/O burst
    - CPU burst → I/O burst → CPU burst → I/O burst → . . . 
    * End: the last CPU burst will end with a system request to terminate execution

- Process classification - Based on distribution of CPU & I/O burst

| Name | Attribute |
| ---- | ---- |
| CPU-bound processes | might have a few very long burst |
| I/O-bound processes | would typically have many very short CPU bursts |

2. CPU scheduler:

- CPU idle -> select 1 process from ready queue to run it <br>CPU scheduling decisions may take place when process switches from: 
    1. running -> waiting state (I/O request)
    2. running -> ready state (out of CPU usage time→ time interrupt)
    3. waiting -> ready state (e.g. completion of I/O)
    4. Or process terminates

> [!NOTE]  
> Case 1&4 ⇒ non-preemptive scheduling scheme
>
> Other cases ⇒ preemptive scheduling scheme

- Scheduling schemes:

| Non-preemptive scheduling | Preemptive scheduling |
| ----------------------- | ----------------------- | 
| Process keeps the CPU until it releases the CPU either by:  <br> 1. terminating <br> <br>2. switching to the waiting state <br><br> Non-preemptive scheduling **DOES NOT** require the special hardware (timer)  | Process only allowed to run in specified period. <br> At the end of the period time interrupt appear, dispatcher is invoked to decide which process goes next. <br> Protect CPU from “CPU hungry" processes. <br> Preemptive scheduling create a new problem: <br> 1. Process 1 updating data and the CPU is taken <br> 2. Process 2 executed and read data which is not completely update | 

  
3. Scheduling criteria:

- CPU utilization 

    - keep the CPU as busy as possible
    - should range from 40 percent (for a lightly loaded system) to 90 percent (for a heavily used system)
- Throughput
    - number of processes completed per time unit
    - Long process: 1 process/hour
    - Short processes: 10 processes/second
- Turnaround time
    - Interval from the time of submission of a process to the time of completion 
    - Can be the sum of: 
    
            1. periods spent waiting to get into memory
            2. waiting in the ready queue
            3. executing on the CPU
            4. doing I/O

- Waiting time
    - sum of the periods spent waiting in the ready queue

    - CPU-scheduling algorithm does not affect the amount of time during which a 
process executes or does I/O;<br> it affects only the amount of time that a process 
spends waiting in the ready queue

- Response time
    - time from the submission of a request until the first response is produced
    - process can produce some output fairly early
    - continue computing new results while previous results are being output to the user

4. Scheduling algorithms:

- First Come, First Served (FCFS):
    - Rule: process that requests the CPU first is allocated the CPU first<br> 
    Process owns CPU until it terminates or blocks for I/O request
    ![first come first serve](First-come-first-serve.png)
    - Pros and cons:
        - Simple, easy to implement
        - Short process must wait like long process

- Shortest job first (SJF):

    - Rule: associates with each process the length of the latter's next CPU burst
        - process that has the smallest next CPU burst
        - Two methods
            - Non-preemptive
            - preemptive (SRTF: Shortest Remaining Time First)

    - Pros:
        - SJF (SRTF) is optimal: Average waiting time is minimum
    - Cons:
        - It’s not possible to predict the length of next CPU burst
        - Predict based on previous one (impossible)

- Round robbin (RR):
    - Rule:
        - Each process is given a time quantum (time slice) τ to be executed
        - When time’s up processor is preemptive, and process is placed in the last position     of ready queue
        - If there are n process, longest waiting time is (n − 1)τ

- Multilevel queue scheduling:
    - Ready queue is divided into several separate queues
    - Processes are permanently assigned to 1 queue
    - Based on some properties of the process, such as memory size, priority, or type..
    - Each queue has its own scheduling algorithm

- Some consideration:
    - Commonly implemented as fixed-priority preemptive scheduling
        - Processes in lower priority queue only executed if higher priority queues are empty
    - High priority process preemptive CPU from lower priority process
    - Starvation is possible
    - Time slice between the queues
        - foreground process queue, 80% CPU time for RR 
        - background process queue, 20% CPU time for FCFS

![Multi-level-queue-example](Multi-level-queue.png)

- A solution to the fixed-priority preemptive scheduling:
    - Allows a process to move between queues
 
    - If a process uses too much CPU time ->moved to a lower priority queue
    - I/O-bound and interactive processes in the higher-priority queues
    - process that waited too long in a lower- priority queue may be moved to a higher-priority queue
    - Prevent “starvation”

- Queue’s scheduler is defined by the following parameters:
    - number of queues
    - scheduling algorithm for each queue 
    - method used to determine when to upgrade/demote a process to a higher/lower priority queue 
    - method used to determine which queue a process will enter when that process needs service

![Multi-level-queue](An-example-multi-level-scheduling-queue.png)

5. Multi-processor scheduling:

- 2 model
    - Symmetric multiprocessor
    - Asymmetric multiprocessor 
 

 - Assymetric multiprocessor problem:   
    - 1 processor execute the scheduling program
    - Only 1 processor can access process queue
    - May be bottleneck at 1 processor

- Symmetric multiprocessor:
    - Each processor runs its own Scheduler
    - Independently selects available proceses in the queue

- Queue management schemes in symmetric multiprocessor model:
    1. Each processor has its own ready queue:
        - Pros: Easy to organize
        - Cons: Exist idle processor with empty queue while other processor has to do a lot of computation

    2. Share ready queue (Global queue):
        -  Pros:
            - Efficient use of CPU
            - Fair to the Process
        - Cons:
            - The problem of sharing data structures (queues):
                - 1 TT is selected by 2 processors or 
                - 1 TT is lost on the queue

    3. Hybrid - combine the above schemes:
        - Use both local and global queue
        - Share loads from queues
        - Each CPU works with its own local queue

6. An example of priority-based in windows:

![Priority levels ](priority-level-windows.png)


### 4. Critical resources and process synchronization:

1. Critical resources:

- What is a critical resource?:
    - Resource that is limited of sharing capability
    - Required concurrently by processes
    - Can be either physical devices or sharing data

- Problem with critical resources:
sharing critical resource may not guarantee data completeness.

- Critical section:
    - The part of the program where the shared memory is accessed is called the critical region or critical section
    - When there are more than 1 process use critical resource then we must synchronize them a.k.a **ONLY ONE** process can stay inside the critical section at a time.

2. Conditions to ensure synchronization:

    1. Mutual Exclusion: Critical resource does not have to serve the number of process more than its capability at any time.
        
    2. Progressive: If critical resource still able to serve and there is any process want to be executed in critical section then this process can use critical resource

    3. Bounded Waiting: There exists a bound on the number of times that other processes are allowed to enter their critical sections after a process has made a request to enter its critical section and before that request is granted

3. Methods to tackle the critical resources problem:
    1. Variable lock:
        - Each process uses 1 byte in the sharing memory area as a lock
            - enters critical section, lock (byte lock = true) 
            - exits from critical section, unlock (byte lock= false)

        - Process want to enter critical section: check other process’s lock ‘s status
            - Locking ⇒ Wait
            - Not lock ⇒ Has the right to enter critical section

    - Pseudo code:
    ![Varlock demonstration](Variable-lock.png)

    > [!CAUTION]
    > This method does not properly synchronize processes
    > - Two processes request resource at the same time
    >
    >    1. Mutual exclusion problem (Case 1) 
    >    2. Progressive problem (Case 2)
    > - Reason: The following actions are done separately
    >
    > 1. Check the right to enter critical section
    > 2. Set the right to enter critical section

    2. Decker's algorithm:

    - Similar to variable lock, but also use a 'turn' variable to show process with priority.

    ![Decker's algo](decker's-algorithm.png)

    > !REMARK
    - Synchronize properly for all cases
    - No hardware support requirement -> implement in any languages
    - Complex when the number of processes and resources increase
    - “busy waiting” before enter critical section
    - When waiting, process must check the right to enter the critical section => Waste processor’s time

    3. Test and set:
    - Utilizing hardware support via uninterruptible instructions.
    - Pseudo codes for instructions:
        1. Test and change the content of a word

                boolean TestAndSet(VAR boolean target) {
                    boolean rv = target; 
                    target = true; 
                    return rv;
                }    
        
        2. Swap the content of two different words

                void Swap(VAR boolean , VAR boolean b) { 
                    boolean temp = a; 
                    a = b; 
                    b = temp;
                }
                
    - Code block is uninterruptible when executing
    - When called at the same time, done in any order

    - Remark:
        - Simple, complexity is not increase when number of processes and critical resource increase
        - “busy waiting” before enter critical section => Waste processor’s time
        - No bounded waiting guarantee - The next process enters critical section is depend on the resource release time of current resource-using process

    4. Semaphore:

    > [!IMPORTANT]
    > I skip the intro about semaphore and went straight to it's actual implementation (the version with block() and wakeup() operations)

    -   An integer variable, initialized by resource sharing capability
        - Number of available resources (e.g. 3 printers)
        - Number of resource’s unit (10 empty slots in buffer)
        - Can only be changed by 2 operation P and V     
    - Overcome "busy waiting" problem by using block() and wakeup() operation.         
    - Semaphore pseudo code:

        typedef struct{
            int value
            struct process *Ptr

        }Semaphore

    - Operation's P pseudo code:
            
            wait(S){
                S.value--
                if(S.value<0){
                    Insert process to S.ptr
                    block()
                }
            }

    - Operation's V pseudo code:

            signal(S){
                S.value++
                if(S.value<=0){
                    Get process P from S.ptr
                    wakeup(P)
                }
            }
    
    - P and V are uninterruptible instructions

    - Remark:
        - Easy to apply for complex system
        - No busy waiting 
        - The effectiveness is depend on user


4. Deadlocks:

- A set of processes is deadlocked if each process in the set is waiting for an event that only another process in the set can cause

- 4 conditions for deadlocks:
    
    1. Critical resource:
        - Resource is used in a non-shareable model
        - Only one process can use resource at a time
        - Other process request to use resource ⇒ request must be postponed until resource is released

    2. Wait before entering critical section:
        - Process can not enter critical section has to wait in queue
        - Still own resources while waiting

    3. No resource reallocation system
        - Resource is non-preemptive
        - Resource is released only by currently using process after this process finished its task
    
    4. Circular waiting
        - Set of processes {P0, P2, . . . , Pn} waiting in a order: P0 → R1 → P1; P1→ R2 → P2; . . . Pn−1 → Rn →Pn; Pn → R0 → P0 creating a non-stop loop.

5. Methods for battling deadlock:



- Deadlock prevention:
    - Objective - Attack 1 of 4 required conditions for deadlock to appear:  

    1. Critical resource:
    - Reduce the system’s critical degree
        - Shareable resource(read-only ffile): accessed simultaneously
        - Non-shareable resource: Cannot be accessed simultaneously

    - SPOOL mechanism(Simultaneous peripheral operation on-line) 
        - Do not allocate resource when it’s not necessary
        - A limited number of processes can request resource

    2. Wait before entering critical section
  
        - Prior allocate
            - processes request all their resources before starting execution and only run when required resources are allocated
            -  Effectiveness of resource utilization is low

        - Resource release
            - Process releases all resource before apply(re-apply) new resource
            - Process execution’s speed is low
            - Must guarantee that data kept in temporary release resource won’t be lost

    ![Example](deadlock-prevention-wait-before-critical.png)
    
    3. Non-preemptive resource
        - Allow process to preempt resource when it’s necessary

    4. Circular wait
        - Provide a global numbering of all type of resources
            - R = {R1, R2, . . . Rn}: Set of resources
        - Construct an ordering function f : R → N based on the order of resource utilization
            - f(Tape) = 1 
            - f(Disk) = 5 
            - f(Printer) = 12
        - Process can only request resource in an increasing order
        - holding resource type Rk can only request resource type Rj satisfy f(Rj)> f(Rk) 
        - Process requests resource Rk has to release all resource Ri satisfy condition f(Ri) ≥ f(Rk)

- Deadlock avoidance:

    - Verify all resource request
        - If the system is still safe after allocate resource ⇒ allocate
        - If not ⇒ process has to wait
    - Banker's algorithm:
        - Data structure:

        | Name | Function |
        | ---- | ---- |
        | Available | Vector with length m represents the number of available resource in the system. (Available[3] = 8 ) |
        | Max | Matrix n ∗m represents each process maximums request for each type of resource. (Max[2,3] = 5 ⇒?) |
        | Allocation | Matrix n ∗m represents each process maximums request for each type of resource. (Max[2,3] = 5 ⇒?) |
        | Need | Matrix n ∗m represents amount of resource is needed for each process <br>(Need[2,3] = 3 ⇒?)  Need[i][j] = Max[i][j] - Allocation[i][j] |
        | Work | vector with length m represents how much each resource still available |
        | Finish | vector with Boolean type, length m represents if a process is guaranteed to finish or not |

        - Pseudo code for banker's algorithm:

                BOOL Safe(Current Resource-Allocation State){ 

                    Work←Available 

                    for (i : 1 → n) Finish[i]←false                    
                    flag← true 

                    While(flag){ 

                        flag←false 

                        for (i : 1 → n)                         
                        if(Finish[i]=false AND Need[i] ≤Work){ 

                            Finish[i]← true 
                            Work ← Work+Allocation[i] 
                            flag← true

                        }//endif

                    }//endwhile 
                    
                    for (i : 1 → n) if (Finish[i]=false)return false;
                    return true;

                }//End function
        
    - Verify flow:

            1. if(Request[i]>Need[i]) => Error(Request higher than declared number)
            
            2. if(Request[i]>Available) => Block(Not enough resource, process has to wait)
            
            3. Set the new resource allocation for the system 
                - Available = Available - Request[i] 
                - Allocation[i] = Allocation[i] + Request[i] 
                - Need[i] = Need[i] - Request[i]
            
            4. Allocate resource based on the result of new system safety check 
            
            if(Safe(New Resource Allocation State)) 
                Allocate resource for Pi as requested
            else 
                Pi has to wait
                Recover former state (Available, Allocation,Need)

    - Example: Request[3,2] = 2: P3 requests 2 units of resource R2.

- Deadlock detection and recovery:
    - Instead of performing checking everytime a request for critical resource is performed,
    it'll check for deadlock periodically.

    - Reaction when detect deadlock:

        1. Terminate all processes 
        
        - Quick to eliminate deadlock
        
        - Too expensive
        
        - Killed processes may be almost finished
            
        2. Terminate processes consequently until deadlock is removed
           
        - After process is terminated, check if deadlock is still exist or not
            - Deadlock checking algorithm complexity is m ∗ n^2
        
        - Need to point out the order of process to be terminated
            - Process’s priority
            - Process’s turn around time, how long until process finish
            - Resources that process is holding, need to finish

        - Process termination’s problem 
            - Process is updating file ⇒ File is not complete 
            - Process is using printer ⇒ Reset printer’s status
        
        3. Resource preemption
        - Need to consider:       
            1. Victim’s selection 
                - Which resource and which process is selected? 
                - Preemptation ‘s order for smallest cost
                - Amount of holding resource, usage time. . .

            2. Rollback 
                - Rollback to a safe state before and restart
                - Require to store state of running process
            
            3. Starvation
                - One process is preempted many times ⇒ infinite waiting 
                - Solution: record the number of times that process is preempted



- Deadlock ignore:
    - Method implemented by modern operating systems.

> [!NOTE]
> TLDR: **IF I DON'T SEE ANY DEADLOCKS THAT MEANS THERE'S NO DEADLOCKS RIGHT?**
    
![True potential lies within ignorance](Deadlock-ignore.png)



