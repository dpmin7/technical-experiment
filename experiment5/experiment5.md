# Experiment 1: SDR and antennae connection recovery experiment

## Results and recommendations
As of the initial phase of the experiment:

- It has been confirmed that when the SDR and antenna are physically connected and functioning properly, the `dump1090` program runs without error and successfully feeds data to ADSBHub.
- A `systemd` service unit was created to automatically start both `dump1090` and the ADSBHub feeding script at system boot.
- It was verified that `dump1090` automatically restarts when it is terminated abnormally (e.g., via kill signal), using `Restart=always` in the service unit configuration.
- However, when the SDR device is physically disconnected, `dump1090` fails to operate correctly and repeatedly restarts without successful recovery.
- Therefore, a monitoring program is required to detect physical disconnection of the SDR and to manage the recovery process by conditionally restarting `dump1090`.

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
3. Create a `systemd` service unit that starts `dump1090` and the ADSBHub script at system boot — ✅ Confirmed.
4. Verify that `dump1090` restarts on abnormal termination (e.g., kill signal) — ✅ Confirmed.
5. Simulate a failure by physically disconnecting the SDR or antenna and observe system behavior.
6. Identify that automatic restart via systemd does not resolve physical hardware issues — ✅ Observed.
7. Develop a monitoring mechanism (e.g., script or watchdog) to detect hardware disconnection.
8. Implement logic to suppress repeated restarts when the hardware is unavailable and to resume operation once it becomes available.
9. Verify and log system behavior throughout the experiment.

## Duration
Deadline: 2025-06-17  
(Progress checkpoints can be optionally defined if needed.)

## Links and references
- https://github.com/antirez/dump1090  
- https://www.adsbhub.org/howtofeed.php
- https://github.com/dpmin7/flight-tracker
