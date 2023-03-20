<!-- <p align="center"> -->
<!--   <img src="" width="300"/> -->
<!-- </p> -->
<p align="center">Track workouts and progress steadily.</p>

<p align="center">
  <a href="https://github.com/mastermedo/workouts/LICENSE">
    <img src="https://img.shields.io/github/license/mastermedo/workouts" alt="license" title="license"/>
  </a>
  <a href="https://github.com/mastermedo/workouts">
    <img src="https://img.shields.io/github/languages/code-size/mastermedo/workouts" alt="build" title="build"/>
  </a>
  <a href="https://github.com/mastermedo/workouts/stargazers">
    <img src="https://img.shields.io/badge/maintainer-mastermedo-yellow" alt="maintainer" title="maintainer"/>
  </a>
</p>

<!-- <p align="center"> -->
<!--   <a href="https://github.com/mastermedo/workouts"> -->
<!--     <img src="https://raw.githubusercontent.com/MasterMedo/mastermedo.github.io/master/assets/img/workouts.svg" alt="demo" title="demo"/> -->
<!--   </a> -->
<!-- </p> -->

## :clipboard: description
`workouts` let's you analyse your workout data, so you can make insights about it and adjust your schedule to meet your goals quicker. `workouts` lets you track two metrics:

- volume per exercise
- max weight (personal best) per exercise

# how it works
While doing a workout, the user writes workouts in their note taking mobile application of choice in a particular user-friendly format. Every so often the user manually copies those notes into the `/datasets/workouts/workouts.txt` and runs the `/analysis/workouts-analysis.py` which creates progress graphs per exercise in two formats volume[kg]/timestamp and max weight[kg]/timestamp.

The goal is to keep progressively increasing volume and/or max weight.

## :zap: features
- parse workouts from a simple form
- analyse workouts

## :chart_with_upwards_trend: analyse workout results
![](./img/abdomenin.png)
![](./img/abdomenout.png)
![](./img/bench.png)
![](./img/biceps_curl.png)
![](./img/dead_lift.png)
![](./img/hip_thrust.png)
![](./img/leg_extension.png)
![](./img/leg_press.png)
![](./img/pec_fly.png)
![](./img/squat.png)
## :shipit: installation
## :bulb: ideas for tests
## :question: usage
## future work
Exercises will be connected to muscle groups and how much do they actually strain the muscle so that these metrics can be tracked:

- volume per muscle group
- max weight(personal best) per muscle group

The program will suggest future exercises based on the rate of progress the user wants to have.
<p align="center">
  <a href="#">
    <img src="https://img.shields.io/badge/⬆️back_to_top_⬆️-white" alt="Back to top" title="Back to top"/>
  </a>
</p>
