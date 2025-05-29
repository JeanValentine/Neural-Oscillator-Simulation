# Neural-Oscillator-Simulation
---
**Project Overview**
---
We are implementing a dynamic simulation of couple neural oscillators using the Kuramoto model. Neural oscillators are simplified mathematical representations of neurons or neuron groups that exhibit rhythmic activity. By coupling these oscillators with adjustable strenght, this simulation models how synchronization emerges in networks resembling biological neural systems. 

**What the code actually does**
  * Simulates 30 neural oscillators each with its own natural frequency drawn from a normal distribution, representing neuronal variability.

  * How oscillator phases evolve over time and how its influenced by instrinsic frequency and the collective coupling with other oscillators.

  * Visualizes:
      - Neural phases on a unit circle, showing oscillators as points rotating in sync or desynchrony
      - Order parameter r(t): a quantitative measure (from 0 to 1) of network synchronization over time.
   
  * Includes an interactive slider to adjust the coupling strenght K in real time. This demostrates the transition from incoherent (low synchronization) to coherent (high synchronization) states.

  * The order parameter plot continuously scrolls to show synchronization dynamics over an extended time period.

**Practicality** 
---
  * The kuramoto model is a foundational mathematical framework in neuroscience, physics, and complex systems research.

  * Helps us understand synchronization by explaning phenomena such as brain rhythms, coordination between brain areas, and disorder like epilepsy.

  * This simulation provides a practical, hands on tool to explore nonlinear dynamics, phase transitions, and collective behavior in neural systems.

 **This project combines:**
 
     - Theoretical foundations in mathematical modeling of oscillators
     - Computational implementation for numerical integration and animation
     - Interactive visualization for real time paramter tuning

**How to run**

    * requires Python with numpy and matplotlib libraries 
    * Run NeuralOscillatorSimulation.py 
    * Use the slider below the plots to adjust coupling strenght K dynamically 
    * Observe the oscillator phases on the unit circle and how synchronization (order parameter r) evolves over time

**Examples**


**Future extensions**
 * implement noise effecrs and hetergeneous network topologies
 * Incorporate real neural data for comparison
 * Enhance interactivity with parameter sweeps, phase histograms, and export features 
