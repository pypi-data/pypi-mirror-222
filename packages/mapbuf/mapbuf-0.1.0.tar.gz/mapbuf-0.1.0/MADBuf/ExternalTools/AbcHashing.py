import subprocess
from MADBuf.ExternalTools.AbcEnvironment import abc_environment

"""
===================== ABC =====================

1. downlaod ABC from github, and compile the binary executable
2. add ABC to the $PATH of the environment
"""


def run_abc_strash(filein: str, fileout: str = None, run_optimization: bool = False):
    tmp_filename = "/tmp/abc.log"

    command = f'abc -c "read_blif {filein}; strash;'

    if run_optimization:
        command += "compress2rs;"
        command += "compress2rs;"
        command += "compress2rs;"

    # placeholder for optimization
    command += "b;"

    if fileout == None:
        command += f'if -K 2; ps;" > {tmp_filename}'
    else:
        command += f'if -K 2; ps; write_hie {filein} {fileout};" > {tmp_filename}'

    with abc_environment():
        subprocess.run(command, shell=True)

    with open(tmp_filename, "r") as f:
        values: dict = {}
        for line in f.readlines():
            if "=" in line:
                data = line.split()
                for i in range(len(data)):
                    if data[i] == "=" and i != len(data) - 1:
                        try:
                            values[data[i - 1]] = int(data[i + 1])
                        except:
                            pass

    subprocess.run(f"rm -f {tmp_filename}", shell=True)
    return values
