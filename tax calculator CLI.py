import platform
import subprocess
import sys, getopt
import time


def usage():
    print("\nParameters: -r/--regular\nUsage: -r is for normal bootup")
    print("This is a simple program for calculating tax based off a ATO taxtable from 2021")
    sys.exit()


def plsRun(argv):
    try:
        opts, args = getopt.getopt(argv, "hr", ["regular"])
        for opt, arg in opts:
            if opt in ['-h']:
                usage()
            elif opt in ['-r','--regular']:
                main()
                
                if system == 'Linux' or system == 'Darwin':
                    subprocess.run(['clear'])
                    main()
                elif system == 'Windows':
                    subprocess.run(['cmd.exe', '/c', 'cls'])
                    main()
                else:
                    print("Operating system unsupported, unable to clear terminal")
                    main()
    except:
        print("Invalid parameters supplied. See below for help:")
        usage()

def close():
    cont = input("Would you like to start the calculator again? [y/n]")
    if cont == 'y':
        main()
    else:
        print("Exiting system")
        shtdwn()

def shtdwn():
    system = platform.system()
    if system == 'Linux' or system == 'Darwin':
        subprocess.run(['clear'])
        sys.exit()
    elif system == 'Windows':
        subprocess.run(['cmd.exe', '/c', 'cls'])
        sys.exit()
    else:
        print("Operating system unsupported, unable to clear terminal")
        sys.exit()

