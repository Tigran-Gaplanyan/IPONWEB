import math


class CompanyError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class Company:
    def __init__(self, company_name, founded_at):
        if type(company_name) != str:
            raise CompanyError("Company_name should be a string:", company_name)
        if type(founded_at) != Date:
            raise CompanyError("Founded_at should be of a Date type:", founded_at)
        self.__company_name = company_name
        self.__founded_at = founded_at
        self.__employees_count = 0

    def __repr__(self):
        return "Company_name - {}, founded_at - {}, employees_count - {}".format(self.__company_name, self.__founded_at,
                                                                                                self.__employees_count)

    @property
    def company_name(self):
        return self.__company_name

    @company_name.setter
    def company_name(self, company_name):
        if type(company_name) != str:
            raise CompanyError("Company_name should be a string:", company_name)
        self.__company_name = company_name

    @property
    def founded_at(self):
        return self.__founded_at

    @founded_at.setter
    def founded_at(self, founded_at):
        if type(founded_at) != Date:
            raise CompanyError("Founded_at should be of type Date:", founded_at)
        self.__founded_at = founded_at


class JobError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class Job:
    def __init__(self, company, salary, experience_year, position):
        if type(company) != Company:
            raise JobError('company should be of type Company', company)
        if type(salary) != Money:
            raise JobError('salary should be of type Money', salary)
        if type(experience_year) != int:
            raise JobError('experience_year should be an int', experience_year)
        if type(position) != str:
            raise JobError('position should be an str', position)

        self.__company = company
        self.__salary = salary
        self.__experience_year = experience_year
        self.__position = position

    def __repr__(self):
        return "Company: {}, salary - {}, experience_year - {}, position - {}".format(self.__company, self.__salary,
                                                                                self.__experience_year, self.__position)

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, company):
        if type(company) != Company:
            raise JobError("company should be of type Company:", company)
        self.__company = company

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if type(salary) != Money:
            raise JobError("salary should be of type Money:", salary)
        self.__salary = salary

    @property
    def experience_year(self):
        return self.__experience_year

    @experience_year.setter
    def experience_year(self, experience_year):
        if type(experience_year) != int:
            raise JobError('experience_year should be an int', experience_year)
        self.__experience_year = experience_year

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if type(position) != str:
            raise JobError('position should be an str', position)
        self.__position = position

    def change_salary(self, salary):
        if type(salary) != Money:
            raise JobError("salary should be of type Money:", salary)
        self.__salary = salary

    def change_experience_year(self, experience_year):
        if type(experience_year) != int:
            raise JobError('experience_year should be an int', experience_year)
        self.__experience_year = experience_year

    def change_position(self, position):
        if type(position) != str:
            raise JobError('position should be an str', position)
        self.__position = position


class PersonError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class Person:
    def __init__(self, name, surname, gender, age, address):
        if type(name) != str:
            raise JobError('name should be an str', name)
        if type(surname) != str:
            raise JobError('surname should be an str', surname)
        if gender != 'Male' and gender != 'Female':
            raise PersonError('gender should be of type Male or Female', gender)
        if age < 0 and type(age) != int:
            raise PersonError('age should be positive int', age)
        if type(address) != str:
            raise JobError('address should be an str', address)

        self.__name = name
        self.__surname = surname
        self.__gender = gender
        self.__age = age
        self.__address = address
        self.__friends = []
        self.__job = []

    def __repr__(self):
        return "Name - {}, Surname - {}, Gender - {}, Age - {}, Address - {}, Friends - {}, Job: {}".format(self.__name,
                                self.__surname, self.__gender, self.__age, self.__address, self.__friends, self.__job)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) != str:
            raise JobError('name should be an str', name)
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if type(surname) != str:
            raise JobError('surname should be an str', surname)
        self.__surname = surname

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        if gender != 'Male' and gender != 'Female':
            raise PersonError('gender should be of type Male or Female', gender)
        self.__gender = gender

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0 and type(age) != int:
            raise PersonError('age should be positive int', age)
        self.__age = age

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        if type(address) != str:
            raise JobError('address should be an str', address)
        self.__address = address

    def add_friend(self, person):
        if type(person) == Person:
            self.__friends.append(person)
        else:
            raise PersonError("person should be of type Person", person)

    def remove_friend(self, person):
        if type(person) == Person:
            self.__friends.remove(person)
        else:
            raise PersonError("person should be of type Person", person)

    def add_job(self, job):
        if type(job) == Job:
            self.__job.append(job)
            job.company.employees_count += 1
        else:
            raise PersonError("job should be of type Job", job)

    def remove_job(self, job):
        if type(job) == Job:
            self.__job.remove(job)
            job.company.employees_count -= 1
        else:
            raise PersonError("job should be of type Job", job)

    def display_job(self):
        return self.__job


