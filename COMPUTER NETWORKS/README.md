

# CHAPTER 1 - INTRODUCTION

* Introduction to the course
* History of the Internet
* Concept of Computer Networks
* Architecture
* Topology
* Protocol
* Circuit switching vs. packet switching.
	* Pros and cons

# CHAPTER 2 - CONCEPTS OF COMPUTERS COMMUNICATIONS

+ Layering architecture on the Internet (OSI - TCP/IP model)
+ Identification on the Internet (MAC, IP, ports)
+ ARP (Address resolution protocol): use to convert IP address -> MAC address. 


# CHAPTER 3 - PHYSICAL LAYER

### 1. CABLES: 
- UTP: cheap, widely used, have weak resistance to noise, short transmission distance (100m - before the need of amplification/repeat)

- Coaxial: used in TV signal transmission or telephone networks; 
	 is being replaced by fiber-optics cable, can be used to link computers of short distance, transmission distance varied (RG11: ~1100m , RG58: ~185m)

- Fiber optics: used for long-range transmission; communication in metropolitan networks; connecting routers of ISP; or in backbone part of a LAN.
> [!NOTE]
> Fiber optic cables have **HUGE ADVANTAGES** over other type of cables: large data rate, small and light, better isolation from electromagnetic environment, much further range of transmission before needing amp/repeat.

> [!WARNING]
> It's FORKIN EXPENSIVE $$$

![Optical fiber cable](Optical-fiber%20cable.png)

### 2. WIRELESS MEDIA:

- Data transmission on different frequency band of electromagnetic waves
- Broadcast, half-duplex: only send or receive at a time
- Easily affected by environment: reflections, noise/inteference or scattering

### 3. DATA ENCODING: (how data/a bit is encoded over a medium)

- Forms of encoding : digital/analog <----> digital/analog - total of 4 types
- Line encoding consideration: 
	 + Clock recovery on receiver side: If the clock recovery is not ideal, then the signal to be decoded will not be sampled at
	      the optimal times. This will increase the probability of error in received data.
	 + DC-component: Encoding should avoid DC-component by having signal mean altitude to be around 0.

1. NRZ (Non return to zero):

   - NRZ-L: a bit 0/1 is determined by signal level

   - NRZ-I: a bit 0/1 is determined by signal level change

   - **NRZ properties**: simple, but does not contain element supporting clock sync -> only use in encoding on magnetic storage

2. Bipolar AMI:

  - Properties: use more than 2 signal level for the 1-bit.

  - Variations: Alternate mark inversion | Pseudoternary
        + Alternate mark inversion: 0 = no signal ; 1 = presence of signal, 
          with 2 consecutive 1s having different signal level.
        + Pseudoternary: The opposite of alternate mark inversion

   - ****Remark***: DC component = 0
            Good sync when there's many bit in the non-zero level
            Not optimal for using in transmission line because the receiver needs to 
            distinguish 3 different levels of signal.

3. Biphase / Manchester:
	
     - Properties: Always change signal level in the middle of bit time.

     - Variations: Manchester | Differential Manchester
       + Manchester: signal level change at middle of bit time determine the bit
       + Diff Manchester: signal level change at a bit interval determine the bit value.
        
	![Line encode summary](/COMPUTER%20NETWORKS/LineEncodeSummary.png)
	 	      				
4. Encoding digital data to analog signal:

   - Amplitude shift keying: 
            Use 2 different amplitude for 0s/1s, one level is typically 0.
            Easily impact by noise.
            Hard to sync signals.
            Used in optical cable.

   - On-off keying: During a bit interval : 0 = no light; 1 = light and vice-versa.

   - Frequency shift keying: Use 2 different frequencies to encode 0/1. 
               Low error rate.
               Use to transfer data in telephone lines.
                    

   - Phase shift keying: Use different phase to encode data.
   	                 Can be used to encode multiple bits at once.
     			Can be combined with ASK.
     
![Digital to analog](/COMPUTER%20NETWORKS/Digital-AnalogEncodeSummary.png)

