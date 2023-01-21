# Task 1
# Write a Python program to create a new dictionary by extracting the mentioned keys
# from the below dictionary.

def extract_keys(dict1, keys):
    new_dict = {k: dict1[k] for k in keys}
    return new_dict


# Task 2
# Get the key of a minimum value from the following dictionary.

def key_of_min_value(dict1):
    min_value = sorted(dict1.values())[0]
    return [key for key, value in dict1.items() if value == min_value]


# Task 3
# Write a Python program to copy the contents of a file to another file

def copy_contents(first_file, second_file):
    with open(first_file, 'r') as f1, open(second_file, 'w') as f2:
        for line in f1:
            f2.write(line)


# Task 4
# Write a Python program to count the frequency of words in a file

def frequency_of_words(file):
    dict1 = dict()
    with open(file, 'r') as f:
        words = f.read().replace(",", "").replace(".", "").lower().split()
        for word in words:
            if word in dict1:
                dict1[word] = dict1[word] + 1
            else:
                dict1[word] = 1
    return dict1


# Task 5
# Write a Python program to read last n lines of a file

def last_n_lines(file, n):
    with open(file, 'r') as f:
        f = f.readlines()
        for line in f[-n:]:
            print(line, end="")


# Task 6
# Finish class work, which you started in class.

class Company:
    def __init__(self, company_name, founded_at):
        self.company_name = company_name
        self.founded_at = founded_at
        self.employees_count = 0

    def __repr__(self):
        return "Company_name - {}, founded_at - {}, employees_count - {}".format(self.company_name, self.founded_at,
                                                                                                self.employees_count)


class Job:
    def __init__(self, company, salary, experience_year, position):
        if type(company) != Company:
            raise ValueError('company should be of type Company')

        self.company = company
        self.salary = salary
        self.experience_year = experience_year
        self.position = position

    def __repr__(self):
        return "Company: {}, salary - {}, experience_year - {}, position - {}".format(self.company, self.salary,
                                                                                self.experience_year, self.position)

    def change_salary(self, salary):
        self.salary = salary

    def change_experience_year(self, experience_year):
        self.experience_year = experience_year

    def change_position(self, position):
        self.position = position


class Person:
    def __init__(self, name, surname, gender, age, address):
        if gender != 'Male' and gender != 'Female':
            raise ValueError('gender should be of type Male or Female')
        if age < 0:
            raise ValueError('age should be positive')

        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.address = address
        self.friends = []
        self.job = []

    def __repr__(self):
        return "Name - {}, Surname - {}, Gender - {}, Age - {}, Address - {}, Friends - {}, Job: {}".format(self.name,
                                     self.surname, self.gender, self.age, self.address, self.friends, self.job)

    def add_friend(self, person):
        if type(person) == Person:
            self.friends.append(person)

    def remove_friend(self, person):
        if type(person) == Person:
            self.friends.remove(person)

    def add_job(self, job1):
        if type(job1) == Job:
            self.job.append(job1)
            job1.company.employees_count += 1

    def remove_job(self, job1):
        if type(job1) == Job:
            self.job.remove(job1)
            job1.company.employees_count -= 1

    def display_job(self):
        return self.job


# Task 7
# Write this classes