class DateError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class Date:
    def __init__(self, year, month, day):
        if type(year) != int:
            raise DateError("year should be an int", year)
        if type(month) != int or month < 1 or month > 12:
            raise DateError("month should be int between 1 and 12", month)
        if type(day) != int:
            raise DateError("day should be an int", day)
        if year < 1:
            raise DateError("year is out of range", year)
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day < 1 or day > 31:
                raise DateError('day should be between 1 and 31', day)
        elif month in [4, 6, 9, 11]:
            if day < 1 or day > 30:
                raise DateError('day should be between 1 and 30', day)
        elif month == 2:
            if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
                if day < 1 or day > 29:
                    raise DateError('day should be between 1 and 29', day)
            elif day < 1 or day > 28:
                    raise DateError('day should be between 1 and 28', day)

        self.__year = year
        self.__month = month
        self.__day = day

    def __repr__(self):
        return "{}.{}.{}".format(self.__day, self.__month, self.__year)

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if type(year) != int:
            raise DateError("year should be an int", year)
        self.__year = year

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        if type(month) != int:
            raise DateError("month should be int", month)
        self.__month = month

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if type(day) != int:
            raise DateError("day should be an int", day)
        self.__day = day

    def add_day(self, day):
        if type(day) == int:
            if self.month in [1, 3, 5, 7, 8, 10, 12]:
                if self.day + day > 31:
                    total = self.day + day
                    self.day += day
                    while total > 31:
                        if self.month in [1, 3, 5, 7, 8, 10, 12]:
                            if self.day > 31:
                                self.month += 1
                                self.day = self.day - 31
                        if self.month in [4, 6, 9, 11]:
                            if self.day > 30:
                                self.month += 1
                                self.day = self.day - 30
                        if self.month == 2:
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
                        total -= 31
                else:
                    self.day += day
            elif self.month in [4, 6, 9, 11]:
                if self.day + day > 30:
                    total = self.day + day
                    self.day += day
                    while total > 30:
                        if self.month in [1, 3, 5, 7, 8, 10, 12]:
                            if self.day > 31:
                                self.month += 1
                                self.day = self.day - 31
                        if self.month in [4, 6, 9, 11]:
                            if self.day > 30:
                                self.month += 1
                                self.day = self.day - 30
                        if self.month == 2:
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
                        total -= 30
                else:
                    self.day += day
            elif self.month == 2:
                if self.__is_leap_year():
                    if self.day + day > 29:
                        total = self.day + day
                        self.day += day
                        while total > 29:
                            if self.month in [1, 3, 5, 7, 8, 10, 12]:
                                if self.day > 31:
                                    self.month += 1
                                    self.day = self.day - 31
                            if self.month in [4, 6, 9, 11]:
                                if self.day > 30:
                                    self.month += 1
                                    self.day = self.day - 30
                            if self.month == 2:
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
                            total -= 29
                    else:
                        self.day += day
                else:
                    if self.day + day > 28:
                        total = self.day + day
                        self.day += day
                        while total > 28:
                            if self.month in [1, 3, 5, 7, 8, 10, 12]:
                                if self.day > 31:
                                    self.month += 1
                                    self.day = self.day - 31
                            if self.month in [4, 6, 9, 11]:
                                if self.day > 30:
                                    self.month += 1
                                    self.day = self.day - 30
                            if self.month == 2:
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
                            total -= 28
                    else:
                        self.day += day
            else:
                self.day += day

        else:
            raise DateError("day should be of type int", day)

    def add_month(self, month):
        if type(month) == int:
            if self.month + month > 12:
                total = self.month + month
                self.month += month
                while total > 12:
                    self.year += 1
                    self.month = self.month - 12
                    total -= 12
                if self.month in [4, 6, 9, 11]:
                    if self.day > 30:
                        self.day = 30
                elif self.month == 2:
                    if self.__is_leap_year():
                        if self.day > 29:
                            self.day = 29
                    else:
                        if self.day > 28:
                            self.day = 28
            else:
                self.month += month
                if self.month in [4, 6, 9, 11]:
                    if self.day > 30:
                        self.day = 30
                elif self.month == 2:
                    if self.__is_leap_year():
                        if self.day > 29:
                            self.day = 29
                    else:
                        if self.day > 28:
                            self.day = 28
        else:
            raise DateError("month should be of type int", month)

    def add_year(self, year):
        if type(year) == int:
            self.year += year
        else:
            raise DateError("year should be of type int", year)

    def __add__(self, other):
        if type(other) == Date:
            if type(other.year) == int:
                year = self.year + other.year
            else:
                raise DateTimeError("year should be of type int", other.year)
            if type(other.month) == int:
                month = self.month + other.month
            else:
                raise DateTimeError("month should be of type int", other.month)
            if type(other.day) == int:
                day = self.day + other.day
            if month in [1, 3, 5, 7, 8, 10, 12]:
                if day > 31:
                    total = day
                    while total > 31:
                        if month in [1, 3, 5, 7, 8, 10, 12]:
                            if day > 31:
                                month += 1
                                day = day - 31
                        if month in [4, 6, 9, 11]:
                            if day > 30:
                                month += 1
                                day = day - 30
                        if month == 2:
                            if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
                                if day > 29:
                                    month += 1
                                    day = day - 29
                            else:
                                if day > 28:
                                    month += 1
                                    day = day - 28
                        if month > 12:
                            year += month // 12
                            month = month % 12
                        total -= 31
            elif month in [4, 6, 9, 11]:
                if day > 30:
                    total = day
                    while total > 30:
                        if month in [1, 3, 5, 7, 8, 10, 12]:
                            if day > 31:
                                month += 1
                                day = day - 31
                        if month in [4, 6, 9, 11]:
                            if day > 30:
                                month += 1
                                day = day - 30
                        if month == 2:
                            if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
                                if day > 29:
                                    month += 1
                                    day = day - 29
                            else:
                                if day > 28:
                                    month += 1
                                    day = day - 28
                        if month > 12:
                            year += month // 12
                            month = month % 12
                        total -= 30
            elif month == 2:
                if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
                    if day > 29:
                        total = day
                        while total > 29:
                            if month in [1, 3, 5, 7, 8, 10, 12]:
                                if day > 31:
                                    month += 1
                                    day = day - 31
                            if month in [4, 6, 9, 11]:
                                if day > 30:
                                    month += 1
                                    day = day - 30
                            if month == 2:
                                if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
                                    if day > 29:
                                        month += 1
                                        day = day - 29
                                else:
                                    if day > 28:
                                        month += 1
                                        day = day - 28
                            if month > 12:
                                year += month // 12
                                month = month % 12
                            total -= 29
                else:
                    if day > 28:
                        total = day
                        while total > 28:
                            if month in [1, 3, 5, 7, 8, 10, 12]:
                                if day > 31:
                                    month += 1
                                    day = day - 31
                            if month in [4, 6, 9, 11]:
                                if day > 30:
                                    month += 1
                                    day = day - 30
                            if month == 2:
                                if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
                                    if day > 29:
                                        month += 1
                                        day = day - 29
                                else:
                                    if day > 28:
                                        month += 1
                                        day = day - 28
                            if month > 12:
                                year += month // 12
                                month = month % 12
                            total -= 28
            if month in [4, 6, 9, 11]:
                if day > 30:
                    day = 30
            elif month == 2:
                if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
                    if day > 29:
                        day = 29
                else:
                    if day > 28:
                        day = 28
            return Date(year, month, day)
        else:
            raise DateError("other should be of type Date", other)

    def __sub__(self, other):
        if type(other) == Date:
            if type(other.year) == int:
                year = self.year - other.year
            else:
                raise DateTimeError("year should be of type int", other.year)
            if type(other.month) == int:
                month = self.month - other.month
            else:
                raise DateTimeError("month should be of type int", other.month)
            if type(other.day) == int:
                day = self.day - other.day

            if day < 1:
                total = day
                while total < 1:
                    if month in [1, 3, 5, 7, 8, 10, 12]:
                        if day < 1:
                            month -= 1
                            day = day + 31
                    if month in [4, 6, 9, 11]:
                        if day < 1:
                            month -= 1
                            day = day + 30
                    if month == 2:
                        if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
                            if day < 1:
                                month -= 1
                                day = day + 29
                        else:
                            if day < 1:
                                month -= 1
                                day = day + 28
                    if month < 1:
                        year -= month // 12
                        month = month % 12
                    total += 31
            if month < 1:
                total = month
                while total < 1:
                    year -= 1
                    month = month + 12
                    total += 12
                if month in [4, 6, 9, 11]:
                    if day > 30:
                        day = 30
                elif month == 2:
                    if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
                        if day > 29:
                            day = 29
                    else:
                        if day > 28:
                            day = 28
            if month in [4, 6, 9, 11]:
                if day > 30:
                    day = 30
            elif month == 2:
                if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
                    if day > 29:
                        day = 29
                else:
                    if day > 28:
                        day = 28
            return Date(year, month, day)
        else:
            raise DateError("other should be of type Date", other)

    def __is_leap_year(self):
        if (self.year % 400 == 0) or (self.year % 100 != 0) and (self.year % 4 == 0):
            return True
        return False


date1 = Date(2022, 1, 31)
date2 = Date(1011, 1, 1)
# print(date1)
# print(date2)
# date1.add_day(29)
# date1.add_month(1)
# date1.add_year(2)
# print(date1 + date2)
# print(date1 - date2)
# print(date1)


class TimeError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class Time:
    def __init__(self, hour, minute, second):
        if type(hour) != int or hour < 0 or hour > 23:
            raise TimeError("hour should be an int between 0 and 23", hour)
        if type(minute) != int or minute < 0 or minute > 59:
            raise TimeError("minute should be an int between 0 and 59", minute)
        if type(second) != int or second < 0 or second > 59:
            raise TimeError("second should be an int between 0 and 59", second)

        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __repr__(self):
        if self.__hour == 0:
            return "0{}:{}:{}".format(self.__hour, self.__minute, self.__second)
        return "{}:{}:{}".format(self.__hour, self.__minute, self.__second)

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour):
        if type(hour) != int:
            raise TimeError("hour should be an int", hour)
        self.__hour = hour

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, minute):
        if type(minute) != int:
            raise TimeError("minute should be an int", minute)
        self.__minute = minute

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, second):
        if type(second) != int:
            raise TimeError("second should be an int", second)
        self.__second = second

    def add_hour(self, hour):
        if type(hour) == int:
            if self.__hour + hour >= 24:
                self.__hour = (self.__hour + hour) % 24
            else:
                self.__hour += hour
        else:
            raise TimeError("hour should be of type int", hour)

    def add_minute(self, minute):
        if type(minute) == int:
            if self.__minute + minute >= 60:
                self.__hour += (self.__minute + minute) // 60
                self.__minute = (self.__minute + minute) % 60
                if self.__hour >= 24:
                    self.__hour = self.__hour % 24
            else:
                self.__minute += minute
        else:
            raise TimeError("minute should be of type int", minute)

    def add_second(self, second):
        if type(second) == int:
            if self.__second + second >= 60:
                self.__minute += (self.__second + second) // 60
                self.__second = (self.__second + second) % 60
                if self.__minute >= 60:
                    self.__hour += self.__minute // 60
                    self.__minute = self.__minute % 60
                    if self.__hour >= 24:
                        self.__hour = self.__hour % 24
            else:
                self.__second += second
        else:
            raise TimeError("second should be of type int", second)

    def __add__(self, other):
        if type(other) == Time:
            if type(other.hour) == int:
                hour = self.hour + other.hour
            else:
                raise TimeError("hour should be of type int", other.hour)
            if type(other.minute) == int:
                minute = self.minute + other.minute
            else:
                raise TimeError("minute should be of type int", other.minute)
            if type(other.second) == int:
                second = self.second + other.second
            else:
                raise TimeError("second should be of type int", other.second)
            if second >= 60:
                total = second
                while total >= 60:
                    minute += 1
                    second = second - 60
                    total -= 60
            if minute >= 60:
                total = minute
                while total >= 60:
                    hour += 1
                    minute = minute - 60
                    total -= 60
            return Time(hour, minute, second)
        else:
            raise TimeError("other should be of type Time", other)

    def __sub__(self, other):
        if type(other) == Time:
            if type(other.hour) == int:
                hour = self.hour - other.hour
            else:
                raise TimeError("hour should be of type int", other.hour)
            if type(other.minute) == int:
                minute = self.minute - other.minute
            else:
                raise TimeError("minute should be of type int", other.minute)
            if type(other.second) == int:
                second = self.second - other.second
            else:
                raise TimeError("second should be of type int", other.second)
            if second < 0:
                total = second
                while total < 0:
                    minute -= 1
                    second = second + 60
                    total += 60
            if minute < 0:
                total = minute
                while total < 0:
                    hour -= 1
                    minute = minute + 60
                    total += 60
            return Time(hour, minute, second)
        else:
            raise TimeError("other should be of type Time", other)