5. Encoding analog data to digital signal:
        
    **Shannon sampling theorem**: The sampling rate is be equal to or greater than twice the highest frequency of the signal, 
                    then the original signal can be considered intact.
    Example: maximum freq of human voice is 4300hz -> minimum sampling freq should be 8600hz.

   - Pulse Code Modulation:
     
![Baud rate](/COMPUTER%20NETWORKS/LineEncodingRateSummary.png)
	
- Delta modulation: Use a stair case function; if the approx falls below the signal -> 1 otherwise 0; the approximation level then is increase if it's a 1/ decrease otherwise.
     	-  The staircase function has a delta (step-size) and a frequency. 
        -  Slow-change signal/ small delta: quantization error / granular noise. 
        -  Fast-change signal/ large delta: Slope Over load distortion.

6. Analog data to analog signals:
        - Combine the data signal with a carrier into a single signal.
        - 3 different methods:  
        
                1. Amplitude modulation.
                2. Frequency modulation.
                3. Phase modulation.


# CHAPTER 4 - DATALINK LAYER


### 1. LAYER PACKET: frame

### 2. LAYER DEVICES: hub, switch

- Function: Framing, addressing, flow/error control, media access control.
- The link layer is implemented inside a Network Interface Card (NIC)
- Identifier: MAC address - 48-bit address, organized by IEEE (Insitute of Electrical and Electronics Engineers). MAC address is unchanged when changing networks(?)

### 3. Error detection:
- Objective: ensure the data is transmitted correctly even under unreliable conditions
 Parity bit:	
	
	- Single bit parity: a bit at the end of a row, set to either 0 or 1 to ensure that the number of 1s is even.

	- Two-dimensional parity: a bit at the end of rows and collumns, set to either 0 or 1 to ensure that the number of 1s in that row/collumn is even.  

### 2. Checksums: 
 1. Basic checksum:

 2. CRC:
 ![CRC_1](CRC_1.png)
 ![CRC_2](CRC_2.png)
- After calculation, the CRC code would be append to the end of the frame and send.
- Checking for errors using CRC:
![CRC_check](CRC_check.png)
- if there is no remainder -> no errors.

### 3. Stop-and-wait ARQ(Automatically repeated requests):
- Stop and wait: Each packet sent would be reply with an ACK packet, only proceed to send the next packet if the previous packet is ACKed, otherwise continue to resend.
	
 Possible errors: Lost ACK 	
 => Solution: Sender automatically resend after timeout (timeout >=1 RTT); 
 Receiver automatically discard packet if it's a duplicate.	  

### 4. Flow control:
- **Objective**: Make sure the sender doesn't overload the reciever, because when the reciever buffer frame is full, all arriving frame after that point would be dropped.

	- **Stop-and-wait**: like the above stop-and-wait ARQ, just without the ARQ part.

	- **Sliding window**: Sender send more than one frame at a time; transmitted frame without ACK will be stored in buffer.
	
	- **Piggy backing**: 
	
		- A and B transmit data from both sides. When B needs to send ACK while still need to send data, B can attach the ACK to the data frame and send it altogether. 	
		
		- Otherwise, send the ACK separately. After an ACK is send, if B send another data frame, the ACK previously send would still be attached to the frame (avoiding ACK lost).

Exercises: page 45-51

Media access control (MAC):

# CHAPTER 5 - LAN
### 1. Devices and Data Forwarding:
| Devices    | What does it do? |
| ----------- | :----------- |
| Hub     | Only broadcast signal.     |
| Switch   | Store and forward a data frame <br/>according to MAC address.        |
| Bridge | Dividing a network<br/>into multiple network segments. |

> [!CAUTION]
> Routers (later).
	

### 2. Switch:
- Link-layer device, store and selectively forward frame to one-or-more outgoing links.  
- Transparent: hosts unaware of switches.
- Plug-and-play, self-learning: switches do not need to be configured.

- Switch self-learning mechanism:

			1. record incoming link, MAC address of sending host

			2. index switch table using MAC destination address

			3. if entry found for destination then {
					if dest on segment from which frame arrived then drop frame
				    else forward frame on interface indicated by entry in MAC table
			  }
			   else flood /* forward on all interfaces except arriving interface */
		 
> [!IMPORTANT]
LAN topology: Bus, Star, Ring, wireless LAN (WLAN).

