# Friday Teaming #7 - Mars Rover Kata | Test Commit Revert

In this episode of Friday Teaming we will be implementing the Mars Rover Kata using Test Commit Revert (TCR)

Test Commit Revert, or TCR, is a development technique first proposed by Kent Beck in his blog article "test && commit || revert". If the tests pass, then the code is automatically committed. If the tests fail, then all of the changes since the previous commit are reverted and you start over.

test && commit || revert by Kent Beck https://medium.com/@kentbeck_7670/test-commit-revert-870bbd756864

## The Mars Rover Kata

You are part of the team that explores Mars by sending remotely controlled vehicles to the surface of the planet. Develop an API that translates the commands sent from earth to instructions that are understood by the rover.

Requirements
- You are given the initial starting point (x,y) of a rover and the direction (N,S,E,W) it is facing.
- The rover receives a character array of commands.
- Implement commands that move the rover forward/backward (f,b).
- Implement commands that turn the rover left/right (l,r).
- Implement wrapping at edges. But be careful, planets are spheres.
- Implement obstacle detection before each move to a new square. If a given sequence of commands encounters an obstacle, the rover moves up to the last possible point, aborts the sequence and reports the obstacle.