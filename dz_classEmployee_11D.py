#------------------------------------------------------------------------------
# Assignment:    Assignment 11D
#
# Program Name:  dz_classEmployee_11D.py
#
# Purpose:       The purpose of this assignment is to familiarize you
#                with the writing Python scripts that demonstrates the usage
#                of Class Inheritance.
#
# Author:        Dominick Zarlenga
# Course:        192CIS115.600
#
# Created:       April 29, 2019
#------------------------------------------------------------------------------

# define employee class
class Employee:
    # init and define employee name and employee id attributes
    def __init__(self, emp_name, emp_id):
        self.__emp_name = emp_name
        self.__emp_id = emp_id
    # return employe name and employe ID
    def set_name(self, emp_name):
        self.__emp_name = emp_name
    def get_name(self):
        return self.__emp_name
    def set_id(self, emp_id):
        self.__emp_id = emp_id
    def get_id(self):
        return self.__emp_id
# define ProductionWorker class passing the Employee class through it
class ProductionWorker(Employee):
    # init and define employee shift and employee pay
    def __init__(self, emp_name, emp_id, emp_shift, emp_pay):
        super().__init__(emp_name, emp_id)
        self.__emp_shift = emp_shift
        self.__emp_pay = emp_pay
    # return employee shift and employee pay
    def set_pay(self, emp_pay):
        self.__emp_pay = emp_pay
    def get_pay(self):
        return self.__emp_pay
    def set_shift(self, emp_shift):
        self.__emp_shift = emp_shift
    def get_shift(self):
        return self.__emp_shift
class ShiftSupervisor(Employee):
    def __init__(self, emp_name, emp_id, sup_salary, sup_bonus):
        super().__init__(emp_name, emp_id)
        self.__sup_salary = sup_salary
        self.__sup_bonus = sup_bonus
    def set_salary(self, sup_salary):
        self.__sup_salary = sup_salary
    def get_salary(self):
        return self.__sup_salary
    def set_bonus(self, sup_bonus):
        self.__sup_bonus = sup_bonus
    def get_bonus(self):
        return self.__sup_bonus

