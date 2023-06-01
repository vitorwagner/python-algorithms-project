def study_schedule(permanence_period, target_time):
    count = 0
    if type(target_time) != int:
        return None
    for i in range(len(permanence_period)):
        if type(permanence_period[i][0]) != int\
                or type(permanence_period[i][1]) != int:
            return None
        if permanence_period[i][0] <= target_time <= permanence_period[i][1]:
            count += 1
    return count