![LAN_topologies](LAN-topology.png)

3. Logical link control (LLC) - IEEE 802.2: 
	+ Connect with protocols of Network layer: IPX, DCE, IP, ...
	+ Functions: Multiplexing / Demultiplexing.
	+ Flow control with 3 modes: 
		
				1. Unacknowledged connectionless 
				2. Acknowledged connectionless 
				3. Connection mode.
					 
		
	+ Frame structure: 
			
			1. DSAP and SSAP: Destination/Source Service Access Point (SAP); <br/> for multiplexing/demultiplexing of the upper layer.

			2. Control: define Protocol Data Unit (PDU) to transfer and control.
				a/ U-frame: send/recieve in connectionless mode (U: unnumbered)
				b/ I-frame: frame with information (I: Information), used in acknowledged mode
				c/ S-frame: for controlling (S: Supervisor)
		
	+ Practical LLC is often different from the above theoretical model.
 
> [!IMPORTANT]
> 1/ Error checking and flow control are used by some upper protocols (**NetBIOS**)
> 
> 2/ U-frame encapsulate PDU without numbering (unnumbered) and therefore **NO** flow control or error checking are provided.
> 
> 3/ Most upper protocols of LLC (TCP/IP) support error checking and flow control
	
> [!CAUTION]
> Due to the above reasons, LLC is only use in Unacknowledged connectionless mode with U-frames.

### 4. Ethernet LAN - IEEE 802.3:
| Classical ethernet | Modern ethernet |
| ---- | ---- |
| connected in bus topology, use CSMA/CD for medium access control. | Connected in star topology, use a central switch to control, exclude the need of medium access control.

- Ethernet frame:
	- An ethernet frame is divided into 4 parts.
	
	| Name | Function | 
	| ---- | ---- |
	| Preamble | Marking the starting of a frame |
	| Address | Physical addresses of source and destination (6-byte length). |
	| Type | Upper layer protocol (IP, Novell IPX, AppleTalk, …) |
	| Checksum | Error detection code. CRC?? |

### 5. Wireless LAN - WLAN - IEEE 802.11:
- Structure: include base station = access point and stations with wireless network interfaces
		
- Base station modes of operation:
	+ Basic Service Set (BSS): 
	+ Ad-hoc: Stations also play the role of AP

- Standards: 
	
| Name | Specifications |
| ---- | ---- |
| 802.11b | Band 2.4-5 GHz (unlicensed spectrum); Maximum speed 11 Mbps |
| 802.11a | Band 5-6 GHz; Maximum speed 54 Mbps |
| 802.11g | Band 2.4-5 GHz; Maximum speed 54 Mbps |			
| 802.11n | use multiple antennas (MIMO); Band 2.4-5 GHz; Maximum speed 200 Mbps |
		
> [!TIP]
> WLANs employ CSMA/CA for multiple access control

- Frame structure:

![802.11 Frame structure](/COMPUTER%20NETWORKS/FRAME-addressing%20in%20WLAN.png)
 
- Channel and correction: 
	+ Band is divided into 14 channels spaced 5Mhz apart.
		
	+ Admin can choose working freq for AP or auto.
	
	+ Station: need to connect to an AP by scanning channels and listen to intial frames (contains SSID and MAC address of AP) -> choose one AP.

		
- AP scanning mechanism:
	+ Passive: AP send beacon frames first, then stations proceed to request connection.
		
	+ Active: Stations broadcast request to find AP -> AP reply -> connection establish.
		
- Collision avoidance in WLAN:
 
	- CSMA/CA:
   	 + Sender: Channel available during DIFS then send entire frame.

   	   		If channel busy then starting random back-off (waiting).
   	   		At the end of back-off, send again, if no ACK then double back-off and try again.
    	+ Reciever: If recieve frame, send ACK after SIFS.
		
		- Collision avoidance:
	
				1. Sender send frame RTS (request-to-send) to BS using CSMA.
				2. BS broadcast the frame CTS (clear-to-send CTS) to answer
				3. All stations receive CTS
					 Sender send data frame
					 All other stations has to cancel the intention to send frames.