time1 = Time(20, 30, 30)
time2 = Time(1, 35, 40)
# time1.add_hour(2)
# time1.add_minute(40)
# time1.add_second(45)
# print(time1 + time2)
# print(time1 - time2)
# print(time1)


class DateTimeError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class DateTime:
    def __init__(self, date, time):
        if type(date) != Date:
            raise DateTimeError("date should be of type Date", date)
        if type(time) != Time:
            raise DateTimeError("time should be of type Time", time)

        self.__date = date
        self.__time = time

    def __repr__(self):
        if self.__time.hour == 0:
            return "{}:{}:{} 0{}:{}:{}".format(self.__date.day, self.__date.month, self.__date.year, self.__time.hour,
                                              self.__time.minute, self.__time.second)
        return "{}:{}:{} {}:{}:{}".format(self.__date.day, self.__date.month, self.__date.year, self.__time.hour,
                                                                                self.__time.minute, self.__time.second)

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        if type(date) != Date:
            raise DateTimeError("date should be of type Date", date)
        self.__date = date

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time):
        if type(time) != Time:
            raise DateTimeError("time should be of type Time", time)
        self.__time = time

    def add_year(self, year):
        if type(year) == int:
            self.__date.year += year
        else:
            raise DateTimeError("year should be of type int", year)

    def add_month(self, month):
        if type(month) == int:
            if self.__date.month + month > 12:
                total = self.__date.month + month
                self.__date.month += month
                while total > 12:
                    self.__date.year += 1
                    self.__date.month = self.__date.month - 12
                    total -= 12
                if self.__date.month in [4, 6, 9, 11]:
                    if self.__date.day > 30:
                        self.__date.day = 30
                elif self.__date.month == 2:
                    if self.__is_leap_year():
                        if self.__date.day > 29:
                            self.__date.day = 29
                    else:
                        if self.__date.day > 28:
                            self.__date.day = 28
            else:
                self.__date.month += month
                if self.__date.month in [4, 6, 9, 11]:
                    if self.__date.day > 30:
                        self.__date.day = 30
                elif self.__date.month == 2:
                    if self.__is_leap_year():
                        if self.__date.day > 29:
                            self.__date.day = 29
                    else:
                        if self.__date.day > 28:
                            self.__date.day = 28
        else:
            raise DateTimeError("month should be of type int", month)

    def add_day(self, day):
        if type(day) == int:
            if self.__date.month in [1, 3, 5, 7, 8, 10, 12]:
                if self.__date.day + day > 31:
                    total = self.__date.day + day
                    self.__date.day += day
                    while total > 31:
                        if self.__date.month in [1, 3, 5, 7, 8, 10, 12]:
                            if self.__date.day > 31:
                                self.__date.month += 1
                                self.__date.day = self.__date.day - 31
                        if self.__date.month in [4, 6, 9, 11]:
                            if self.__date.day > 30:
                                self.__date.month += 1
                                self.__date.day = self.__date.day - 30
                        if self.__date.month == 2:
                            if self.__is_leap_year():
                                if self.__date.day > 29:
                                    self.__date.month += 1
                                    self.__date.day = self.__date.day - 29
                            else:
                                if self.__date.day > 28:
                                    self.__date.month += 1
                                    self.__date.day = self.__date.day - 28
                        if self.__date.month > 12:
                            self.__date.year += self.__date.month // 12
                            self.__date.month = self.__date.month % 12
                        total -= 31
                else:
                    self.__date.day += day
            elif self.__date.month in [4, 6, 9, 11]:
                if self.__date.day + day > 30:
                    total = self.__date.day + day
                    self.__date.day += day
                    while total > 30:
                        if self.__date.month in [1, 3, 5, 7, 8, 10, 12]:
                            if self.__date.day > 31:
                                self.__date.month += 1
                                self.__date.day = self.__date.day - 31
                        if self.__date.month in [4, 6, 9, 11]:
                            if self.__date.day > 30:
                                self.__date.month += 1
                                self.__date.day = self.__date.day - 30
                        if self.__date.month == 2:
                            if self.__is_leap_year():
                                if self.__date.day > 29:
                                    self.__date.month += 1
                                    self.__date.day = self.__date.day - 29
                            else:
                                if self.__date.day > 28:
                                    self.__date.month += 1
                                    self.__date.day = self.__date.day - 28
                        if self.__date.month > 12:
                            self.__date.year += self.__date.month // 12
                            self.__date.month = self.__date.month % 12
                        total -= 30
                else:
                    self.__date.day += day
            elif self.__date.month == 2:
                if self.__is_leap_year():
                    if self.__date.day + day > 29:
                        total = self.__date.day + day
                        self.__date.day += day
                        while total > 29:
                            if self.__date.month in [1, 3, 5, 7, 8, 10, 12]:
                                if self.__date.day > 31:
                                    self.__date.month += 1
                                    self.__date.day = self.__date.day - 31
                            if self.__date.month in [4, 6, 9, 11]:
                                if self.__date.day > 30:
                                    self.__date.month += 1
                                    self.__date.day = self.__date.day - 30
                            if self.__date.month == 2:
                                if self.__is_leap_year():
                                    if self.__date.day > 29:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 29
                                else:
                                    if self.__date.day > 28:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 28
                            if self.__date.month > 12:
                                self.__date.year += self.__date.month // 12
                                self.__date.month = self.__date.month % 12
                            total -= 29
                    else:
                        self.__date.day += day
                else:
                    if self.__date.day + day > 28:
                        total = self.__date.day + day
                        self.__date.day += day
                        while total > 28:
                            if self.__date.month in [1, 3, 5, 7, 8, 10, 12]:
                                if self.__date.day > 31:
                                    self.__date.month += 1
                                    self.__date.day = self.__date.day - 31
                            if self.__date.month in [4, 6, 9, 11]:
                                if self.__date.day > 30:
                                    self.__date.month += 1
                                    self.__date.day = self.__date.day - 30
                            if self.__date.month == 2:
                                if self.__is_leap_year():
                                    if self.__date.day > 29:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 29
                                else:
                                    if self.__date.day > 28:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 28
                            if self.__date.month > 12:
                                self.__date.year += self.__date.month // 12
                                self.__date.month = self.__date.month % 12
                            total -= 28
                    else:
                        self.__date.day += day
            else:
                self.__date.day += day
        else:
            raise DateTimeError("day should be of type int", day)

    def add_hour(self, hour):
        if type(hour) == int:
            if self.__time.hour + hour >= 24:
                total = self.__time.hour + hour
                self.__time.hour += hour
                while total >= 24:
                    self.__date.day += 1
                    self.__time.hour = self.__time.hour - 24
                    total -= 24
                if self.__date.month in [1, 3, 5, 7, 8, 10, 12]:
                    if self.__date.day > 31:
                        total = self.__date.day
                        while total > 31:
                            if self.__date.month in [1, 3, 5, 7, 8, 10, 12]:
                                if self.__date.day > 31:
                                    self.__date.month += 1
                                    self.__date.day = self.__date.day - 31
                            if self.__date.month in [4, 6, 9, 11]:
                                if self.__date.day > 30:
                                    self.__date.month += 1
                                    self.__date.day = self.__date.day - 30
                            if self.__date.month == 2:
                                if self.__is_leap_year():
                                    if self.__date.day > 29:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 29
                                else:
                                    if self.__date.day > 28:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 28
                            if self.__date.month > 12:
                                self.__date.year += self.__date.month // 12
                                self.__date.month = self.__date.month % 12
                            total -= 31
                elif self.__date.month in [4, 6, 9, 11]:
                    if self.__date.day > 30:
                        total = self.__date.day
                        while total > 30:
                            if self.__date.month in [1, 3, 5, 7, 8, 10, 12]:
                                if self.__date.day > 31:
                                    self.__date.month += 1
                                    self.__date.day = self.__date.day - 31
                            if self.__date.month in [4, 6, 9, 11]:
                                if self.__date.day > 30:
                                    self.__date.month += 1
                                    self.__date.day = self.__date.day - 30
                            if self.__date.month == 2:
                                if self.__is_leap_year():
                                    if self.__date.day > 29:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 29
                                else:
                                    if self.__date.day > 28:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 28
                            if self.__date.month > 12:
                                self.__date.year += self.__date.month // 12
                                self.__date.month = self.__date.month % 12
                            total -= 30
                elif self.__date.month == 2:
                    if self.__is_leap_year():
                        if self.__date.day > 29:
                            total = self.__date.day
                            while total > 29:
                                if self.__date.month in [1, 3, 5, 7, 8, 10, 12]:
                                    if self.__date.day > 31:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 31
                                if self.__date.month in [4, 6, 9, 11]:
                                    if self.__date.day > 30:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 30
                                if self.__date.month == 2:
                                    if self.__is_leap_year():
                                        if self.__date.day > 29:
                                            self.__date.month += 1
                                            self.__date.day = self.__date.day - 29
                                    else:
                                        if self.__date.day > 28:
                                            self.__date.month += 1
                                            self.__date.day = self.__date.day - 28
                                if self.__date.month > 12:
                                    self.__date.year += self.__date.month // 12
                                    self.__date.month = self.__date.month % 12
                                total -= 29
                    else:
                        if self.__date.day > 28:
                            total = self.__date.day
                            while total > 28:
                                if self.__date.month in [1, 3, 5, 7, 8, 10, 12]:
                                    if self.__date.day > 31:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 31
                                if self.__date.month in [4, 6, 9, 11]:
                                    if self.__date.day > 30:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 30
                                if self.__date.month == 2:
                                    if self.__is_leap_year():
                                        if self.__date.day > 29:
                                            self.__date.month += 1
                                            self.__date.day = self.__date.day - 29
                                    else:
                                        if self.__date.day > 28:
                                            self.__date.month += 1
                                            self.__date.day = self.__date.day - 28
                                if self.__date.month > 12:
                                    self.__date.year += self.__date.month // 12
                                    self.__date.month = self.__date.month % 12
                                total -= 28
            else:
                self.__time.hour += hour
        else:
            raise DateTimeError("hour should be of type int", hour)

    def add_minute(self, minute):
        if type(minute) == int:
            if self.__time.minute + minute >= 60:
                total = self.__time.minute + minute
                self.__time.minute += minute
                while total >= 60:
                    self.__time.hour += 1
                    self.__time.minute = self.__time.minute - 60
                    total -= 60
                if self.__time.hour >= 24:
                    total = self.__time.hour
                    while total >= 24:
                        self.__date.day += 1
                        self.__time.hour = self.__time.hour - 24
                        total -= 24
                if self.__date.month in [1, 3, 5, 7, 8, 10, 12]:
                    if self.__date.day > 31:
                        total = self.__date.day
                        while total > 31:
                            if self.__date.month in [1, 3, 5, 7, 8, 10, 12]:
                                if self.__date.day > 31:
                                    self.__date.month += 1
                                    self.__date.day = self.__date.day - 31
                            if self.__date.month in [4, 6, 9, 11]:
                                if self.__date.day > 30:
                                    self.__date.month += 1
                                    self.__date.day = self.__date.day - 30
                            if self.__date.month == 2:
                                if self.__is_leap_year():
                                    if self.__date.day > 29:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 29
                                else:
                                    if self.__date.day > 28:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 28
                            if self.__date.month > 12:
                                self.__date.year += self.__date.month // 12
                                self.__date.month = self.__date.month % 12
                            total -= 31
                elif self.__date.month in [4, 6, 9, 11]:
                    if self.__date.day > 30:
                        total = self.__date.day
                        while total > 30:
                            if self.__date.month in [1, 3, 5, 7, 8, 10, 12]:
                                if self.__date.day > 31:
                                    self.__date.month += 1
                                    self.__date.day = self.__date.day - 31
                            if self.__date.month in [4, 6, 9, 11]:
                                if self.__date.day > 30:
                                    self.__date.month += 1
                                    self.__date.day = self.__date.day - 30
                            if self.__date.month == 2:
                                if self.__is_leap_year():
                                    if self.__date.day > 29:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 29
                                else:
                                    if self.__date.day > 28:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 28
                            if self.__date.month > 12:
                                self.__date.year += self.__date.month // 12
                                self.__date.month = self.__date.month % 12
                            total -= 30
                elif self.__date.month == 2:
                    if self.__is_leap_year():
                        if self.__date.day > 29:
                            total = self.__date.day
                            while total > 29:
                                if self.__date.month in [1, 3, 5, 7, 8, 10, 12]:
                                    if self.__date.day > 31:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 31
                                if self.__date.month in [4, 6, 9, 11]:
                                    if self.__date.day > 30:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 30
                                if self.__date.month == 2:
                                    if self.__is_leap_year():
                                        if self.__date.day > 29:
                                            self.__date.month += 1
                                            self.__date.day = self.__date.day - 29
                                    else:
                                        if self.__date.day > 28:
                                            self.__date.month += 1
                                            self.__date.day = self.__date.day - 28
                                if self.__date.month > 12:
                                    self.__date.year += self.__date.month // 12
                                    self.__date.month = self.__date.month % 12
                                total -= 29
                    else:
                        if self.__date.day > 28:
                            total = self.__date.day
                            while total > 28:
                                if self.__date.month in [1, 3, 5, 7, 8, 10, 12]:
                                    if self.__date.day > 31:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 31
                                if self.__date.month in [4, 6, 9, 11]:
                                    if self.__date.day > 30:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 30
                                if self.__date.month == 2:
                                    if self.__is_leap_year():
                                        if self.__date.day > 29:
                                            self.__date.month += 1
                                            self.__date.day = self.__date.day - 29
                                    else:
                                        if self.__date.day > 28:
                                            self.__date.month += 1
                                            self.__date.day = self.__date.day - 28
                                if self.__date.month > 12:
                                    self.__date.year += self.__date.month // 12
                                    self.__date.month = self.__date.month % 12
                                total -= 28
            else:
                self.__time.minute += minute
        else:
            raise DateTimeError("minute should be of type int", minute)

    def add_second(self, second):
        if type(second) == int:
            if self.__time.second + second >= 60:
                total = self.__time.second + second
                self.__time.second += second
                while total >= 60:
                    self.__time.minute += 1
                    self.__time.second = self.__time.second - 60
                    total -= 60
                if self.__time.minute >= 60:
                    total = self.__time.minute
                    while total >= 60:
                        self.__time.hour += 1
                        self.__time.minute = self.__time.minute - 60
                        total -= 60
                    if self.__time.hour >= 24:
                        total = self.__time.hour
                        while total >= 24:
                            self.__date.day += 1
                            self.__time.hour = self.__time.hour - 24
                            total -= 24
                if self.__date.month in [1, 3, 5, 7, 8, 10, 12]:
                    if self.__date.day > 31:
                        total = self.__date.day
                        while total > 31:
                            if self.__date.month in [1, 3, 5, 7, 8, 10, 12]:
                                if self.__date.day > 31:
                                    self.__date.month += 1
                                    self.__date.day = self.__date.day - 31
                            if self.__date.month in [4, 6, 9, 11]:
                                if self.__date.day > 30:
                                    self.__date.month += 1
                                    self.__date.day = self.__date.day - 30
                            if self.__date.month == 2:
                                if self.__is_leap_year():
                                    if self.__date.day > 29:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 29
                                else:
                                    if self.__date.day > 28:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 28
                            if self.__date.month > 12:
                                self.__date.year += self.__date.month // 12
                                self.__date.month = self.__date.month % 12
                            total -= 31
                elif self.__date.month in [4, 6, 9, 11]:
                    if self.__date.day > 30:
                        total = self.__date.day
                        while total > 30:
                            if self.__date.month in [1, 3, 5, 7, 8, 10, 12]:
                                if self.__date.day > 31:
                                    self.__date.month += 1
                                    self.__date.day = self.__date.day - 31
                            if self.__date.month in [4, 6, 9, 11]:
                                if self.__date.day > 30:
                                    self.__date.month += 1
                                    self.__date.day = self.__date.day - 30
                            if self.__date.month == 2:
                                if self.__is_leap_year():
                                    if self.__date.day > 29:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 29
                                else:
                                    if self.__date.day > 28:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 28
                            if self.__date.month > 12:
                                self.__date.year += self.__date.month // 12
                                self.__date.month = self.__date.month % 12
                            total -= 30
                elif self.__date.month == 2:
                    if self.__is_leap_year():
                        if self.__date.day > 29:
                            total = self.__date.day
                            while total > 29:
                                if self.__date.month in [1, 3, 5, 7, 8, 10, 12]:
                                    if self.__date.day > 31:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 31
                                if self.__date.month in [4, 6, 9, 11]:
                                    if self.__date.day > 30:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 30
                                if self.__date.month == 2:
                                    if self.__is_leap_year():
                                        if self.__date.day > 29:
                                            self.__date.month += 1
                                            self.__date.day = self.__date.day - 29
                                    else:
                                        if self.__date.day > 28:
                                            self.__date.month += 1
                                            self.__date.day = self.__date.day - 28
                                if self.__date.month > 12:
                                    self.__date.year += self.__date.month // 12
                                    self.__date.month = self.__date.month % 12
                                total -= 29
                    else:
                        if self.__date.day > 28:
                            total = self.__date.day
                            while total > 28:
                                if self.__date.month in [1, 3, 5, 7, 8, 10, 12]:
                                    if self.__date.day > 31:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 31
                                if self.__date.month in [4, 6, 9, 11]:
                                    if self.__date.day > 30:
                                        self.__date.month += 1
                                        self.__date.day = self.__date.day - 30
                                if self.__date.month == 2:
                                    if self.__is_leap_year():
                                        if self.__date.day > 29:
                                            self.__date.month += 1
                                            self.__date.day = self.__date.day - 29
                                    else:
                                        if self.__date.day > 28:
                                            self.__date.month += 1
                                            self.__date.day = self.__date.day - 28
                                if self.__date.month > 12:
                                    self.__date.year += self.__date.month // 12
                                    self.__date.month = self.__date.month % 12
                                total -= 28
            else:
                self.__time.second += second
        else:
            raise TimeError("second should be of type int", second)

    def sub_year(self, year):
        if type(year) == int:
            self.__date.year -= year
        else:
            raise DateTimeError("year should be of type int", year)

    def sub_month(self, month):
        if type(month) == int:
            if self.__date.month - month < 1:
                total = self.__date.month - month
                self.__date.month -= month
                while total < 1:
                    self.__date.year -= 1
                    self.__date.month = self.__date.month + 12
                    total += 12
                if self.__date.month in [4, 6, 9, 11]:
                    if self.__date.day > 30:
                        self.__date.day = 30
                elif self.__date.month == 2:
                    if self.__is_leap_year():
                        if self.__date.day > 29:
                            self.__date.day = 29
                    else:
                        if self.__date.day > 28:
                            self.__date.day = 28
            else:
                self.__date.month -= month
                if self.__date.month in [4, 6, 9, 11]:
                    if self.__date.day > 30:
                        self.__date.day = 30
                elif self.__date.month == 2:
                    if self.__is_leap_year():
                        if self.__date.day > 29:
                            self.__date.day = 29
                    else:
                        if self.__date.day > 28:
                            self.__date.day = 28
        else:
            raise DateTimeError("month should be of type int", month)

    def sub_day(self, day):
        if type(day) == int:
            if self.__date.day - day < 1:
                total = self.__date.day - day
                self.__date.day -= day
                while total < 1:
                    if self.__date.month in [1, 3, 5, 7, 8, 10, 12]:
                        if self.__date.day < 1:
                            self.__date.month -= 1
                            self.__date.day = self.__date.day + 31
                    if self.__date.month in [4, 6, 9, 11]:
                        if self.__date.day < 1:
                            self.__date.month -= 1
                            self.__date.day = self.__date.day + 30
                    if self.__date.month == 2:
                        if self.__is_leap_year():
                            if self.__date.day < 1:
                                self.__date.month -= 1
                                self.__date.day = self.__date.day + 29
                        else:
                            if self.__date.day < 1:
                                self.__date.month -= 1
                                self.__date.day = self.__date.day + 28
                    if self.__date.month < 1:
                        self.__date.year -= self.__date.month // 12
                        self.__date.month = self.__date.month % 12
                    total += 31
                if self.__date.month < 1:
                    total = self.__date.month
                    while total < 1:
                        self.__date.year -= 1
                        self.__date.month = self.__date.month + 12
                        total += 12
                    if self.__date.month in [4, 6, 9, 11]:
                        if self.__date.day > 30:
                            self.__date.day = 30
                    elif self.__date.month == 2:
                        if self.__is_leap_year():
                            if self.__date.day > 29:
                                self.__date.day = 29
                        else:
                            if self.__date.day > 28:
                                self.__date.day = 28
                if self.__date.month in [4, 6, 9, 11]:
                    if self.__date.day > 30:
                        self.__date.day = 30
                elif self.__date.month == 2:
                    if self.__is_leap_year():
                        if self.__date.day > 29:
                            self.__date.day = 29
                    else:
                        if self.__date.day > 28:
                            self.__date.day = 28
            else:
                self.__date.day -= day
        else:
            raise DateTimeError("day should be of type int", day)

    def sub_hour(self, hour):
        if type(hour) == int:
            if self.__time.hour - hour < 0:
                total = self.__time.hour - hour
                self.__time.hour -= hour
                while total < 0:
                    self.__date.day -= 1
                    self.__time.hour = self.__time.hour + 24
                    total += 24
                if self.__date.day < 1:
                    total = self.__date.day
                    while total < 1:
                        if self.__date.month in [1, 3, 5, 7, 8, 10, 12]:
                            if self.__date.day < 1:
                                self.__date.month -= 1
                                self.__date.day = self.__date.day + 31
                        if self.__date.month in [4, 6, 9, 11]:
                            if self.__date.day < 1:
                                self.__date.month -= 1
                                self.__date.day = self.__date.day + 30
                        if self.__date.month == 2:
                            if self.__is_leap_year():
                                if self.__date.day < 1:
                                    self.__date.month -= 1
                                    self.__date.day = self.__date.day + 29
                            else:
                                if self.__date.day < 1:
                                    self.__date.month -= 1
                                    self.__date.day = self.__date.day + 28
                        if self.__date.month < 1:
                            self.__date.year -= self.__date.month // 12
                            self.__date.month = self.__date.month % 12
                        total += 31
                    if self.__date.month < 1:
                        total = self.__date.month
                        while total < 1:
                            self.__date.year -= 1
                            self.__date.month = self.__date.month + 12
                            total += 12
                        if self.__date.month in [4, 6, 9, 11]:
                            if self.__date.day > 30:
                                self.__date.day = 30
                        elif self.__date.month == 2:
                            if self.__is_leap_year():
                                if self.__date.day > 29:
                                    self.__date.day = 29
                            else:
                                if self.__date.day > 28:
                                    self.__date.day = 28
                    if self.__date.month in [4, 6, 9, 11]:
                        if self.__date.day > 30:
                            self.__date.day = 30
                    elif self.__date.month == 2:
                        if self.__is_leap_year():
                            if self.__date.day > 29:
                                self.__date.day = 29
                        else:
                            if self.__date.day > 28:
                                self.__date.day = 28
            else:
                self.__time.hour -= hour
        else:
            raise DateTimeError("hour should be of type int", hour)

    def sub_minute(self, minute):
        if type(minute) == int:
            if self.__time.minute - minute < 0:
                total = self.__time.minute - minute
                self.__time.minute -= minute
                while total < 0:
                    self.__time.hour -= 1
                    self.__time.minute = self.__time.minute + 60
                    total += 24
                if self.__time.hour < 0:
                    total = self.__time.hour
                    while total < 0:
                        self.__date.day -= 1
                        self.__time.hour = self.__time.hour + 24
                        total += 24
                if self.__date.day < 1:
                    total = self.__date.day
                    while total < 1:
                        if self.__date.month in [1, 3, 5, 7, 8, 10, 12]:
                            if self.__date.day < 1:
                                self.__date.month -= 1
                                self.__date.day = self.__date.day + 31
                        if self.__date.month in [4, 6, 9, 11]:
                            if self.__date.day < 1:
                                self.__date.month -= 1
                                self.__date.day = self.__date.day + 30
                        if self.__date.month == 2:
                            if self.__is_leap_year():
                                if self.__date.day < 1:
                                    self.__date.month -= 1
                                    self.__date.day = self.__date.day + 29
                            else:
                                if self.__date.day < 1:
                                    self.__date.month -= 1
                                    self.__date.day = self.__date.day + 28
                        if self.__date.month < 1:
                            self.__date.year -= self.__date.month // 12
                            self.__date.month = self.__date.month % 12
                        total += 31
                    if self.__date.month < 1:
                        total = self.__date.month
                        while total < 1:
                            self.__date.year -= 1
                            self.__date.month = self.__date.month + 12
                            total += 12
                        if self.__date.month in [4, 6, 9, 11]:
                            if self.__date.day > 30:
                                self.__date.day = 30
                        elif self.__date.month == 2:
                            if self.__is_leap_year():
                                if self.__date.day > 29:
                                    self.__date.day = 29
                            else:
                                if self.__date.day > 28:
                                    self.__date.day = 28
                    if self.__date.month in [4, 6, 9, 11]:
                        if self.__date.day > 30:
                            self.__date.day = 30
                    elif self.__date.month == 2:
                        if self.__is_leap_year():
                            if self.__date.day > 29:
                                self.__date.day = 29
                        else:
                            if self.__date.day > 28:
                                self.__date.day = 28
            else:
                self.__time.minute -= minute
        else:
            raise DateTimeError("minute should be of type int", minute)

    def sub_second(self, second):
        if type(second) == int:
            if self.__time.second - second < 0:
                total = self.__time.second - second
                self.__time.second -= second
                while total < 0:
                    self.__time.minute -= 1
                    self.__time.second = self.__time.second + 60
                    total += 60
                if self.__time.minute < 0:
                    total = self.__time.minute
                    while total < 0:
                        self.__time.hour -= 1
                        self.__time.minute = self.__time.minute + 60
                        total += 60
                    if self.__time.hour < 0:
                        total = self.__time.hour
                        while total < 0:
                            self.__date.day -= 1
                            self.__time.hour = self.__time.hour + 24
                            total += 24
                    if self.__date.day < 1:
                        total = self.__date.day
                        while total < 1:
                            if self.__date.month in [1, 3, 5, 7, 8, 10, 12]:
                                if self.__date.day < 1:
                                    self.__date.month -= 1
                                    self.__date.day = self.__date.day + 31
                            if self.__date.month in [4, 6, 9, 11]:
                                if self.__date.day < 1:
                                    self.__date.month -= 1
                                    self.__date.day = self.__date.day + 30
                            if self.__date.month == 2:
                                if self.__is_leap_year():
                                    if self.__date.day < 1:
                                        self.__date.month -= 1
                                        self.__date.day = self.__date.day + 29
                                else:
                                    if self.__date.day < 1:
                                        self.__date.month -= 1
                                        self.__date.day = self.__date.day + 28
                            if self.__date.month < 1:
                                self.__date.year -= self.__date.month // 12
                                self.__date.month = self.__date.month % 12
                            total += 31
                        if self.__date.month < 1:
                            total = self.__date.month
                            while total < 1:
                                self.__date.year -= 1
                                self.__date.month = self.__date.month + 12
                                total += 12
                            if self.__date.month in [4, 6, 9, 11]:
                                if self.__date.day > 30:
                                    self.__date.day = 30
                            elif self.__date.month == 2:
                                if self.__is_leap_year():
                                    if self.__date.day > 29:
                                        self.__date.day = 29
                                else:
                                    if self.__date.day > 28:
                                        self.__date.day = 28
                        if self.__date.month in [4, 6, 9, 11]:
                            if self.__date.day > 30:
                                self.__date.day = 30
                        elif self.__date.month == 2:
                            if self.__is_leap_year():
                                if self.__date.day > 29:
                                    self.__date.day = 29
                            else:
                                if self.__date.day > 28:
                                    self.__date.day = 28
            else:
                self.__time.second -= second
        else:
            raise TimeError("second should be of type int", second)

    def __add__(self, other):
        if type(other) == DateTime:
            if type(other.__date.year) == int:
                year = self.__date.year + other.__date.year
            else:
                raise DateTimeError("year should be of type int", other.__date.year)
            if type(other.__date.month) == int:
                month = self.__date.month + other.__date.month
            else:
                raise DateTimeError("month should be of type int", other.__date.month)
            if type(other.__date.day) == int:
                day = self.__date.day + other.__date.day
            else:
                raise DateTimeError("day should be of type int", other.__date.day)
            if type(other.__time.hour) == int:
                hour = self.__time.hour + other.__time.hour
            else:
                raise DateTimeError("hour should be of type int", other.__time.hour)
            if type(other.__time.minute) == int:
                minute = self.__time.minute + other.__time.minute
            else:
                raise DateTimeError("minute should be of type int", other.__time.minute)
            if type(other.__time.second) == int:
                second = self.__time.second + other.__time.second
            else:
                raise DateTimeError("second should be of type int", other.__time.second)
            if second >= 60:
                total = second
                while total >= 60:
                    minute += 1
                    second = second - 60
                    total -= 60
            if minute >= 60:
                total = minute
                while total >= 60:
                    hour += 1
                    minute = minute - 60
                    total -= 60
            if hour >= 24:
                total = hour
                while total >= 24:
                    day += 1
                    hour = hour - 24
                    total -= 24
            if month in [1, 3, 5, 7, 8, 10, 12]:
                if day > 31:
                    total = day
                    while total > 31:
                        if month in [1, 3, 5, 7, 8, 10, 12]:
                            if day > 31:
                                month += 1
                                day = day - 31
                        if month in [4, 6, 9, 11]:
                            if day > 30:
                                month += 1
                                day = day - 30
                        if month == 2:
                            if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
                                if day > 29:
                                    month += 1
                                    day = day - 29
                            else:
                                if day > 28:
                                    month += 1
                                    day = day - 28
                        if month > 12:
                            year += month // 12
                            month = month % 12
                        total -= 31
            elif month in [4, 6, 9, 11]:
                if day > 30:
                    total = day
                    while total > 30:
                        if month in [1, 3, 5, 7, 8, 10, 12]:
                            if day > 31:
                                month += 1
                                day = day - 31
                        if month in [4, 6, 9, 11]:
                            if day > 30:
                                month += 1
                                day = day - 30
                        if month == 2:
                            if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
                                if day > 29:
                                    month += 1
                                    day = day - 29
                            else:
                                if day > 28:
                                    month += 1
                                    day = day - 28
                        if month > 12:
                            year += month // 12
                            month = month % 12
                        total -= 30
            elif month == 2:
                if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
                    if day > 29:
                        total = day
                        while total > 29:
                            if month in [1, 3, 5, 7, 8, 10, 12]:
                                if day > 31:
                                    month += 1
                                    day = day - 31
                            if month in [4, 6, 9, 11]:
                                if day > 30:
                                    month += 1
                                    day = day - 30
                            if month == 2:
                                if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
                                    if day > 29:
                                        month += 1
                                        day = day - 29
                                else:
                                    if day > 28:
                                        month += 1
                                        day = day - 28
                            if month > 12:
                                year += month // 12
                                month = month % 12
                            total -= 29
                else:
                    if day > 28:
                        total = day
                        while total > 28:
                            if month in [1, 3, 5, 7, 8, 10, 12]:
                                if day > 31:
                                    month += 1
                                    day = day - 31
                            if month in [4, 6, 9, 11]:
                                if day > 30:
                                    month += 1
                                    day = day - 30
                            if month == 2:
                                if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
                                    if day > 29:
                                        month += 1
                                        day = day - 29
                                else:
                                    if day > 28:
                                        month += 1
                                        day = day - 28
                            if month > 12:
                                year += month // 12
                                month = month % 12
                            total -= 28
            if month in [4, 6, 9, 11]:
                if day > 30:
                    day = 30
            elif month == 2:
                if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
                    if day > 29:
                        day = 29
                else:
                    if day > 28:
                        day = 28
            date = Date(year, month, day)
            time = Time(hour, minute, second)
            return DateTime(date, time)
        else:
            raise DateTimeError("other should be of type DateTime", other)

    def __sub__(self, other):
        if type(other) == DateTime:
            if type(other.__date.year) == int:
                year = self.__date.year - other.__date.year
            else:
                raise DateTimeError("year should be of type int", other.__date.year)
            if type(other.__date.month) == int:
                month = self.__date.month - other.__date.month
            else:
                raise DateTimeError("month should be of type int", other.__date.month)
            if type(other.__date.day) == int:
                day = self.__date.day - other.__date.day
            else:
                raise DateTimeError("day should be of type int", other.__date.day)
            if type(other.__time.hour) == int:
                hour = self.__time.hour - other.__time.hour
            else:
                raise DateTimeError("hour should be of type int", other.__time.hour)
            if type(other.__time.minute) == int:
                minute = self.__time.minute - other.__time.minute
            else:
                raise DateTimeError("minute should be of type int", other.__time.minute)
            if type(other.__time.second) == int:
                second = self.__time.second - other.__time.second
            else:
                raise DateTimeError("second should be of type int", other.__time.second)
            if second < 0:
                total = second
                while total < 0:
                    minute -= 1
                    second = second + 60
                    total += 60
            if minute < 0:
                total = minute
                while total < 0:
                    hour -= 1
                    minute = minute + 60
                    total += 60
            if hour < 0:
                total = hour
                while total < 0:
                    day -= 1
                    hour = hour + 24
                    total += 24
            if day < 1:
                total = day
                while total < 1:
                    if month in [1, 3, 5, 7, 8, 10, 12]:
                        if day < 1:
                            month -= 1
                            day = day + 31
                    if month in [4, 6, 9, 11]:
                        if day < 1:
                            month -= 1
                            day = day + 30
                    if month == 2:
                        if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
                            if day < 1:
                                month -= 1
                                day = day + 29
                        else:
                            if day < 1:
                                month -= 1
                                day = day + 28
                    if month < 1:
                        year -= month // 12
                        month = month % 12
                    total += 31
                if month < 1:
                    total = month
                    while total < 1:
                        year -= 1
                        month = month + 12
                        total += 12
                    if month in [4, 6, 9, 11]:
                        if day > 30:
                            day = 30
                    elif month == 2:
                        if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
                            if day > 29:
                                day = 29
                        else:
                            if day > 28:
                                day = 28
                if month in [4, 6, 9, 11]:
                    if day > 30:
                        day = 30
                if month == 2:
                    if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
                        if day > 29:
                            day = 29
                    else:
                        if day > 28:
                            day = 28
            if month in [4, 6, 9, 11]:
                if day > 30:
                    day = 30
            elif month == 2:
                if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
                    if day > 29:
                        day = 29
                else:
                    if day > 28:
                        day = 28
            date = Date(year, month, day)
            time = Time(hour, minute, second)
            return DateTime(date, time)
        else:
            raise DateTimeError("other should be of type DateTime", other)

    def __is_leap_year(self):
        if (self.__date.year % 400 == 0) or (self.__date.year % 100 != 0) and (self.__date.year % 4 == 0):
            return True
        return False


