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
`workouts` visualises progress in max weight and weight volume for every exercise you're performing from a specific data format you write after each exercise.

You record your exercises in `datasets/workouts/workouts.txt`:
```
YYYY-MM-DD hh:mm
  exercise1 WEIGHT SETSxREPS
  exercise2 WEIGHT SETSxREPS WEIGHT SETSxREPS

2023-04-13 17:30
  squat 80 4x12
  deadlift 70 1x12 80 2x5 90 1x3
```

And the workouts analysis tool in `analysis/workouts-analysis.py` draws the progress graph:

![](./img/squat.png)

# How I use it
While doing a workout, I write workouts in Google Keep on my phone.
Every so often I copy those notes into the `/datasets/workouts/workouts.txt` on my laptop and run the `/analysis/workouts-analysis.py` script.
Then I inspect the max weight and weight volume progress on particular exercises and adjust my future workouts to maintain the progress.

The goal is to keep progressively increasing volume and/or max weight.

## :chart_with_upwards_trend: analyse workout results
![](./img/bench.png)
![](./img/dead_lift.png)
![](./img/hip_thrust.png)
![](./img/squat.png)
## :shipit: installation
## :bulb: ideas for tests
## :question: usage
## future work

1. Show weekly strain for a particular muscle group.
1. Identify underworked muscles and suggest exercises for them.
1. Suggest exercises, weight, and number of sets and reps.

<p align="center">
  <a href="#">
    <img src="https://img.shields.io/badge/⬆️back_to_top_⬆️-white" alt="Back to top" title="Back to top"/>
  </a>
</p>
