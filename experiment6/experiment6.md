# Experiment 6: Polygon-based Aircraft Filtering Module Implementation

## Results and recommendations

-  Set a polygon area and experiment to see if 10,000 points are included within the polygon (data is converted to ENU coordinate system based on latitude, longitude, and altitude data, and then filtered)

	-  c# :   It takes about 7msec
	- c++ : It takes about 0.5msec
	- The C++ implementation is approximately 14 times faster than the C# implementation in this test case
	- It is recommended to implement the functionality in C# for integration into the project, and to provide a C++ version as a DLL when higher performance is required.

- 프로젝트에 적용하여 기능 시험 완료
	- 좌표 변환 없이 위도, 경도를 이용하여 다각형 내 항공기만 필터링 하는 것으로 변경하어 적용
	- 기능 수행 확인
	
<img width="812" alt="Image" src="https://github.com/user-attachments/assets/faec9dff-b658-41ba-ab95-8379536d5a2f" />


## Objective

- Can we accurately and efficiently determine whether the real-time latitude/longitude coordinates of an aircraft are within a defined polygonal area?
- Impact:
  - Aircraft visualization filtering feature of the Remote User Interface (RUI)
  - The level of filtering required depends on the speed and volume of filtering operations

## Status

- Concluded
## Expected outcomes

- Measurement results of processing time based on the number of aircraft and the complexity of the polygons
- Test cases for the experiment
- Filtering module code:
  - Python code (for this experiment)
  - C++ or C# code (for integration into the final application)

## Resources required

- 1 person for 5 days
- Sample aircraft position data
- Sample polygon area definitions
- Python development environment
- C++/C# development environment

## Experiment description

- [x] Analysis of the provided code
- ~~Research algorithms and libraries on the Internet~~
	- Code is in the provided code(c++)
- [x] Create prototype python code
- [x] Test basic functionality (using x,y not longitude, latitude)
- [x] Create c++ and c# code and test.
- [x] Test code using longitude, latitude data
- [x] Document the results

## Duration

- Start date: 2025-06-12
- Midpoint review: 2025-06-14
- Target end date: 2025-06-17

## Links and references

- (TBD)
