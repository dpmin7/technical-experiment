# Experiment 4: Performance Test for Aircraft CPA Computation

## Results and Recommendations

- **Experiment 1**
    
    - **Environment**
        - Applied the provided CPA computation module as a DLL in a C# project
        - Used approximately 9,000 pre-recorded aircraft data
        - Performed CPA computation for all aircraft pairs
            
    - **Results**

|Trial|Total Aircrafts|Total Pairs Calculated|Elapsed Time (s)|
|---|---|---|---|
|1|8461|35,790,030|12.67|
|2|8632|37,251,396|14.46|
|3|8774|38,487,151|13.49|
|4|8917|39,751,986|14.17|
|5|9039|40,847,241|13.33|
|6|9039|40,847,241|12.89|
|7|9039|40,847,241|13.38|
|8|9039|40,847,241|13.53|
|9|9039|40,847,241|13.38|
|10|9039|40,847,241|13.53|

- **Average Aircraft Count**: 8,901.8
- **Average Pairs Calculated**: 39,636,400.9
- **Average Elapsed Time**: 13.48 seconds
    
- **Experiment 2**
    - **Environment**
        - Applied a horizontal distance filter:
            - Only calculated CPA for aircraft within 85NM horizontal distance
        - Other settings identical to Experiment 1
        
    - **Results**

|Trial|Total Aircrafts|Total Pairs Calculated|Elapsed Time (s)|
|---|---|---|---|
|1|8763|274,437|0.62|
|2|8816|277,236|0.58|
|3|8827|278,390|0.58|
|4|8880|281,687|0.57|
|5|8935|284,073|0.61|
|6|8952|285,173|0.61|
|7|8991|288,322|0.60|
|8|9039|291,233|0.58|
|9|9039|291,232|0.57|
|10|9039|291,232|0.56|

- **Average Aircraft Count**: 8,898.5
- **Average Pairs Calculated**: 284,101.5
- **Average Elapsed Time**: 0.588 seconds

- Performing CPA computation for all aircraft results in an impractically long processing time
- Applying filters before CPA computation is deemed necessary to reduce the processing time

## Purpose

Implement a distance calculation algorithm to support aircraft collision avoidance.  
For each selected aircraft pair, compute CPA distance and time, and measure processing duration.  
Perform pairwise CPA calculations for all active aircraft and measure overall processing time.  
Based on these results, explore ways to reduce the computational load and derive implementation strategies.

## Status

- Concluded
    
## Expected Deliverables

- Measured processing time (computational load) of CPA distance/time computation between aircraft
- Implementation of aircraft CPA computation logic
    
## Required Resources

- C++/C# build environment
- 1 developer for 5 days
- 1 laptop
- Recorded aircraft position log data

## Experiment Description

- The function computes CPA distance/time using aircraft position (latitude, longitude, altitude), speed, and heading
- Perform large-scale CPA computation using real-world recorded aircraft data
- Investigate filtering methods to exclude aircraft pairs with no collision risk:
    - Exclude aircraft with large horizontal separation (Distance > 85NM)
        - Justification: Typical maximum aircraft speed is approximately 500 knots
        - Two aircraft 85NM apart flying head-on would require about 300 seconds (5 minutes) to collide
        - Therefore, immediate CPA calculation is not necessary
            
## Timeline

- Acquire aircraft data by **June 18**
    
- Complete experiments by **June 20**
    
- Derive and document results by **June 21**
    
## Related Links & References
N/A
