# slef_learning-event-driven-object-oriented
Reference to Stanford University’s assignment CS106AP: Programming Methodologies in Python and CS106B: Programming Abstractions as practice, focusing topics: event-driven and object-oriented
## Projects Source Codes:
* [breakout](https://github.com/An022/self_learning-event-driven-object-oriented/blob/main/breakout/breakout.py)\
* [breakoutgraphics](https://github.com/An022/self_learning-event-driven-object-oriented/blob/main/breakout/breakoutgraphics.py)\
  * Milestone 1: Fill in the BreakoutGraphics constructor (breakoutgraphics.py)\
  (1) Create a paddle at the correct starting location using the given constants.(PADDLE_OFFSET is the distance from the top of the paddle to the bottom of the window)\
  (2) Create a ball that whose center is in the middle of the window.\
  (3) Set default values for the ball’s initial x and y velocities. (referred to as vx and vy throughout the rest of this handout)\
  
  *  Milestone 2: Draw the bricks (breakoutgraphics.py)
  The number, dimensions, and spacing of the bricks are specified using named constants in the breakoutgraphics.py starter file.\
  The BRICK_OFFSET constant is the distance from the top of the window to the top edge of the first line of bricks.\ 
  The left side of the very first brick in a row should start at the very left edge of the window, and the remaining bricks should be drawn at appropriate locationsto produce the pattern detailed above. \
  
  *  Milestone 3: Connect the paddle to the mouse (breakout.py)
  The paddle moves along a fixed horizontal line on the bottom of the screen, and you are provided with a PADDLE_OFFSET constant that is the distance from the top of the paddle to the bottom of the window.
  
  *  Milestone 4: Get the ball to bounce off the walls (breakoutgraphics.py and breakout.py)
     * 1. The program needs to keep track of the velocity of the ball, which consists of two separate components that you can declare as class attributes.\ 
       The velocity components represent the change in position that occurs at each time step.\
       Initially, the ball should be heading downward, and we provide you with a starting speed constant for vy (y values increase as you move down the screen).\ 
       The game would be boring if every ball took the same course, so we use the function random.uniform(-MAX_SPEED, MAX_SPEED) to select the vx component randomly.\ 
     * 2. Get the ball to bounce around the world.\
  
  *  Milestone 5: Check for collisions (breakoutgraphics.py and breakout.py)
  Tell whether the ball is colliding with another object in the window.\
  
  1. Call get_object_at() on that location to see whether anything is there.\
  2. If the value you get back is not None, then you don’t need to look any farther. You can simply return that GObject, since it’s the object that the ball hit.\
  3. If get_object_at() returns None for a particular corner, go on and try the next corner.\
  4. If you get through all four corners without finding a collision, then no collision exists.\
  
  * 

  
  
  ```
  
  ```
