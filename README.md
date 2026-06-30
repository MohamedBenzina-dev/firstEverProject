# firstEverProject
For my first ever project i did something simple that is the foundational logic behind a camera tracking system 


# How it works
Its pretty simple instead of tracking targets on a basic, single-axis flat line, this Python script simulates
**2D computer vision sensor tracking**. It divides a camera's field of view into four geometric quadrants using X and Y coordinates on a 100x100 grid but this is of course can be changed to you camera resolution and the quadrants are not going to be just four they would be a lot more


### How the Logic Breaks Down:
* **Lower Left:** `X < 50` and `Y < 50`
* **Lower Right:** `X >= 50` and `Y < 50`
* **Upper Left:** `X < 50` and `Y >= 50`
* **Upper Right:** `X >= 50` and `Y >= 50`


**Language:** Python 3
* **Concepts Used:** Control Flow Loops (`for`), Conditional Logic (`if/elif`), Target Randomization, and Exception Handling (`KeyboardInterrupt`).

Dev: Mohamed Benzina
