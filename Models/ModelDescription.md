1. Barcelona Model
  - Attempt to use a complex functions and guide the car to follow a drawn line based off of Fernando Alonso's F1 track record in 2018.
  - Too complex, convergence was too slow, car wasn't really learning
  - Performed decently, was my leading Barcelona model until All You Model (#5)
2. Slow Complex Model
  - Similar Attempt as Model 1, without pathfinding
  - Surpassed by Pathfinder Model (#3)
3. Pathfinder Model
  - Relying only on a given path and speed
  - Surpassed by Speed Model (#4)
4. Speed Model
  - Rewarded completion and staying left of track, less distance to cover on the left, much simpler
  - Surpassed by All You Model (#5)
5. All You Model
  - Simplest Model, Don't go off track, finish the lap, fast
  - Top 5-10% finishes, could've been improved with more training time
