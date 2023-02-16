def study_schedule(permanence_period, target_time):
    sum_estudant_by_target_time = 0

    if target_time is None:
        return None

    for period in permanence_period:
        if (
            period[0] is None
            or period[1] is None
            or type(period[0]) == str
            or type(period[1]) == str
        ):
            return None
        elif period[0] <= target_time and period[1] >= target_time:
            sum_estudant_by_target_time += 1
    return sum_estudant_by_target_time


# print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 5))