datetime1 = DateTime(Date(2024, 5, 31), Time(22, 10, 55))
datetime2 = DateTime(Date(2004, 3, 30), Time(3, 20, 5))
# datetime1.add_year(2)
# datetime1.add_month(1)
# datetime1.add_day(31)
# datetime1.add_hour(6)
# datetime1.add_minute(55)
# datetime1.add_second(15)
# datetime2.sub_year(5)
# datetime2.sub_month(1)
# datetime2.sub_day(30)
# datetime2.sub_hour(4)
# datetime2.sub_minute(25)
# datetime2.sub_second(15)
# print(datetime1 + datetime2)
# print(datetime1 - datetime2)
# print(datetime1)
# print(datetime2)


class MoneyError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class Money:
    exchange = {'AMD': 1, 'RUB': 5.8, 'USD': 400, 'EUR': 430}

    def __init__(self, amount, currency):
        amount = float(amount)
        if type(amount) != float:
            raise MoneyError('amount should be of type float', amount)
        if type(currency) != str:
            raise MoneyError('currency should be of type str', currency)

        self.__amount = amount
        self.__currency = currency

    def __repr__(self):
        return "Amount: {}, currency - {}".format(self.__amount, self.__currency)

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        if type(amount) != float:
            raise MoneyError('amount should be of type float', amount)
        self.__amount = amount

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, currency):
        if type(currency) != str:
            raise MoneyError('currency should be of type str', currency)
        self.__currency = currency

    def conversation(self, other):
        if type(other) != Money:
            raise MoneyError("other should be of type Money", other)
        if self.__currency != other.__currency:
            if self.__currency == 'RUB':
                self.__amount = self.__amount * Money.exchange['RUB']
                self.currency = 'AMD'
            elif self.__currency == 'USD':
                self.__amount = self.__amount * Money.exchange['USD']
                self.currency = 'AMD'
            elif self.__currency == 'EUR':
                self.__amount = self.__amount * Money.exchange['EUR']
                self.currency = 'AMD'
            if other.__currency == 'RUB':
                other.__amount = other.__amount * Money.exchange['RUB']
                other.currency = 'AMD'
            elif other.__currency == 'USD':
                other.__amount = other.__amount * Money.exchange['USD']
                other.currency = 'AMD'
            elif other.__currency == 'EUR':
                other.__amount = other.__amount * Money.exchange['EUR']
                other.currency = 'AMD'

    def __add__(self, other):
        if type(other) != Money:
            raise MoneyError("other should be of type Money", other)
        self.conversation(other)
        return self.__class__(str(self.__amount + other.__amount), self.__currency)

    def __sub__(self, other):
        if type(other) != Money:
            raise MoneyError("other should be of type Money", other)
        self.conversation(other)
        return self.__class__(str(self.__amount - other.__amount), self.__currency)

    def __truediv__(self, other):
        if type(other) == Money:
            self.conversation(other)
            if other.amount == 0:
                raise MoneyError("cannot divide by 0", other.amount)
            return self.__class__(self.__amount / other.__amount, self.__currency)
        else:
            if other == 0:
                raise MoneyError("cannot divide by 0", other)
            self.__amount = self.__amount / other
            return self.__class__(self.__amount, self.__currency)

    def __eq__(self, other):
        if type(other) != Money:
            raise MoneyError("other should be of type Money", other)
        self.conversation(other)
        return self.__amount == other.__amount

    def __ne__(self, other):
        if type(other) != Money:
            raise MoneyError("other should be of type Money", other)
        self.conversation(other)
        return not self.__amount == other.__amount

    def __lt__(self, other):
        if type(other) != Money:
            raise MoneyError("other should be of type Money", other)
        self.conversation(other)
        return self.__amount < other.__amount

    def __gt__(self, other):
        if type(other) != Money:
            raise MoneyError("other should be of type Money", other)
        self.conversation(other)
        return self.__amount > other.__amount

    def __le__(self, other):
        if type(other) != Money:
            raise MoneyError("other should be of type Money", other)
        self.conversation(other)
        return self.__amount <= other.__amount

    def __ge__(self, other):
        if type(other) != Money:
            raise MoneyError("other should be of type Money", other)
        self.conversation(other)
        return self.__amount >= other.__amount


