# Experiment 3: Implement a C#-based prototype
 

## Results and recommendations 
Evaluation of the feasibility and suitability of C#/WPF-based implementation. 
Decision to adopt or not will be made based on the results.

## Objective 
 - Verify if we can build the main features at the same level as exist system with C#/WPF.
 - Verify that performance (rendering performance, data processing performance) is equivalent to or better than the existing system.

## Status
In progress

## Expected outcomes
 - A working C#/WPF prototype
 - Comparative report vs. existing implementation (functionality / performance / development convenience, etc.)
 - List of problems found and how we solved them
 - Simple sharing for the team

## Resources required
 - Visual Studio 2022
 - .NET Framework 4.7.2
 - WPF Framework
 - OpenGL or a similar library
 - Current source code to study
 - ChatGPT — for help with understanding code, converting to C#, finding libraries, writing sample code
 - About 5 person-days
 - Windows PC

## Experiment description
 - Study the current C++/Embarcadero code
 - Make and test each part:
   - UI
   - TCP communication
   - Data parsing and handling
   - Map tile display
   - OpenGL rendering
 - Do full tests and measure performance
 - Compare with the current version
 - Write and share the final results

## Duration
TO-DO: write the end date for this experiment.

## Links and references
TO-DO: list here publications, web pages, etc. that contain information relevant to the experiment. 

## Results
Step 1.
 - User Interface (UI):
   Basic window layout and interaction elements were created using WPF.
   Functionality equivalent to the existing system’s UI has been achieved for the tested parts.

 - TCP Communication:
   TCP client implementation is working as expected.
   Successfully connects to the server, receives streaming data, and handles connection state.

 - Data Parsing and Handling:
   Implemented a data parser that processes incoming TCP messages.
   Verified the correctness of parsing and real-time message handling logic.

   ![Image](https://github.com/user-attachments/assets/e2d1b15c-4611-4cc2-889d-9546ae1bfa81)

Step 2.
 - OpenGL rendering
   we experimented with OpenGL rendering by applying OpenTK, one of the available options for OpenGL integration in WPF, and tested rendering functionality.
   ![Image](https://github.com/user-attachments/assets/40dd4195-7df4-4171-a4e8-b2c08fc36ecd)
