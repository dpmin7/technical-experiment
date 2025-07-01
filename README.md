# Technical Experiments Summary

This repository contains six key experiments conducted to evaluate and improve various aspects of the Intelligent Flight Tracking Assistant system. Below is a summary of each experiment and its key findings.

---

### ✅ Experiment 1: Improving Rendering Performance When Displaying 10,000+ Objects

- **Goal**:
  Evaluate performance degradation when rendering over 10,000 objects and its impact on UI responsiveness.

- **Approach**:
  Implemented and benchmarked multiple OpenGL rendering methods (e.g., VBO) using C#.

- **Result**:
  VBO showed the best rendering time (0.062s) among tested methods.

- **Conclusion**:
  VBO was selected as the optimal rendering approach under OpenGL 2.x constraints.

📄 [View Details](experiment1/experiment1.md)

---

### ✅ Experiment 2: Network Connection Recovery Experiment

- **Goal**:
  Verify whether disconnection and reconnection can be reliably detected and recovered using ping/echo and TCP methods.

- **Approach**:
  Tested ICMP and TCP-based monitoring with scheduled connection checks and measured recovery timing.

- **Result**:
  ICMP was blocked; TCP-based monitoring succeeded with 100% success in 50 trials for both internet and USB disconnection.

- **Conclusion**:
  TCP-based periodic connection attempts are reliable for fault detection and enable timely recovery within 1 minute.

📄 [View Details](experiment2/experiment2.md)

---

### ✅ Experiment 3: Implement a C#-based prototype

- **Goal**:
  Validate whether a C#/WPF implementation can match or exceed the functionality and performance of the existing system.

- **Approach**:
  Reimplemented core features including UI, TCP communication, OpenGL rendering, and map display using C# and WPF.

- **Result**:
  All key components were successfully implemented with performance comparable to the current C++ version.

- **Conclusion**:
  The C#/WPF-based prototype proved feasible and was confirmed as a viable replacement for the legacy implementation.

📄 [View Details](experiment3/experiment3.md)

---

### ✅ Experiment 4: Performance Test for Aircraft CPA (Closest Point of Approach) Computation

- **Goal**:
  Evaluate the computational load of CPA (Closest Point of Approach) calculations for large-scale aircraft tracking data.

- **Approach**:
  Conducted pairwise CPA calculations using ~9,000 recorded aircraft and compared full-set vs. distance-filtered computation.

- **Result**:
  Full CPA computation took ~13.5s on average; applying an 85NM horizontal filter reduced time to ~0.59s.

- **Conclusion**:
  Pre-filtering based on distance is essential for reducing computation time and enabling real-time CPA analysis.

📄 [View Details](experiment4/experiment4.md)

---

### ✅ Experiment 5: SDR connection recovery experiment

- **Goal**:
  Verify automatic detection and recovery from physical disconnection or malfunction of SDR or antenna on a Raspberry Pi system.

- **Approach**:
  Developed `systemd` services and a custom `sdrmonitor` script to manage `dump1090` and ADSBHub feeding based on hardware state.

- **Result**:
  All 50 manual disconnect/reconnect tests and 49/50 reboots succeeded in automatic recovery; 1 reboot failed due to unrelated OS issue.

- **Conclusion**:
  The proposed tactic demonstrated reliable fault detection and full recovery, ensuring robust ADS-B data feed availability.

📄 [View Details](experiment5/experiment5.md)

---

### ✅ Experiment 6: Polygon-based Aircraft Filtering Module Implementation

- **Goal**:
  Determine if aircraft positions (lat/lon) can be efficiently filtered against polygonal areas in real-time.

- **Approach**:
  Implemented and benchmarked filtering logic in Python, C++, and C# using both ENU and lat/lon comparisons.

- **Result**:
  C++ filtering was ~14× faster than C# (0.5ms vs. 7ms); lat/lon-based filtering was successfully integrated and validated in the project.

- **Conclusion**:
  C# is suitable for integration, with a C++ DLL recommended for performance-critical scenarios.

📄 [View Details](experiment6/experiment6.md)

---

📌 *For architecture decisions related to these experiments, please refer to the associated [ADRs](https://github.com/dpmin7/IFTA/tree/L5/ADRs) and design documents in the architecture repository.*