money1 = Money(10000, 'AMD')
money2 = Money(100, 'USD')
money3 = Money(7000, 'RUB')
money4 = Money(200, 'EUR')
money5 = Money(25, 'USD')
# money1.conversation(money2)
# print(money1.amount, money1.currency)
# print(money2.amount, money2.currency)
# money3.conversation(money4)
# print(money3.amount, money3.currency)
# print(money4.amount, money4.currency)
# print(money1 + money2)
# print(money4 - money3)
# print(money2 / money1)
# print(money1 / 2)
# print(money1 == money5)
# print(money2 != money3)
# print(money2 > money1)
# print(money3 < money4)
# print(money1 >= money3)
# print(money2 <= money4)


class MyRangeError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class MyRange:
    def __init__(self, current, end, step):
        if type(current) != int:
            raise MyRangeError('current should be of type int', current)
        if type(end) != int:
            raise MyRangeError('end should be of type int', end)
        if type(step) != int:
            raise MyRangeError('step should be of type int', step)
        if step == 0:
            raise MyRangeError('step cannot be 0', step)

        self.__current = current
        self.__end = end
        self.__step = step

    def __repr__(self):
        return "Current: {}, end - {}, step - {}".format(self.__current, self.__end, self.__step)

    @property
    def current(self):
        return self.__current

    @current.setter
    def current(self, current):
        if type(current) != int:
            raise MyRangeError('current should be of type int', current)
        self.__current = current

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, end):
        if type(end) != int:
            raise MyRangeError('end should be of type int', end)
        self.__end = end

    @property
    def step(self):
        return self.__step

    @step.setter
    def step(self, step):
        if type(step) != int:
            raise MyRangeError('step should be of type int', step)
        self.__step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current == self.__end:
            raise StopIteration
        self.current += self.__step
        return self.__current - self.__step

    def __len__(self):
        return math.ceil(abs(self.__end - self.__current) / abs(self.__step))

    def __getitem__(self, index):
        return self.__current + self.__step * index

    def __reversed__(self):
        return iter(MyRange(self.__end - self.__step, self.__current - self.__step, -1 * self.__step))