![RTS-CTS](RTS-CTS_Collision%20avoidance.png)

### 6. Virtual LAN (VLAN):
- Purpose: scaling and administrative issue.

- Approach:
	+ Port based VLAN: 1 physical switch acts as multiple virtual switches.

 	Properties:
					
				1. Traffic isolation: frames to/from ports 1-8 can only reach ports 1-8
				can also define VLAN based on MAC addresses of endpoints, rather than switch port
			 	
				2. Dynamic membership: ports can be dynamically assigned among VLANs
				
				3. Forwarding between VLANS: done via routing (just as with separate switches)
					• in practice vendors sell combined switches plus routers
			
> [!TIP]
> In a virtual LAN there's a port called a **trunk port**: carries frames between VLANS defined over multiple physical switches.

		
### 7. Access network:
 
- A type of telecommunications network which connects subscribers to their immediate service provider.
	
- Architecture:
 
![Optical access network](/COMPUTER%20NETWORKS/Fiber-to-the_MODEL.png) 	

1. Hub: provider side
	
2. NIU (Network Interface Unit): Client side

3. Remote node (RN): 
	- In a broadcast network, RN distribute data from Hub to all NIU
				
	- In a switched network, RN receives data from Hub and distributes different data flows to different NIU
4. ONU (Optical network unit): A device to convert optical signal into electrical signal.

	- AON (Active optical network) and PON (Passive optical network):

		- AON: Active Optical Network
		
				• Network use active technology (RN consumes electricity)
				• Remote Node analyses and route packets to destinations
				• Cable length could be up to 100km

		- PON: Passive Optical Network
		
				• Passive Network (No external energy source is need for RN)
				• RN (Splitter) only repeat signals to all ports 
				• Upstream: MUX from different sources by TDM (TDM PON) or WDM (WDM PON)
				• Limit cable length (20km)
	
		- GPON (Gigabit capable optical network):

			 	• GPON can be used to transport different types of data frame: Ethernet, ATM,
			 	 voice, …
				• Data from OLT to subscribers use a shared channel between OLT and RN
				• Downstream broadcast
				•	Upstream TDM
				• Data encapsulated in GPON frames have fields of receiver ID (for downstream), and sender ID (for upstream) 


# CHAPTER 6 - INTERNET LAYER		

### 1. IP:

1. **Role**: forwarding and routing between distant nodes.	

2. Principles:
	- host: end systems.
	- subnetworks: collection of hosts connected by 2nd layer devices.
	- forwarding:   
		- direct: without routers
		- indirect: with routers

3. Forwarding mechanism:
	- Routing table
	- Rule for sending packets: 
			
			if dest IP has same prefix as one of the interface -> send directly.
			else -> send to a router according to IP table.
>[!IMPORTANT]	
> IP characteristics:
> - Not reliable / fast: no mechanism to recover lost/error data. When necessary, data integrity is ensured by TCP in Transport layer.
> - Packets are processed independently.

### 2. IP ADDRESS:

1. IPv4:
	- A 32-bit number identifying uniquely a network interface.
	- For routing purpose, IP address of interfaces in the same subnetwork have the same prefix.
	- IP addresses have two parts: the host id and the network id.

2. Classful / Classless IP addresses (for IPv4 only):
	- Classful:
		+ Inefficient use of addressing space due to its hard classification of the address space into classes, making it inefficient to use all of address space.
		+ IPv4 space is depleting fast -> classful needs to be replaced. 
![Classful_IP](Classful_IP_address_structure.png)

	- CIDR: Classless Inter Domain Routing:
		+ IPv4 address have two parts: an address and a network mask, where the mask decide how many bits in the IPv4 address belongs to the network address part.
  		+ For each network mask, the part with consecutive 1s decides how many bits of the IP address belongs to the network address part, whilst the 0s determine the host address part. 
  		+ Example of network mask:
![Network_mask](Network_mask.png)  

3. Subnets:
	- Subnet is a part of a network, hosts of a subnet communicate directly without reaching to layer 3.

	- Subnet division principle: 
		+ Divide an IP range into sub-ranges of equal size.
		+ Take some bits from HostID part to distinguish subnets.

