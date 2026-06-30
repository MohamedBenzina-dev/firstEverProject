import random
import time


try:
    for scan in range(1, 6):
        print(f"Scan {scan}:")
        
        randomHumanPositionx = random.randint(1, 100)
        randomHumanPositiony = random.randint(1, 100)
        print(f"Human detected at position: ({randomHumanPositionx}, {randomHumanPositiony})")
        if randomHumanPositionx < 50 and randomHumanPositiony < 50:
            print("Human is in the lower left quadrant.")
            print("Robot is moving to the lower left quadrant to track the human.")
        elif randomHumanPositionx >= 50 and randomHumanPositiony < 50:
            print("Human is in the lower right quadrant.")
            print("Robot is moving to the lower right quadrant to track the human.")
        elif randomHumanPositionx < 50 and randomHumanPositiony >= 50:
            print("Human is in the upper left quadrant.")
            print("Robot is moving to the upper left quadrant to track the human.")
        elif randomHumanPositionx >= 50 and randomHumanPositiony >= 50:
            print("Human is in the upper right quadrant.")
            print("Robot is moving to the upper right quadrant to track the human.")
        
        time.sleep(2)  

        print("Robot has reached the human's position and is tracking the human.")

except KeyboardInterrupt:
    print("Tracking Stopped by User.")
    

        