my_range = MyRange(5, 1, -1) # 5, 4, 3, 2
my_range2 = MyRange(1, 5, 1) # 1, 2, 3, 4
# iterator = iter(my_range)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(len(my_range))
# print(my_range[2])
# reversed = reversed(my_range)
# print(next(reversed))
# print(next(reversed))
# print(next(reversed))
# print(next(reversed))
# reversed = reversed(my_range2)
# print(next(reversed))
# print(next(reversed))
# print(next(reversed))
# print(next(reversed))


class DoctorError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class Doctor(Person):
    def __init__(self, name, surname, gender, age, address, department, profession, patronymic, salary):
        super().__init__(name, surname, gender, age, address)
        if type(department) != str:
            raise DoctorError('department should be of type str', department)
        if type(profession) != str:
            raise DoctorError('profession should be of type str', profession)
        if type(patronymic) != str:
            raise DoctorError('patronymic should be of type str', patronymic)
        if type(salary) != Money:
            raise DoctorError('salary should be of type Money', salary)

        self.__department = department
        self.__profession = profession
        self.__patronymic = patronymic
        self.__salary = salary

    def __repr__(self):
        return "Department - {}, profession - {}, patronymic - {}, salary - {}".format(self.__department,
                                                                    self.__profession, self.__patronymic, self.__salary)

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, department):
        if type(department) != str:
            raise DoctorError('department should be of type str', department)
        self.__department = department

    @property
    def profession(self):
        return self.__profession

    @profession.setter
    def profession(self, profession):
        if type(profession) != str:
            raise DoctorError('profession should be of type str', profession)
        self.__profession = profession

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, patronymic):
        if type(patronymic) != str:
            raise DoctorError('patronymic should be of type str', patronymic)
        self.__patronymic = patronymic

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if type(salary) != Money:
            raise DoctorError('salary should be of type Money', salary)
        self.__salary = salary


