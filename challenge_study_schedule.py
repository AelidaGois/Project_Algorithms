def study_schedule(p: list, target_time: int) -> int:
    if not isinstance(p, list) or not all(
        isinstance(i, tuple)
        and len(i) == 2
        and isinstance(i[0], int)
        and isinstance(i[1], int)
        for i in p
    ):
        return None
    if not isinstance(target_time, int):
        return None

    count = 0
    for i in p:
        if i[0] <= target_time <= i[1]:
            count += 1
    return count
