
def parse_version(version, is_msb):
    cte_version = 100
    if version > 199: cte_version = 1000
    if is_msb:
        return int(float(version) / cte_version)
    else:
        return int((float(version) % cte_version)/10)

def version_builder(major, minor, build):
    return str(major) + str(minor) + str(build)