doctor = Doctor('Karen', 'Abgaryan', 'Male', 42, 'A', 'General Surgery', 'Surgeon', 'Vardanich', Money(300000, 'AMD'))
# print(doctor)


class CityError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class City:
    def __init__(self, name, mayor, population, language):
        if type(name) != str:
            raise CityError('name should be of type str', name)
        if type(mayor) != Person:
            raise CityError('mayor should be of type Person', mayor)
        if type(population) != int:
            raise CityError('population should be of type int', population)
        if type(language) != str:
            raise CityError('language should be of type str', language)

        self.__name = name
        self.__mayor = mayor
        self.__population = population
        self.__language = language

    def __repr__(self):
        return "Name: {}, mayor: {}, population - {}, language - {}".format(self.__name, self.__mayor,
                                                                                    self.__population, self.__language)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) != str:
            raise CityError('name should be of type str', name)
        self.__name = name

    @property
    def mayor(self):
        return self.__mayor

    @mayor.setter
    def mayor(self, mayor):
        if type(mayor) != Person:
            raise CityError('mayor should be of type Person', mayor)
        self.__mayor = mayor

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, population):
        if type(population) != int:
            raise CityError('population should be of type int', population)
        self.__population = population

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language):
        if type(language) != str:
            raise CityError('language should be of type str', language)
        self.__language = language


