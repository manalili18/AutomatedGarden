# Automated Garden
This project's goal is to automate the watering and nutrition of garden.

## Phases
1. Grounds planning, preparation, and planting
   * Where to plant, what to plant, when to plant
   * Infrastructure for automated watering, soaker hoses, various valves
   * Soil nutrition and quality
2. Soil moisture tracking
   * Trends and ideal moisture

3. Soil moisture control
4. Advanced weather anticipation (potential for AI)
5. Nutrition tracking
6. Nutrition delivery
7. Sell?

## Implementation

### Actual Garden Hardware
- Wireless valve
- some microcontroller
- moisture I/O
- Waterproofed housing
- Wireless I/O

#### SW
- Hopefully none

### Localized Metering
- Microcontroller reports to main control server

#### SW (more like firmware but yeah)
- Probe drivers
- Wireless comm drivers

### Centralized Control Center (Server HUB)
- Controls garden software
- Crunches numbers based on predicted rainfall/humidity/current moisture
- Records moisture over time
- Recommends adjustments to parameters for watering schedule
- Schedules ideal garden times
- Maintains ideal moisture
- need dedicated server at home
- phone app
- sell eventually?

#### SW (more like firmware but yeah)
- THERE IS A HUNK OF MEAT TO BE PUT HERE
- will definitely need help






