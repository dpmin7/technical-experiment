# Experiment 1: Improving Rendering Performance When Displaying 10,000+ Objects
 

## Results and recommendations 
 - Ensure the system maintains optimal rendering performance when displaying over 10,000 objects, without degrading responsiveness or affecting other system operations.

   Among the four approaches, the Vertex Buffer Object (VBO) method and instanced rendering are expected to deliver the best performance.  
   However, since instanced rendering cannot be applied at our current implementation level of OpenGL 2.x, we decided to exclude the instanced rendering approach.

   typical way : 0.211s  
   code base(Immediate Mode) : 0.077s  
   Vertex Buffer Object (VBO) : 0.062s  
   <s>instanced rendering : -s</s>

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
