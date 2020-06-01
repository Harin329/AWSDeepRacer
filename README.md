My AWS Deep Racer Progress in May 2020

- 10 Days of Learning + Setup
- 20 Days of Trial and Error Training

Goal:
- Finish top 100, or top 50% of all racers

Result: <br />
<b>Summit Time Trial - 32/341         - Top 9%</b>  <br />
Summit Head 2 Head - 37/157           - Top 23% <br />
<b>Virtual Time Trial - 79/1291       - Top 6%</b> <br />
Virtual Object Avoidance - 39/134     - Top 29% <br />
Virtual Head 2 Head - 50/202          - Top 25% <br />

Success :)

***

<b>Model Description:</b>
1. <b>Barcelona Model</b>
  - Attempt to use a complex functions and guide the car to follow a drawn line based off of Fernando Alonso's F1 track record in 2018.
  - Too complex, convergence was too slow, car wasn't really learning
  - Performed decently, was my leading Barcelona model until All You Model (#5)
2. <b>Slow Complex Model</b>
  - Similar Attempt as Model 1, without pathfinding
  - Surpassed by Pathfinder Model (#3)
3. <b>Pathfinder Model</b>
  - Relying only on a given path and speed
  - Surpassed by Speed Model (#4)
4. <b>Speed Model</b>
  - Rewarded completion and staying left of track, less distance to cover on the left, much simpler
  - Surpassed by All You Model (#5)
5. <b>All You Model</b>
  - Simplest Model, Don't go off track, finish the lap, fast
  - Top finishes, could've been improved with more training time
