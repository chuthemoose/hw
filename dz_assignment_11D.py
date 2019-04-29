#------------------------------------------------------------------------------
# Assignment:    Assignment 11D
#
# Program Name:  dz_assignment_11D.py
#
# Purpose:       The purpose of this assignment is to familiarize you
#                with the writing Python scripts that demonstrates the usage
#                of Class Inheritance.
#
# Author:        Dominick Zarlenga
# Course:        192CIS115.600
#
# Created:       April 26, 2019
#------------------------------------------------------------------------------

# import class file
import dz_classEmployee_11D

# define globabls
TITLE = 'Shift Supervisor Information'
WIDTH = 100
HR = '-' * 110

# def main
def main():
    print()
    print(TITLE.center(WIDTH, ' '))
    print(HR)
    print('Name', 'ID Number'.rjust(32, ' '),
          'Current Salary'.rjust(32, ' '),
          'Bonus'.rjust(32, ' '))
    print(HR)

    # define employees and supervisors variables setting to appropiate classes
    employees = dz_classEmployee_11D.ProductionWorker
    supervisors = dz_classEmployee_11D.ShiftSupervisor

    # set initial loop variable
    continue_input = 'y'

    # begin looping asking user for emp name, ID, salary, and bonus.
    while continue_input == 'y':
        name = input('Enter the worker name: ')
        name_cla = employees.get_name
        emp_id = input('Enter ' + name + "'s ID number: ")
        id_cla = employees.get_id

        emp_salary = input('Enter ' + name + "'s salary: ")
        salary_cla = supervisors.set_salary
        emp_bonus = input('Enter ' + name + "'s bonus: ")
        bonus_cla = supervisors.set_bonus
        # display results of loop
        # ERROR: PROGRAM WILL FAIL CALLING get_salary
        # AND get_bonus. WILL TRY TO FIX.
        print(name, emp_id.rjust(22, ' '), '$'.rjust(29, ' '),
               '{:>7.2f}'.format(float(supervisors.get_salary())),
              '$'.rjust(29, ' '), '{:>7.2f}'.format(float(supervisors.get_bonus)))

        # prompt user to continue or end loop
        user_cont = input('Do you have another employee'
                          'to enter (y to continue): ')
        if user_cont != 'y':
            continue_input = 'n'




# call main function
main()