class Date:
    def __init__(self, year, month, day):
        for attribute in [year, month, day]:
            if type(attribute) != int:
                raise TypeError('year, month, and day must be `int`')
        if month < 1 or month > 12:
            raise ValueError('month should be between 1 and 12')
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day < 1 or day > 31:
                raise ValueError('day should be between 1 and 31')
        elif month in [4, 6, 9, 11]:
            if day < 1 or day > 30:
                raise ValueError('day should be between 1 and 30')
        elif month == 2:
            if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
                if day < 1 or day > 29:
                    raise ValueError('day should be between 1 and 29')
                elif day < 1 or day > 28:
                    raise ValueError('day should be between 1 and 28')

        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return "{}.{}.{}".format(self.day, self.month, self.year)

    def add_day(self, day):
        if type(day) == int:
            if self.month in [1, 3, 5, 7, 8, 10, 12]:
                if self.day + day > 31:
                    self.month += (self.day + day) // 31
                    self.day = (self.day + day) % 31
                    if self.month in [4, 6, 9, 11]:
                        if self.day > 30:
                            self.month += 1
                            self.day = self.day - 30
                    elif self.month == 2:
                        if self.__is_leap_year():
                            if self.day > 29:
                                self.month += 1
                                self.day = self.day - 29
                        else:
                            if self.day > 28:
                                self.month += 1
                                self.day = self.day - 28
                    if self.month > 12:
                        self.year += self.month // 12
                        self.month = self.month % 12
                else:
                    self.day += day
            elif self.month in [4, 6, 9, 11]:
                if self.day + day > 30:
                    self.month += (self.day + day) // 30
                    self.day = (self.day + day) % 30
                    if self.month > 12:
                        self.year += self.month // 12
                        self.month = self.month % 12
                else:
                    self.day += day
            elif self.month == 2:
                if self.__is_leap_year():
                    if self.day + day > 29:
                        self.month += (self.day + day) // 29
                        self.day = (self.day + day) % 29
                        if self.month > 12:
                            self.year += self.month // 12
                            self.month = self.month % 12
                    else:
                        self.day += day
                else:
                    if self.day + day > 28:
                        self.month += (self.day + day) // 28
                        self.day = (self.day + day) % 28
                        if self.month > 12:
                            self.year += self.month // 12
                            self.month = self.month % 12
                    else:
                        self.day += day
            else:
                self.day += day

        else:
            raise ValueError("day should be of type int")

    def add_month(self, month):
        if type(month) == int:
            if self.month + month > 12:
                self.year += (self.month + month) // 12
                self.month = (self.month + month) % 12
                if self.month in [4, 6, 9, 11]:
                    if self.day > 30:
                        self.month += 1
                        self.day = self.day - 30
                elif self.month == 2:
                    if self.__is_leap_year():
                        if self.day > 29:
                            self.month += 1
                            self.day = self.day - 29
                    else:
                        if self.day > 28:
                            self.month += 1
                            self.day = self.day - 28
            else:
                self.month += month
                if self.month in [4, 6, 9, 11]:
                    if self.day > 30:
                        self.month += 1
                        self.day = self.day - 30
                elif self.month == 2:
                    if self.__is_leap_year():
                        if self.day > 29:
                            self.month += 1
                            self.day = self.day - 29
                    else:
                        if self.day > 28:
                            self.month += 1
                            self.day = self.day - 28
        else:
            raise ValueError("month should be of type int")

    def add_year(self, year):
        if type(year) == int:
            self.year += year
        else:
            raise ValueError("year should be of type int")

    def __is_leap_year(self):
        if (self.year % 400 == 0) or (self.year % 100 != 0) and (self.year % 4 == 0):
            return True
        return False

class Time:
    def __init__(self, hour, minute, second):
        for attribute in [hour, minute, second]:
            if type(attribute) != int:
                raise TypeError('hour, minute, and second must be `int`')

        if hour < 0 or hour > 23:
            raise ValueError('hour should be between 0 and 23')
        if minute < 0 or minute > 59:
            raise ValueError('minute should be between 0 and 59')
        if second < 0 or second > 59:
            raise ValueError('second should be between 0 and 59')

        self.hour = hour
        self.minute = minute
        self.second = second

    def __repr__(self):
        return "{}:{}:{}".format(self.hour, self.minute, self.second)

    def add_hour(self, hour):
        if type(hour) == int:
            if self.hour + hour >= 24:
                self.hour = (self.hour + hour) % 24
            else:
                self.hour += hour
        else:
            raise ValueError("hour should be of type int")

    def add_minute(self, minute):
        if type(minute) == int:
            if self.minute + minute >= 60:
                self.hour += (self.minute + minute) // 60
                self.minute = (self.minute + minute) % 60
                if self.hour >= 24:
                    self.hour = self.hour % 24
            else:
                self.minute += minute
        else:
            raise ValueError("minute should be of type int")

    def add_second(self, second):
        if type(second) == int:
            if self.second + second >= 60:
                self.minute += (self.second + second) // 60
                self.second = (self.second + second) % 60
                if self.minute >= 60:
                    self.hour += self.minute // 60
                    self.minute = self.minute % 60
                    if self.hour >= 24:
                        self.hour = self.hour % 24
            else:
                self.second += second
        else:
            raise ValueError("second should be of type int")