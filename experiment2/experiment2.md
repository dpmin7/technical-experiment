# Experiment 2: Tracker, Network Connection Recovery Experiment 
 

## Results and recommendations 
- 1. Tried to check if the server is alive using ICMP Request(ping), but the server did't respond. -> we can not use ICMP Request.  
- 2. Network disconnection and reconnection were detected through TCP connection attempts.  
     Connectivity with the ADS-B Hub and the local server was verified every 10 seconds using TCP connection attempts.   
	 (A 10-second interval was used for the ADS-B Hub to prevent potential problems that could arise from frequent TCP connection attempts.)  
	 For the Raspberry Pi, TCP connection attempts were performed every 2 seconds.  
- 3. Test for Detecting Internet Disconnection and Reconnection: All 50 out of 50 test attempts were successful.  
     Test for USB Disconnection between the Raspberry Pi and the SDR: All 50 out of 50 test attempts were successful.  

## Objective 
This experiment aims to verify whether network disconnection can be effectively detected using ping/echo methods and whether the system can recover and return to a normal state within 1 minute after reconnection.
The results will impact the following design decisions:

- Failure detection and failover logic design
- Network recovery timer configuration
- User notification policies
  The main technical questions to answer are:
  "Can a ping or echo request-based monitoring method detect network disconnection within 20 seconds?"
  "When the network is restored, does the system recover within 1 minute?"

## Status
[Done]

## Expected outcomes
- Logs of state changes during disconnection and recovery scenarios
- Monitoring logs using ping/echo requests
- Summary report (in PDF or tabular format)
- Presentation for internal design discussion

## Resources required
- Two test devices (Sender and Receiver roles)
- ICMP-based ping tools
- One engineer for 2 person-days
- Dedicated test network environment

## Experiment description
1. Set up a test environment with two devices sending ICMP ping requests at regular intervals.
2. Log ping responses during normal operation.
3. Manually disconnect the network (unplug LAN cable).
4. Measure the time taken to detect disconnection (based on ping response failures).
5. Reconnect the network after a predefined period.
6. Confirm whether normal operation resumes and measure the recovery time.
7. Repeat the test under various conditions (e.g., different disconnection durations, ping intervals).
8. Collect results and perform comparative analysis.

## Duration
- Total experiment duration: 2 days
- Day 1: Test setup and initial scenario runs
- Day 2: Repeat tests under varying conditions and analyze logs

## Links and references
- RFC 792 - ICMP Protocol Specification
- Linux ping manual