![Dividing_into_subnets](Dividing_to_2_subnets.png)
   
4. Addressing space of IPv4:
	- In theory:
		+ All between 0.0.0.0 ～ 255.255.255.255	
		+ Some special address (RFC 1918)
	
5. IPv6:
	- 128 bit address ( 64 for network ID / 64 for host ID)
	- Security feature is integrated	
> [!CAUTION]	 
> Special address in CIDR (always reserved):
> 
> ***NETWORK ADDRESS***: address where the **hostID's** bits are all **0s**
> 
> ***BROADCAST ADDRESS***: address where the **hostID's** bits are all **1s**

### 3. IP package:
| Name | length (in bits) | Function |
| ---- | ---- | ---- |
| Version | 4 bits | Version?
| Header length | 4 bits | length of header in range 5 -> 60 bits? |
| DS | | Used for QoS management by some router. |
| Length | 16 bits | total length of the packet including header. |
| 16 bits Identifier – ID of the packet; Flag; Fragmentation offset | | for fragmentation/reassemble purpose. |
| TTL | 8 bits | maximum number of hops the packet is allowed to perform. |
| Protocol | | upper layer protocol. |
| Checksum | | to detect corruption in the header of IPv4 data packets. |
| Source IP | 32 bits | Source IP |
| Dest IP | 32 bits | Destination IP |

![IP_packet_header](IP_header.png)

### 4. Internet Control Message Protocol (ICMP):

- ICMP is used in network layer for providing information exchange between sender and receivers.
- ICMP message: Type, Code, with 8 first bytes of the error IP message
	1. ICMP format:
		- Type: type of ICMP message
		- Code: cause of error
		- Checksum
		- Rest of header varies according on type
![ICMP_message_type](ICMP_messages_type.png)
	2. Ping / traceroute:
		- ping: 
	 
				• Test a connection
				• Sender sends packet “ICMP echo request”
				• Receiver responses with “ICMP echo reply”
				• Data field contains the time stamp when the packet is sent

		- traceroute: 
		
				• Calculate round-trip-time (RTT).
				• Sender send many packets to reciever (1st has TTL=1; 2nd has TTL=2; ...)
				• When nth packet arrives => Router destroy packet => send back an ICMP packet (type 11, code 0)
			    containing the IP address of the nth router. RTT can be calculated based on the reply message.

### 5. Network address translation (NAT):
	
1. NAT:
	- NAT: all devices in local network share just one IPv4 address as far as outside world is concerned

2. Advantages:
	- Just one IP address needed from provider ISP for all devices
	- Can change addresses of host in local network without notifying 
	  outside world
	- Can change ISP without changing addresses of devices in local 
	  network
	- Security: devices inside local net not directly addressable, visible 
	  by outside world

