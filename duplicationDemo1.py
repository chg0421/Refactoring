class MissingPropertiesException(Exception):
    pass


def getTimes(**kargs):
    if ("interval" in kargs) == 0:
        raise MissingPropertiesException("monitor interval")
    value = kargs["interval"]

    if (value <= 0):
        raise MissingPropertiesException("monitor interval > 0")
    checkInterval = value

    if ("duration" in kargs) == 0:
        raise MissingPropertiesException("duration")
    value = kargs["duration"]
    if (value <= 0):
        raise MissingPropertiesException("duration > 0")
    if ((value % checkInterval) != 0):
        raise MissingPropertiesException("duration % checkInterval")
    monitorTime = value

    if ("departure" in kargs) == 0:
        raise MissingPropertiesException("departure offset")
    value = kargs["departure"]
    if (value <= 0):
        raise MissingPropertiesException("departure > 0")
    if ((value % checkInterval) != 0):
        raise MissingPropertiesException("departure % checkInterval")
    departureOffset = value

    result = []
    result.append(checkInterval)
    result.append(monitorTime)
    result.append(departureOffset)
    return result


if __name__ == "__main__":
    # print(getTimes(interval=10, duration=50, departure=12))
    print(getTimes(interval=10, duration=10, departure=20))
