def abbrevName(name):
    splitted= name.split()
    return f"{splitted[0].capitalize():.1s}.{splitted[1].capitalize():.1s}"