city = City('Paris', Person('Anne', 'Hidalgo', 'Female', 63, 'B'), 11142000, 'French')
# print(city)


class UniversityError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class University:
    def __init__(self, name, founded_at, rector, city):
        if type(name) != str:
            raise UniversityError('name should be of type str', name)
        if type(founded_at) != Date:
            raise UniversityError('founded_at should be of type Date', founded_at)
        if type(rector) != Person:
            raise UniversityError('rector should be of type Person', rector)
        if type(city) != City:
            raise UniversityError('city should be of type City', city)

        self.__name = name
        self.__founded_at = founded_at
        self.__rector = rector
        self.__city = city

    def __repr__(self):
        return "Name: {}, founded_at - {}, rector - {}, city - {}".format(self.__name, self.__founded_at,
                                                                                    self.__rector, self.__city)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) != str:
            raise UniversityError('name should be of type str', name)
        self.__name = name

    @property
    def founded_at(self):
        return self.__founded_at

    @founded_at.setter
    def founded_at(self, founded_at):
        if type(founded_at) != Date:
            raise UniversityError('founded_at should be of type Date', founded_at)
        self.__founded_at = founded_at

    @property
    def rector(self):
        return self.__rector

    @rector.setter
    def rector(self, rector):
        if type(rector) != Person:
            raise UniversityError('rector should be of type Person', rector)
        self.__rector = rector

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        if type(city) != City:
            raise UniversityError('city should be of type City', city)
        self.__city = city


university = University('Sorbonne', Date(1257, 9, 1), Person('Nathalie', 'Drach-Temam','Female', 56, 'C'), city)
# print(university)


class TeacherError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class Teacher(Person):
    def __init__(self, name, surname, gender, age, address, university, facultet, experience, start_work_at, subject, salary):
        super().__init__(name, surname, gender, age, address)
        if type(university) != University:
            raise TeacherError('university should be of type University', university)
        if type(facultet) != str:
            raise TeacherError('facultet should be of type str', facultet)
        if type(experience) != int:
            raise TeacherError('experience should be of type int', experience)
        if type(start_work_at) != Date:
            raise TeacherError('start_work_at should be of type Date', start_work_at)
        if type(subject) != str:
            raise TeacherError('subject should be of type str', subject)
        if type(salary) != Money:
            raise TeacherError('salary should be of type Money', salary)

        self.__university = university
        self.__facultet = facultet
        self.__experience = experience
        self.__start_work_at = start_work_at
        self.__subject = subject
        self.__salary = salary

    def __repr__(self):
        return "University - {}, facultet - {}, experience - {}, start_work_at - {}, subject - {}, salary - {}".format(self.__university,
                                self.__facultet, self.__experience, self.__start_work_at, self.__subject, self.__salary)

    @property
    def facultet(self):
        return self.__facultet

    @facultet.setter
    def facultet(self, facultet):
        if type(facultet) != str:
            raise TeacherError('facultet should be of type str', facultet)
        self.__facultet = facultet

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, experience):
        if type(experience) != int:
            raise TeacherError('experience should be of type int', experience)
        self.__experience = experience

    @property
    def start_work_at(self):
        return self.__start_work_at

    @start_work_at.setter
    def start_work_at(self, start_work_at):
        if type(start_work_at) != Date:
            raise TeacherError('start_work_at should be of type Date', start_work_at)
        self.__start_work_at = start_work_at

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject):
        if type(subject) != str:
            raise TeacherError('subject should be of type str', subject)
        self.__subject = subject

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if type(salary) != Money:
            raise TeacherError('salary should be of type Money', salary)
        self.__salary = salary


teacher = Teacher('Anahit', 'Karapetyan', 'Female', 46, 'D', university, 'History', 20, Date(2002, 9, 1), 'History of the World', Money(500, 'EUR'))
# print(teacher)


class StudentError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class Student(Person):
    def __init__(self, name, surname, gender, age, address, university, faculty, course, started_at):
        super().__init__(name, surname, gender, age, address)
        if type(university) != University:
            raise StudentError('university should be of type University', university)
        if type(faculty) != str:
            raise StudentError('faculty should be of type str', faculty)
        if type(course) != int:
            raise StudentError('course should be of type int', course)
        if type(started_at) != Date:
            raise StudentError('started_at should be of type Date', started_at)

        self.__university = university
        self.__faculty = faculty
        self.__course = course
        self.__started_at = started_at

    def __repr__(self):
        return "University - {}, faculty - {}, course - {}, started_at - {}".format(self.__university,
                                                                    self.__faculty, self.__course, self.__started_at)

    @property
    def university(self):
        return self.__university

    @university.setter
    def university(self, university):
        if type(university) != University:
            raise StudentError('university should be of type University', university)
        self.__university = university

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, faculty):
        if type(faculty) != str:
            raise StudentError('faculty should be of type str', faculty)
        self.__faculty = faculty

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, course):
        if type(course) != int:
            raise StudentError('course should be of type int', course)
        self.__course = course

    @property
    def started_at(self):
        return self.__started_at

    @started_at.setter
    def started_at(self, started_at):
        if type(started_at) != Date:
            raise StudentError('started_at should be of type Date', started_at)
        self.__started_at = started_at


student = Student('Meri', 'Grigoryan', 'Female', 18, 'E', university, 'Economics', 140, Date(2022, 9, 8))
# print(student)


def count(func):
    def inner(*args, **kwargs):
        inner.calls += 1
        return func(*args, **kwargs)
    inner.calls = 0
    return inner


@count
def square(x):
    return x ** 2


for i in range(3):
    square(2)


# print(square.calls)
