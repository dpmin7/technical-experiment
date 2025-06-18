# Experiment 1: Improving Rendering Performance When Displaying 10,000+ Objects
 

## Results and recommendations 
 - Ensure the system maintains optimal rendering performance when displaying over 10,000 objects, without degrading responsiveness or affecting other system operations.
  typical way : 0.21s
  code base : 0.77s
  Vertex Buffer Object (VBO) : 0.62s
  instanced rendering : 0.63s
  Since there was no significant difference between the Vertex Buffer Object (VBO) approach and instanced rendering, we decided to proceed with VBO, as it is relatively easier to implement.

## Objective 
 - Identify and analyze potential performance degradation when rendering more than 10,000 objects on the screen, and assess its impact on overall system behavior.

## Status
[Concluded]

## Expected outcomes
 - Quantitative performance metrics depending on the number of rendered objects  
 - Representative test cases for rendering scalability validation  
 - Source code:
   1) Experimental C# code for benchmarking  
   2) Final C# module prepared for integration with the production application

## Resources required
 - 1 person for 2 days
 - Sample airport data
 - C# development environment

## Experiment description
### Completed:
 - [O] Analysis of the provided code
 - [O] Created prototype C# code
 - [O] Tested basic functionality (Object display confirmation)
 - [O] Developed and tested C# code
 - [O] Measured rendering performance based on OpenGL display method (Performance vs. number of objects)
 - [O] Document the results

## Duration
 - Deadline: 2025-06-17  

## Links and references
 - TBD
 
 
 typical way
실행 시간: 127 ms
실행 시간: 148 ms
실행 시간: 154 ms
실행 시간: 152 ms
실행 시간: 141 ms
실행 시간: 320 ms
실행 시간: 267 ms
실행 시간: 261 ms
실행 시간: 262 ms
실행 시간: 277 ms

0.2109

code base
실행 시간: 95 ms
실행 시간: 69 ms
실행 시간: 77 ms
실행 시간: 84 ms
실행 시간: 73 ms
실행 시간: 68 ms
실행 시간: 77 ms
실행 시간: 71 ms
실행 시간: 72 ms
실행 시간: 81 ms

0.767

Vertex Buffer Object
실행 시간: 58 ms
실행 시간: 81 ms
실행 시간: 58 ms
실행 시간: 62 ms
실행 시간: 49 ms
실행 시간: 64 ms
실행 시간: 66 ms
실행 시간: 51 ms
실행 시간: 69 ms
실행 시간: 59 ms

0.617

instanced rendering
실행 시간: 46 ms
실행 시간: 54 ms
실행 시간: 73 ms
실행 시간: 57 ms
실행 시간: 59 ms
실행 시간: 71 ms
실행 시간: 72 ms
실행 시간: 78 ms
실행 시간: 71 ms
실행 시간: 50 ms

0.631

0.631