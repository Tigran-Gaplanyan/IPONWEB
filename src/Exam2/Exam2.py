from datetime import timedelta


class PatientError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class Patient:
    def __init__(self, name, surname, age, gender):
        if type(name) != str:
            raise PatientError('name should be an str', name)
        if type(surname) != str:
            raise PatientError('surname should be an str', surname)
        if 18 > age > 100 and type(age) != int:
            raise PatientError('age should be positive int', age)
        if gender != 'Male' and gender != 'Female':
            raise PatientError('gender should be of type Male or Female', gender)
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__gender = gender

    def __repr__(self):
        return "{}{} - {}, {} years old".format(self.__name, self.__surname, self.__gender, self.__age)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) != str:
            raise PatientError('name should be an str', name)
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if type(surname) != str:
            raise PatientError('surname should be an str', surname)
        self.__surname = surname

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        if gender != 'Male' and gender != 'Female':
            raise PatientError('gender should be of type Male or Female', gender)
        self.__gender = gender

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 18 > age > 100 and type(age) != int:
            raise PatientError('age should be positive int', age)
        self.__age = age

    def __ne__(self, other):
        if type(other) != Patient:
            raise PatientError("other should be of type Patient", other)
        if self.__name == other.__name and self.__surname == other.__surname and self.__age == other.__age and self.__gender == other.__gender:
            return False
        else:
            return True


class DoctorError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class Doctor:
    def __init__(self, name, surname, schedule):
        if type(name) != str:
            raise DoctorError('name should be an str', name)
        if type(surname) != str:
            raise DoctorError('surname should be an str', surname)
        if type(schedule) != dict:
            raise DoctorError('schedule should be of type dictionary', schedule)
        self.__name = name
        self.__surname = surname
        self.__schedule = schedule

    def __repr__(self):
        return "Doctor{}{} schedule {}(every pair from new line)".format(self.__name, self.__surname, self.__schedule)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) != str:
            raise DoctorError('name should be of type str', name)
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if type(surname) != str:
            raise DoctorError('surname should be of type str', surname)
        self.__surname = surname

    def is_free(self, datetime):
        d1 = datetime - timedelta(minutes=30)
        d2 = datetime + timedelta(minutes=30)
        for date in self.__schedule.keys():
            if date.hour == datetime.hour:
                if d1.minute < date < datetime.minute:
                    return False
                elif datetime.minute < date < d2.minute:
                    return False
        if datetime in self.__schedule:
            return False
        elif datetime.hour < 9 or datetime.hour > 6 or (datetime.hour > 1 and datetime.hour < 2):
            return False
        else:
            return True

    def is_registered(self, patient):
        if patient in self.__schedule.values():
            return True
        else:
            return False

    def register_patient(self, patient, datetime):
        if self.is_registered(patient):
            print("Patient {} already registered".format(patient))
        elif self.is_free(datetime):
            print("Datetime {} already taken from {} patient".format(datetime, patient))
        else:
            self.__schedule[datetime] = patient
            print("Patient {} successfully registered at {}".format(patient, datetime))


class ProductError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class Product:
    def __init__(self, price, id, quantity):
        if type(price) != int:
            raise ProductError('price should be an int', price)
        if type(id) != int:
            raise ProductError('id should be an int', id)
        if type(quantity) != int:
            raise ProductError('quantity should be an int', quantity)
        self.__price = price
        self.__id = id
        self.__quantity = quantity

    def __repr__(self):
        return "Price - {}, ID - {}, Quantity - {}".format(self.__price, self.__id, self.__quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if type(price) != int:
            raise ProductError('price should be of type int', price)
        self.__price = price

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if type(quantity) != int:
            raise ProductError('quantity should be of type int', quantity)
        self.__quantity = quantity

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if type(id) != int:
            raise ProductError('id should be of type int', id)
        self.__id = id

    def buy(self, count):
        if count > self.__quantity:
            raise ProductError('count of buying product is greater than quantity of the product', count)
        else:
            self.__quantity -= count


class InventoryError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class Inventory:
    def __init__(self, ids):
        if type(ids) != list:
            raise InventoryError('ids should be of type', ids)

        self.__ids = ids

    def __repr__(self):
        return "IDS - {}".format(self.__ids)

    def get_by_id(self, id):
        for product in self.__ids:
            if id == product.__id:
                return product

    def sum_of_products(self):
        sum = 0
        for product in self.__ids:
            sum += product.__quantity
        return sum


class PassengerError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class Passenger:
    def __init__(self, name, city, rooms):
        if type(name) != str:
            raise PassengerError('name should be an str', name)
        if type(city) != str:
            raise PassengerError('city should be an str', city)
        if type(rooms) != dict:
            raise PassengerError('rooms should be of type dictionary', rooms)
        self.__name = name
        self.__city = city
        self.__rooms = rooms

    def __repr__(self):
        return "Name - {}, City - {}, Rooms - {}".format(self.__name, self.__city, self.__rooms)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) != str:
            raise PassengerError('name should be of type str', name)
        self.__name = name

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        if type(city) != str:
            raise PassengerError('city should be of type str', city)
        self.__city = city

    @property
    def rooms(self):
        return self.__rooms

    @rooms.setter
    def rooms(self, rooms):
        if type(rooms) != dict:
            raise PassengerError('rooms should be of type dict', rooms)
        self.__rooms = rooms


class HotelError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class Hotel:
    def __init__(self, city, rooms):
        if type(city) != str:
            raise HotelError('city should be an str', city)
        if type(rooms) != dict:
            raise PassengerError('rooms should be of type dictionary', rooms)
        self.__city = city
        self.__rooms = rooms

    def __repr__(self):
        return "City - {}, Rooms - {}".format(self.__city, self.__rooms)

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        if type(city) != str:
            raise HotelError('city should be of type str', city)
        self.__city = city

    @property
    def rooms(self):
        return self.__rooms

    @rooms.setter
    def rooms(self, rooms):
        if type(rooms) != dict:
            raise PassengerError('rooms should be of type dict', rooms)
        self.__rooms = rooms

    def free_rooms_list(self, key):
        return self.__rooms[key]

    def reserve_rooms(self, key, count):
        if self.__rooms[key] < count:
            print("There is not so many free rooms")
        else:
            diff = self.__rooms[key] - count
            self.__rooms[key] = diff


def book():
    passenger  = Passenger("Gevorg", "Yerevan", {"Double": 2, "Single": 1, "Triple": 3})
    hotel = Hotel("Yerevan", {"Double": 2, "Single": 1, "Triple": 3})
    print(passenger)
    print(hotel)
    print(passenger.name)
    print(passenger.city)
    print(passenger.rooms)
    print(hotel.city)
    print(hotel.free_rooms_list("Double"))
    hotel.reserve_rooms("Double", 1)
    print(hotel.free_rooms_list("Double"))


book()