def main():
    system = platform.system()
    if system == 'Linux' or system == 'Darwin':
        subprocess.run(['clear'])
    elif system == 'Windows':
        subprocess.run(['cmd.exe', '/c', 'cls'])
    else:
        print("Operating system unsupported, unable to clear terminal")
    print("Welcome to the finance calculator\n")
    response = input("Please select mode:\n1. Depreciation\n2. Interest\n3. Tax\n4. Exit\n")

    if response == '1':
        n_step = input("Do you know the current value of the item? [y/n] ").lower()
        if n_step == 'y':
            valid = False
            while not valid:
                try:
                    years = int(input("Please input the amount of years that the value has depreciated for: "))
                    val = int(input("Please input the original value: "))
                    cur = int(input("Please input current value: "))
                    result = (val - cur) / years
                    valid = True
                except ValueError:
                    print("One or more of these values are not integers")
            fl = input("Would you like the result to be rounded? [y/n] ").lower()
            if fl == "y":
                print("Value: ${:.2f}".format(result))
                print("Value decrease by " + str(result) + " per year")
                cont = input("Would you like to start the calculator again? [y/n] ")
                if cont == 'y':
                    main()
                else:
                    print("Exiting system")
                    shtdwn()
            elif fl == "n":
                print("Value: " + str(result))
                print("Value decrease by " + str(result) + " per year")
                cont = input("Would you like to start the calculator again? [y/n] ")
                if cont == 'y':
                    main()
                else:
                    print("Exiting system")
                    shtdwn()
            else:
                print("Error, not an option. Result will be displayed as rounded figure")
                # final = result-val
                # print("Result: ${:.2f}".format(final))
                print("Value: ${:.2f}".format(result))
                print("Value decrease by " + str(result) + " per year")
                cont = input("Would you like to start the calculator again? [y/n] ")
                if cont == 'y':
                    main()
                else:
                    print("Exiting system")
                    shtdwn()
        elif n_step == 'n': 
            valid = False
            while not valid:
                try:
                    years = int(input("Please input the amount of years that the value has depreciated for: "))
                    val = int(input("Please input the original value: "))
                    rate = int(input("Please input the depreciation rate: "))
                    valid = True
                except ValueError:
                    print("One or more of these values are not integers")
            rate = rate/100
            result = val-(years*(val*rate))
            fl = input("Would you like the result to be rounded? [y/n] ").lower()
            if fl == "y":
                final = val-result
                print("Result: ${:.2f}".format(result))
                print("Value: ${:.2f}".format(result))
                cont = input("Would you like to start the calculator again? [y/n] ")
                if cont == 'y':
                    main()
                else:
                    print("Exiting system")
                    shtdwn()
            elif fl == "n":
                print("Result: " + str(val-result))
                print("Value: " + str(result))
                cont = input("Would you like to start the calculator again? [y/n] ")
                if cont == 'y':
                    main()
                else:
                    print("Exiting system")
                    shtdwn()
            else:
                print("Error, not an option. Result will be displayed as rounded figure")
                final = val-result
                print("Result: ${:.2f}".format(final))
                print("Value: ${:.2f}".format(result))
                cont = input("Would you like to start the calculator again? [y/n] ")
                if cont == 'y':
                    main()
                else:
                    print("Exiting system")
                    shtdwn()
        else:
            print("Error, not an option")
            cont = input("Would you like to start the calculator again? [y/n]")
            if cont == 'y':
                main()
            else:
                print("Exiting system")
                shtdwn()
    elif response == '2': 
        cs = input("Would you like to calculate compound or simple interest? [c/s] ").lower()
        if cs == "c":
            valid = False
            while not valid:
                try:
                    rate = int(input("Please input the interest rate: "))
                    years = int(input("Please input the amount of years that the value is compounded for: "))
                    amount = int(input("Please input amount compounded per year: "))
                    val = int(input("Please input the original value: "))
                    valid = True
                except:
                    print("One or more of these values are not integers")
            percentage = rate/100
            result = val * (1 + percentage / amount) ** (years*amount)
            fl = input("Would you like the result to be rounded? [y/n] ").lower()
            if fl == "y":
                final = result-val
                print("Result: ${:.2f}".format(result))
                print("Amount gained: ${:.2f}".format(final))
                cont = input("Would you like to start the calculator again? [y/n] ")
                if cont == 'y':
                    main()
                else:
                    print("Exiting system")
                    shtdwn()
            elif fl == "n":
                print("Result: $" + str(result))
                print("Amount gained: $" + str(result-val))
                cont = input("Would you like to start the calculator again? [y/n] ")
                if cont == 'y':
                    main()
                else:
                    print("Exiting system")
                    shtdwn()
            else:
                print("Error, not an option. Result will be displayed as rounded figure")
                final = result-val
                print("Result: ${:.2f}".format(result))
                print("Amount gained: ${:.2f}".format(final))
                cont = input("Would you like to start the calculator again? [y/n] ")
                if cont == 'y':
                    main()
                else:
                    print("Exiting system")
                    shtdwn()
        if cs == "s":
            valid = False
            while not valid:
                try:
                    rate = input("Please input the interest rate: ")
                    years  = input("Please input the amount of years that the value gains interest for: ")
                    val = input("Please input the original value: ")
                    valid = True
                except:
                    print("One or more of these values are not integers")
            result = rate*years*val
            fl = input("Would you like the result to be rounded? [y/n] ").lower()
            if fl == "y":
                print("Result: ${:.2f}".format(result))
                print("Amount gained: ${:.2f}".format(result-val))
                cont = input("Would you like to start the calculator again? [y/n] ")
                if cont == 'y':
                    main()
                else:
                    print("Exiting system")
                    shtdwn()
            elif fl == "n":
                print("Result: $" + str(result))
                print("Amount gained: $" + str(result-val))
                cont = input("Would you like to start the calculator again? [y/n] ")
                if cont == 'y':
                    main()
                else:
                    print("Exiting system")
                    shtdwn()
            else:
                print("Error, not an option. Result will be displayed as rounded figure")
                print("Result: ${:.2f}".format(result))
                print("Amount gained: ${:.2f}".format(result-val))
                cont = input("Would you like to start the calculator again? [y/n] ")
                if cont == 'y':
                    main()
                else:
                    print("Exiting system")
                    shtdwn()
    elif response == "3":
        print("WARNING: THIS CALCULATOR HAS BEEN BUILT TO CALCULATE TAX THE AUSTRALIAN WAY, USE AT OWN RISK IN OTHER COUNTRIES, DOUBLE CHECK THE PROVIDED ANSWER")
        print("WARNING 2: THIS CALCULATOR IS USING TAX BRACKETS FROM 2020-2021")
        time.sleep(5)
        next = input("I understand the risks and will continue to use this calculator [y/n] ").lower()
        if next == 'y':
            pass
        else: 
            print("Exiting system")
            shtdwn()
        valid = False
        while not valid:
            try:
                grss_inc = int(input("Please input your gross annual income"))
                tax_ded = int(input("Please input the amount of tax deductible"))
                valid = True
            except:
                print("One or more of these values are not integers")
        new_inc = grss_inc-tax_ded 
        print(new_inc)
        if new_inc <= 18200:
            print("No tax needs to be paid")
            time.sleep(3)
            close()
        elif new_inc >= 18201 and new_inc <= 45000:
            taxable = new_inc-18200
            amount_tax = 0.19*taxable
            print("Amount required to be paid: " + amount_tax)
            close()
        elif new_inc >= 45001 and new_inc <= 120000:
            taxable = new_inc-45000
            amount_tax = 5092+(0.325*taxable)
            print("Amount required to be paid: " + amount_tax)
            close()
        elif new_inc >= 120001 and new_inc <= 180000:
            taxable = new_inc-120000
            amount_tax = 29467+(0.37*taxable)
            print("Amount required to be paid: " + amount_tax)
            close()
        elif new_inc >= 180001:
            taxable = new_inc-180000
            amount_tax = 29467+(0.45*taxable)
            print("Amount required to be paid: " + amount_tax)
            close()
    elif response == "4":
        print("Exiting system")
        shtdwn()
    else:
        print("Not an option")
        cont = input("Would you like to start the calculator again? [y/n]")
        if cont == 'y':
            main()
        else:
            print("Exiting system")
            shtdwn()


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("No parameter provided")
        usage()
    else:
        plsRun(sys.argv[1:])