3. Implementation:
	- Outgoing datagrams: replace source IP & port number of outgoing datagram to NAT IP & new port number
	- Remember the mapping of Inside IP/port to NAT IP/port using NAT table.
	- Incoming datagrams: replace (NAT IP address, port #) in destination fields of every incoming datagram with corresponding 
	(source IP address, port #) stored in NAT table.
	- Types of NAT:
		
		|    Name | Description |
		| ---- | ---- |
		|     Static NAT | Each inside address is mapped to 1 outside NAT address. |
		|    Dynamic NAT | Each available public IP will be assigned for a private IP dynamically. |
		|    PAT-NAT | Only use 1 public IP, map inside IP to public IP plus a port number dynamically. |

### 6. Address resolution protocol (ARP):

1. ARP table:
	- ARP table: each IP node (host, router) on LAN has a table.
	- Contains  IP/MAC address mappings for some LAN nodes.
	- Each record has a TTL, after TTL expire -> record deleted.

2. ARP protocol:
	- Not in table -> broadcast to find MAC address of reciever.
	- Add recievers reply to ARP table.
	
3. Routing to another subnet in ARP:
	- Case study: A wants to send to B in a different network via R.
	- A know B address.  
![routing_1](Routing_to_another_subnet_1.png)

![routing_2](Routing_to_another_subnet_2.png)

![routing_3](Routing_to_another_subnet_3.png)

![routing_4](Routing_to_another_subnet_4.png)

![routing_5](Routing_to_another_subnet_5.png)

![routing_6](Routing_to_another_subnet_6.png)

### 7. Dynamic Host Configuration Protocol (DHCP):
	
1. DHCP:
	- Goal: host dynamically obtains IP address from network server when it 
	“joins” network
	- Can renew its lease on address in use
	- Allows reuse of addresses (only hold address while connected/on)
	- Support for mobile users who join/leave network 

2. Overview:		
	- host broadcasts DHCP discover msg [optional]
	- DHCP server responds with DHCP offer msg [optional]
	- host requests IP address: DHCP request msg
	- DHCP server sends address: DHCP ack msg 
	- DHCP diagram: 
![DHCP_model](DHCP_client-server_model.png)

	- In-case DHCP server does not belong to the same subnet as the client, a DHCP relay is performed:
![DHCP_relay](DHCP_relay.png)

3. Extended using:
![DHCP-extended](Extended_using_DHCP.png)
4. Extras:
	- DHCP can return more than just allocated IP address on subnet:
	- address of first-hop router for client
	- name and IP address of DNS sever
	- network mask (indicating network versus host portion of address)


# CHAPTER 7 - ROUTING

### 1. What is routing:

1. Basics:

- Router :
	- Is a computer with particular hardware
	- Connects multiple networks together, has multiple network interfaces
	- Forward packets according to routing table

- **TLDR**: Router is the device that forwards data between networks


-  Routing is a mechanism so that a host or a router decides how to forward a packet from source to destination.
- Result of the routing is a routing table

- What to consider in routing
	1. Building routing table 
	2. Information need to calculating route
	3. Routing algorithm and protocol.
			       
![Routing](Routing-principle.png)

- Routing principle:
	
		When a host send an IP packet to another host:
	
		1. If the destination and the source are in the same physical medium: Transfer directly
		
		2. If the destination is in a different network with the source: Send through some other routers (need to choose route)

- Routing table:

	- Lists of possible routes, saved in the memory of router

	- Main components of routing table:
		- Destination network address/network mask
		- Next router address

![Routing-table-example](routing-table-example.png)

2. Longest matching rule and default route:

- Suppose you have a destination address of 11.1.2.5, which route should you take according to the following routing table:

![Longest-matching-1](Longest-matching-1.png)

![Longest-matching-2](Longest-matching-2.png)

- According to the binary representation of the ip addresses, the route we should choose here is 11.1.2.0/24
- Explain - What counts as a longest match?

		- An address is the longest match if it satisfies the following conditions:
		1. In binary representation, all bits of the network address of the route and the destination must match under that particular mask.
		Example:
			11.1.2.5 = 	  00001011.		00000001.		00000010.		00000101 
		matches with
			11.1.2.0/24 = 00001011.		00000001.		00000010.		00000000

		but does not matches with
			11.1.3.0/24 = 00001011.		00000001.		00000011.		00000000 
			because the 24th bit is different

		however it still matches with
			11.1.3.0/23 = 00001011.		00000001.		00000011.		00000000 
			
			because all bits of the network address aka 1-23rd bits are the same
		
		2. The length of the network mask in case there is a match must be the longest

- Default route:
	- If router does not find a route to a destination in its routing table, default route is necessary
	
	- Default route is defined for all destination networks that are not figured in the routing table.

	- 0.0.0.0/0 is the address of the default route
		- Is a special notation for all destination networks

3. Route aggregation:

- There are many networks on the Internet, hence if we try to store route for each network
	- There will be a lot of entries in the routing table?

- **Solution**: the entries to sub-networks of the same “big” network can be aggregated<br> in order to reduce the size of routing table.

> ![NOTE]
> Default route is a type of route aggregation

![route-aggregation](route-aggregation.png)

- Example:
	- In this case, if someone wants to send to 200.23.1.0/24, they only need to have the route to <br> 200.23.0.0/22 in their table.

4. Exercise and solutions:

![Routing-excercise-1](Routing-excercise-1.png)

![Routing-excercise-2](Routing-excercise-2.png)

![Routing-excercise-3](Routing-excercise-3.png)

![Routing-excercise-4](Routing-excercise-4.png)

> ![IMPORTANT]
> FOR QUESTION 2, there can be multiple answers that matches the criteria

### 2. Static and dynamic routing:

1. Why the need of update routing table?
	- Network structure may change overtime
		1. New network is added.
		2. Router failure due to power corruption …

	- Hence, it’s necessary to update routing table 
		1. in theory: all nodes
		2. in pratice: some node

2. How to?

| Name | Description | Pros | Cons | 
| ---- | ---- | ----| ---- | 
| Static routing | Entries in routing table are added manually by administrator |Stable & Secure | Very...static, of course<br> Back up link cannot be used <br> Difficult to manage |
| Dynamic routing | Automatically update routing table by mean of routing protocols | Easy to manage & Backup link can be utilized | Insecure <br> Difficult to understand the routing protocols


### 3. Routing algorithms and protocols:

1. Routing protocol:
- Goal: determine “good” paths (equivalently, routes), from sending hosts to receiving host, through network of routers

- Path: sequence of routers packets traverse from given initial source host to final destination host
	- “good”: least “cost”, “fastest”, “least congested”

> ![TIP]
> Routing is a “**TOP-10”** networking challenge

2. Routing algorithms:

- Classification:

![routing-algos-classification](Routing-algorithms-classification.png)

- Dijkstra's link-state routing-algorithm:
	
	- It is the Dijkstra's algorithm for finding the shortest path from 1 node to others in a graph with no edges having sub-zero weight.
	
	- Properties:
		1. Centralized: network topology, link costs known to all nodes

				• accomplished via “link state broadcast” 
				• all nodes have same info
		2. Computes least cost paths from one node (“source”) to all other nodes

				• gives forwarding table for that node

		3. Iterative: after k iterations, know least cost path to k destinations
	
	- **Notations**:
		- Algorithm complexity:
			
				1. each of n iteration: need to check all nodes, w, not in N
				2. n(n+1)/2 comparisons: O(n^2) complexity
				3. more efficient implementations possible: O(nlogn)

		- Message complexity:

				1. each router must broadcast its link state information to other n routers 
				2. efficient (and interesting!) broadcast algorithms: O(n) link crossings to disseminate a broadcast message from one source
				3. each router’s message crosses O(n) links: overall message complexity: O(n^2)

- Distance vector algorithm:
	- Based on Bellman-Ford (BF) equation (dynamic programming)

![Equation](Bellman-Ford-equation.png)


### 3. Hierarchical routing:

1. Motivation:
	
	1. The Internet structure isn't "flat", as in not all routers are identical in terms of capability, administrative priveleges, etc...

	2. The scale of the Internet is absolutely massive with billions of destination, means that:
		- can’t store all destinations in routing tables!
		- routing table exchange would swamp links

	3. On the topic of administrative autonomy, since the Internet is a network of networks, each network admin may want to control routing in its own network

2. Approach:
	- Aggregate routers into regions known as “autonomous systems” (AS) (a.k.a. "domains”)

- 2 types of domain routing:

| Name | Function | Properties |
| - | - | - |
| Intra AS (domain) | routing among within same AS (“network”) | - All routers in AS must run same intra-domain protocol <br> - Routers in different AS can run different intra-domain routing protocols <br> - Gateway routers: at “edge” of its own AS, has link(s) to router(s) in other AS’es |
| inter-AS (domain) | routing among AS’es | Gateways perform inter-domain routing (as well as intra-domain routing) <br> - There is only one interdomain routing protocol : BGP - will be discussed later |

> ![TIP]
> Here's an example of the hierarchy of the Internet:

![internet-hierarchy-example](internet-hierarchy.png)

3. Autonomous system (AS):

- A set of routers with the same routing policy (routing protocol, metric…) is aggregated into an AS
- Gateway: router connect between two ASes
- Each AS has an unique number (ASN - 16 bits or 32 bits).

![AS-examples](autonomous-systems-example.png)

- Inter/intra domain routing:
	- Some protocols for intra-domain routing (a.k.a IGP or Interior Gateway Protocol):
		- RIP: Routing Information Protocol 
		- OSPF: Open Shortest Path First
		- IS-IS, IGRP, EIGRP (Cisco)… 
	
	- For inter-domain routing (a.k.a EGP or Exterior Gateway Protocol), there is only **ONE** option:
		-	BGP (v4): Border Gateway Protocol

> ![TIP]
> Here's an example of intra/inter domain routing of the Internet:

![Inter-intra-routing](Inter-intra-domain-routing.png)

- Forwarding table configured by intra- and inter-AS routing algorithms follows the below principle: 

	1. For destinations within AS: intra-AS routing determine entries 

	2. For external destinations: inter-AS & intra-AS determine entries 

- Inter-AS routing: a role in intra-domain forwarding:
	- **Question**: suppose a router in AS1 receives datagram destined outside of AS1, how does it know which gateway router of AS1 should the packet be forwarded to? 
	- Hence, AS1 inter-domain routing must:

			1. Learn which destinations reachable through AS2 or AS3 (in example)
			2. Propagate this reachability info to all routers in AS1

![Inter-AS-routing-role-in-intra-domain-routing-Example](Inter-AS-routing-role-in-intra-domain-routing.png)

- Intra-AS routing:
	1. RIP: Routing Information Protocol [RFC 1723] 
		- classic DV: DVs exchanged every 30 secs
		- no longer widely used
	2. OSPF: Open Shortest Path First [RFC 2328] 
		- link-state routing
	3. IS-IS protocol (ISO standard, not RFC standard) essentially same as OSPF
	4. EIGRP: Enhanced Interior Gateway Routing Protocol 
		- DV based
		- formerly Cisco-proprietary for decades (became open in 2013 [RFC 7868])


### 4. Intra-domain routing protocol

1. RIP (Routing Information Protocol):

- IGP
- RIP v.1, currently use RIP v.2
- Distance-vector algorithm
- Routing metric: # of hops (max = 15 hops)

- How RIP exchange information:
	- Routing table of router is exchanged
	
	- Periodic
		- Node advertise its distance-vector with neighbors every 30s
		- Each message contains up to 25 routing table entries
		- In practice, multiple messages are sent
	- Trigger
		- When every entry changes, send copy of entry to neighbors
		- Neighbors use to update their tables

- RIP timers:
	1. Update timer
		- Exchange routing table every 30 sec
	2. Invalid timer
		- Updated every time router receives information
		- If it is time out (180sec), it becomes hold down status
	3. Hold down timer
		- Router keeps routing information for 180 sec
		- Not refer the worse update (to avoid the loop)
		- Possibly down status
	4. Flush timer
		- Update every time router receives information
		- If 240sec passed, routing entry will be deleted

![RIP-timers-graph](RIP-timers-graph.png)

- Ping-pong failure in RIP:

![Ping-pong problem](Ping-pong%20problem.png)

- To tackle ping-pong failure:
	1. Limit the maximum hop count, e.g: 16
	2. Split horizon
		- The routing info will not return back to the sender
	3. Poison reverse
		- When network is down, send update with metric 16
		- That routing information become Hold-down status

2. OSPF (Open Shortest Path First):

- IGP

- “open”: publicly available - standard by IETF (current version, version 3, defined in RFC 2740)

- Classic link-state 
	- each router floods OSPF link-state advertisements (directly over IP rather than using TCP/UDP) to all other routers in entire AS
	- multiple link costs metrics possible: bandwidth, delay
	- each router has full topology, uses Dijkstra’s algorithm to compute forwarding table (Shortest Path First)

- Advanced features
	- security: all OSPF messages authenticated (to prevent malicious intrusion) 
	- Large AS: Hierarchical OSPF
	- Classless routing (able to use Variable-Length Subnet Masking -VLSM )
	- Different metric for each link based on TOS (is not used in practice)

- Hierarchical OSPF:
	- Why we have to divide the network into small area?
	- If we have more than 100 routers….
		- Link state update is delivered all the time
		- Number of re-calculation increase
		- Need more memory, need more CPU power
		- Number of link state update become large
		- Routing table become large
	- Area
		- Group of routers which share the same LSA

![Hierarchical-OSPF](Hierarchical-OSPF.png)