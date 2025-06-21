# Experiment 1: Improving Rendering Performance When Displaying 10,000+ Objects
 

## Results and recommendations 
 - Ensure the system maintains optimal rendering performance when displaying over 10,000 objects, without degrading responsiveness or affecting other system operations.

   typical way : 0.211s  
   code base : 0.077s  
   Vertex Buffer Object (VBO) : 0.062s  
   instanced rendering : 0.063s
   
   Among the four evaluated approaches, the Vertex Buffer Object (VBO) method and instanced rendering demonstrated the best performance.  
   Given that the performance difference between the two was negligible, the VBO method was selected for implementation due to its relatively simpler integration and lower development complexity.

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
