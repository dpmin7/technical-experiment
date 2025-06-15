# Experiment 1: SDR and antennae connection recovery experiment

## Results and recommendations
As of the initial phase of the experiment, it has been confirmed that when the SDR and antenna are physically connected and functioning properly, the `dump1090` program runs without error and successfully feeds data to ADSBHub.  
This establishes the baseline for normal operation, which will be used to verify the effectiveness of the recovery mechanism in later phases of the experiment.

## Objective
The objective of this experiment is to determine whether it is possible to automatically detect a physical failure (e.g., disconnection or malfunction) in the SDR or antenna and recover from it by:
- stopping the `dump1090` program when a failure is detected, and
- restarting `dump1090` and resuming feeding to ADSBHub once the hardware connection is restored.

This will help increase the robustness and availability of the ADS-B data feeder system running on Raspberry Pi 5.

## Status
In Progress

## Expected outcomes
- Automatic shutdown of `dump1090` when SDR or antenna is physically disconnected or fails
- Automatic recovery and restart of `dump1090` and resumption of data feeding to ADSBHub when the issue is resolved
- Optional: a script or monitoring service prototype implementing the above behavior

## Resources required
- Raspberry Pi 5
- SDR (Software Defined Radio) USB device
- ADS-B antenna
- `dump1090` program
- ADSBHub feeding script
- 1 person-day, at a rate of 1 hour/day
- Internet connection

## Experiment description
The experiment will proceed with the following steps:

1. Set up `dump1090` and the ADSBHub feeding script on Raspberry Pi 5 with SDR and antenna connected.
2. Confirm that the system functions normally when hardware is connected — ✅ Confirmed.
3. Simulate a failure by disconnecting the SDR or antenna and observe system behavior.
4. Develop a monitoring mechanism (e.g., script or systemd watchdog) that detects hardware disconnection.
5. Implement automated stopping of `dump1090` upon failure detection.
6. Simulate hardware reconnection and implement detection of recovery.
7. Automatically restart `dump1090` and feeding script.
8. Verify and log system behavior throughout the experiment.

## Duration
Deadline: 2025-06-17  
(Progress checkpoints can be optionally defined if needed.)

## Links and references
- https://github.com/antirez/dump1090  
- https://www.adsbhub.org/howtofeed.php

