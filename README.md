# Planet Simulator

A small interactive Python program for exploring a planet's two-dimensional orbit around a star. Choose a star and planet mass, initial separation, tangential velocity, and simulation duration, then view the resulting trajectories as a plot or animation. The program also includes a short orbital mechanics glossary.

## Features

- Interactive command-line menu with a glossary of orbital mechanics terms and Kepler's laws.
- Two-body Newtonian gravity: both the planet and star move in response to their mutual gravitational attraction.
- Static trajectory plot with the closest and farthest sampled orbital points, estimated eccentricity, and orbital period.
- Animation with trails, elapsed simulation time, current planet–star distance, and orbital details.
- User inputs in familiar units: star mass in solar masses, planet mass in Earth masses, distance in AU, velocity in km/s, and duration in days.

## Requirements

- Python 3
- Matplotlib
- Astropy
- Tkinter, for Matplotlib's interactive `TkAgg` window backend (often included with Python; on some Linux distributions it is a separate package)

Install the Python dependencies with:

```bash
python -m pip install matplotlib astropy
```

## Run

From the project directory, run:

```bash
python planet_simulator.py
```

On Windows, you can also use `py planet_simulator.py` if the Python launcher is installed.

At the menu, choose:

1. Read about orbital mechanics.
2. Enter system parameters and display a trajectory plot.
3. Enter system parameters and play an orbit animation.
4. Quit.

For options 2 and 3, enter positive finite values for masses and starting distance, a finite velocity in km/s, and a positive whole number of days. The initial planet position is on the positive x-axis and its velocity is along the positive y-axis. The star begins at the origin; it is not fixed in place during the simulation.

## Simulation details

The gravitational constant and Earth and Sun masses come from Astropy constants. One astronomical unit is set to 149,597,870,700 meters. The simulation advances in fixed one-hour steps using a semi-implicit Euler update. For a run of *N* days, it computes *N × 24* steps.

The plot reports the minimum and maximum planet–star separation found among the computed positions as periastron and apastron, and estimates eccentricity from those sampled distances. The orbital period is calculated from the initial position and velocity using the two-body vis-viva relation; it is labeled as not a closed orbit when those initial conditions do not imply a bound elliptical orbit.

## Notes

- This is an educational, simplified two-body model. It does not include other planets, non-gravitational forces, or adaptive time steps.
- Very close approaches or extreme inputs can reduce numerical accuracy because the time step is fixed at one hour.
- The animation calculates the trajectory before displaying it. Longer simulations therefore require more computation up front.
- The plotting window requires a working Tkinter installation and a graphical desktop session.
