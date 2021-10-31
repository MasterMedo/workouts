from collections import defaultdict


names = [
        'target',
        'synergist',
        'stabilizer',
        'dynamic stabilizer',
        'antagonist stabilizer'
]
percentages = {
        names[0]: 75 * 0.01,
        names[1]: 50 * 0.01,
        names[2]: 5 * 0.01,
        names[3]: 1 * 0.01,
        names[4]: 1 * 0.01
}


def formula(exercise, custom_perc=dict()):
    muscle_perc = defaultdict(int)

    for name in names:

        for muscle in exercise[name]:
            if muscle in custom_perc:
                if muscle_perc[muscle] == 0:
                    muscle_perc[muscle] += custom_perc[name]
            else:
                muscle_perc[muscle] += percentages[name]

    return muscle_perc
