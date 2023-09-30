import os
import sys
import argparse
import time
import colorama
import random
import user as fakeUser

# coloring
def color(color=None):
    global R, G, B, Y, V, L, W
    if color == "off":
        print("\t Coloring  is disabled ")
        R = G = Y = B = V = L = W = ""
    else:
        R, G, Y, B, V, L, W = (
            "\033[91m,",
            "\033[92m",
            "\033[93m",
            "\033[94m",
            "\033[95m",
            "\033[96m",
            "\033[0m",
        )
    return (R, G, Y, B, V, L, W)

# art banner
def art():
    print(
        """ %s
               _ _ _                  _           _ _ _ 
              |  -  \       _   | \  | |     _   | ---_|
              | | |  |    _| |  |  \ | |   _| |  ||  __
              | |- |    / _  |  | \ \| | / _  |  || |--| / _  \   %s
              | |  \ \  ||_| \  | |  | | ||_| \  | \_ || | |_||   %s
              |_|   \_\ \__ /\\  |_|  | | \__ /\\  \ __ | \_\__    %s                                     
       
        
          %s #Fake User Profiles and Names Generator
        """
        %(G, W, B, G, G)
    )

# error messaging
def error_Handler(errmsg):
    print(f"\t Usage: python {sys.argv[0]} -h for help\n")
    print("%s\t [?] Error: %s %s\n" % (R, errmsg, W))
    sys.exit()


# parse arguments
def argument_handler():
    parser = argparse.ArgumentParser("Random Name generator")
    parser.add_argument(
        "-g",
        "--gender",
        default='both',
        required=False,
        help='Pass in the gender option to specify the gender you want to generate names for ie. "-g  "female" or --gender "male" or --gender "f"',
    )
    parser.add_argument(
        "-o",
        "--output",
        default='names.txt',
        required=False,
        help='Pass in a the Output File Name To Save the Results if not provided the default file name will be used  ie: -o filename.js or --output test.txt ',
    )
    parser.add_argument(
        "-s",
        "--save",
        default = True,
        required=False,
        help='Pass in a save option to specify whether to save the file or not -s  ie: "-s  True or --save False',
    )
    parser.add_argument(
        "-n",
        "--number",
        default=100,
        required=False,
        help="Specify The Number of Names You Want To generate --n 20  or --number 200",
    )
   
    parser.add_argument(
        "-v",
        "--verbose",
        type=bool,
        default=True,
        required=False,
        help="Enable verbose mode to print to the screen while generating names :ie -v False or --verbose True",
    )
    parser.add_argument(
        "-p",
        "--profile",
        default=True,
        type=bool,
        required=False,
        help="Enable Profile Generator to include a fake user profile ie . -p yes or --profile off",
    )
    parser.add_argument(
        "-c",
        "--color",
        default="off",
        type=str,
        dest="color",
        required=False,
        help=" Disable coloring with -c ie . -c 'off' or --color 'on' ",
    )
    parser.add_argument(
        "-i",
        "--input",
        required=False,
        help='Pass in an Input File Name That Already contains the names using the format in names.py ie: -i custnamefiles.json or --i abc.txt ',
    )
    parser.error = error_Handler
    return parser.parse_args()


class Generator:
    def __init__(self,profile=False,
                 number=100,verbose=False,save=False,gender="",file_name="names.txt",
              male_first_names=[],male_surnames=[],female_first_names=[],female_surnames=[]):
        self.number = number
        self.time = time.time()
        self.verbose = verbose
        self.save = save
        self.gender = gender
        self.file_name = file_name
        self.male_first_names = male_first_names
        self.male_surnames = male_surnames
        self.female_first_names = female_first_names
        self.female_surnames= female_surnames
        self.final_list = []
        self.profile = profile

    def nameGenerator(self):

        if self.gender.lower().startswith('b') or self.gender.lower().startswith('m'):
            # Generate random names for Male
            male_names = []
            if self.verbose:
                print('%s\n\t\t [+] Generating Male names now...\n' %G)
            for _ in range(self.number):
                first_name = random.choice(self.male_first_names)
                last_name = random.choice(self.male_surnames) 
                
                if self.profile:
                    user =  fakeUser.userProfile(first_name,last_name)
                    male_names.append(user)
                    if self.verbose:
                        print(f"{user}")    
                else:
                    if self.verbose:
                        print(f"{first_name} {last_name}")               
                    male_names.append(f"{first_name} {last_name}")
                
            self.final_list.extend(male_names)

        if self.gender.lower().startswith('b') or self.gender.lower().startswith('f'):
            if self.verbose:
                print('%s\n\t\t [-] Generating female names now...\n'%B)

            # Generate random names for females
            female_names = []
            for _ in range(self.number):
                first_name = random.choice(self.female_first_names)
                last_name = random.choice(self.female_surnames)
        
                if self.profile:
                    user =  fakeUser.userProfile(first_name,last_name)
                    female_names.append(user)
                    if self.verbose:
                        print(f"{user}")    
                if not self.profile:
                    if self.verbose:
                        print(f"{first_name} {last_name}")               
                    female_names.append(f"{first_name} {last_name}")
                
            self.final_list.extend(female_names)        
        
        if self.verbose:
            time_diff = time.time() - self.time
            users = len(self.final_list)
            print('%s\n\t [!] Generated a total of %s users in %s seconds...\n'%(G,users,time_diff))
        
    # save results to a file
    def saveResults(self):
        if self.save:
            if self.verbose == True:
                print("%s\n\t [-] Saving Generated names to file %s \n" % (W,self.file_name))

            with open(str(self.file_name), "wt") as f:
                for name in self.final_list:
                    f.write("\n%s" % name)


def main():
    args = argument_handler()
    gender = args.gender
    file_name = args.output
    save = args.save
    number = args.number
    verbose = args.verbose
    profile = args.profile
    clr = args.color
    input_file = args.input
    
    # For coloring
    if sys.platform.startswith("win"):
        colorama.init()
    color(clr)
    art()
    from names import male_first_names,male_surnames,female_first_names,female_surnames
    action = Generator(profile=profile,number=number,verbose=verbose,save=save,gender=gender,file_name=file_name,
              male_first_names=male_first_names,male_surnames=male_surnames,female_first_names=female_first_names
              ,female_surnames=female_surnames)
    
    action.nameGenerator()
    if save:
        action.saveResults()
    print('%s\n\t [!] Process Completed Exiting...'%(W))

if __name__ == "__main__":
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")
    main()









