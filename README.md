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
While doing a workout, you write workouts in your note taking mobile application of choice in a particular user-friendly format (see down). Every so often you manually copy those notes into the `/datasets/workouts/workouts.txt` and run the `/analysis/workouts-analysis.py`. That creates progress graphs per exercise in two formats; `volume[kg]/timestamp` and `max weight[kg]/timestamp`.

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
- connect exercises to muscle groups
- calculate strain on all muscles per exercise
    - e.g. barbell bench press wide grip
        - pectoral muscle 60% of the weight
        - triceps 20% of the weight
- create graph: volume per muscle
- create graph: max weight (personal best) per muscle
- suggest exercises that need to be done so that all muscle groups are exercised
- calculate how much weight and sets/reps need to be lifted per exercise
<p align="center">
  <a href="#">
    <img src="https://img.shields.io/badge/⬆️back_to_top_⬆️-white" alt="Back to top" title="Back to top"/>
  </a>
</p>
