import datetime
from collections import defaultdict
from dataclasses import dataclass

from flota_app.models.car import Car
from flota_app.models.insurances.basic_insurance import BasicInsurance
from flota_app.models.insurances.insurance import Insurance
from flota_app.models.mots.basic_mot import BasicMot
from flota_app.models.mots.mot import Mot
from flota_app.repo.cars_repo import CarsRepo
from flota_app.repo.insurances_repo import BasicInsurancesRepo
from flota_app.repo.mots_repo import BasicMotsRepo


@dataclass(eq=False)
class CarsFleetService:
    """
    cars_repo: CarsRepo that will be providing data about cars in fleet
    basic_mots_repo: BasicMotsRepo that will be providing data about mots of cars in the fleet
    basic_insurances_repo: BasicInsurancesRepo that will be providing data about insurances of cars in the fleet
    """
    cars_repo: CarsRepo
    basic_mots_repo: BasicMotsRepo
    basic_insurances_repo: BasicInsurancesRepo

    def update_car(self, car: Car) -> Car:
        """
        Updates row that contains data about car
        :param car: Car object that will update
        :return: new updated Car (indicator that process succeeded)
        """
        return self.cars_repo.update(item_id=car.id, item=car)

    def update_cars(self, cars: list[Car]) -> list[Car]:
        """
        Updates rows that contain data about cars
        :param cars: list of Cars that user is willing to update
        :return: list of new updated Cars (indicator that process succeeded)
        """
        return self.cars_repo.update_many(cars)

    def add_car(self, car: Car) -> int:
        """
        Adds Car data into cars table
        :param car: Car object that will be inserted (id will be created by auto_increment mechanizm, so we can provide
        None as id.
        :return: id of new row in cars table created using Car data
        """
        return self.cars_repo.insert(car)

    def add_cars(self, cars: list[Car]) -> list[int]:
        """
        Adds multiple Cars into cars table
        :param cars: list of Cars objects that will be inserted (ids will be created by auto_increment mechanizm,
        so we can provide None as id
        :return: list of id of new rows in cars table created using Cars data
        """
        return self.cars_repo.insert_many(cars)

    def delete_car(self, car: Car) -> int:
        """
        Deletes row that have same id as provided Car object
        :param car: Car object that needs to be deleted from cars table
        :return: id of deleted car
        """
        return self.cars_repo.delete_one(car.id)

    def delete_cars(self, cars: list[Car]) -> list[int]:
        """
        Deletes rows that have same ids as provided Cars objects
        :param cars: list of Cars objects that needs to be deleted from cars table
        :return: list of ids of deleted cars
        """
        return self.cars_repo.delete_many(cars)

    def delete_car_by_id(self, car_id: int) -> None:
        """
        Deletes row in cars table that has same id as car_id attr
        :param car_id: id of deleted car
        :return: id of deleted car
        """
        return self.cars_repo.delete_one(car_id)

    def delete_cars_by_id(self, cars_ids: list[int]) -> None:
        """
        Deletes rows in cars table that have same ids as elements of cars_ids list
        :param cars_ids: list of ids of deleted cars
        :return: id of deleted car
        """
        return self.cars_repo.delete_many_by_id(cars_ids)

    def insurance_by_car_id(self, car_id: int) -> BasicInsurance:
        """
        Insurance that is linked to provided car_id
        :param car_id: id of car that is linked to insurance that user want to get
        :return: BasicInsurance object that is linked to that car
        """
        return [insurance for insurance in self.basic_insurances_repo.find_all() if insurance.car_id == car_id][0]

    def mot_by_car_id(self, car_id: int) -> BasicMot:
        """
        Mot that is linked to provided car_id
        :param car_id: id of car that is linked to mot that user want to get
        :return: BasicMot object that is linked to that car
        """
        return [mot for mot in self.basic_mots_repo.find_all() if mot.car_id == car_id][0]

    def insurance_deadline_by_car_id(self, car_id: int) -> datetime.date:
        """
        Deadline of insurance that is linked to car that has id of 'car_id'
        :param car_id: id of car that is linked to deadline that user want to get
        :return: deadline of insurance
        """
        return self.insurance_by_car_id(car_id).deadline()

    def mot_deadline_by_car_id(self, car_id: int) -> datetime.date:
        """
        Deadline of mot that is linked to car that has id of 'car_id'
        :param car_id: id of car that is linked to deadline that user want to get
        :return: deadline of insurance
        """
        return self.mot_by_car_id(car_id).deadline()

    def update_insurance(self, insurance: BasicInsurance) -> int:
        """
        Deletes old insurance and inserts new one
        :param insurance: BasicInsurance object that needs to be deleted from database table
        :return: id of newly created record
        """
        deleted_insurance = self.insurance_by_car_id(insurance.car_id)
        self.basic_insurances_repo.delete_one(deleted_insurance.id)
        return self.basic_insurances_repo.insert(insurance)

    def update_mot(self, mot: BasicMot) -> int:
        """
        Deletes old mot and inserts new one
        :param mot: BasicMot object that needs to be deleted from database table
        :return: id of newly created record
        """
        deleted_mot = self.mot_by_car_id(mot.car_id)
        self.basic_mots_repo.delete_one(deleted_mot.id)
        return self.basic_mots_repo.insert(mot)

    def cars_with_insurances_by_deadline(self) -> list[datetime.date, Insurance, Car]:
        """
        List of elements that have structure of: [insurance_deadline, BasicInsurance object, Car object]
        in ascending order. Handy when user want to generate list of insurances that needs to be renewed
        :return: list of lists that have deadline, insurance and car
        """
        deadlines_insurances_cars = defaultdict(list)
        cars = self.cars_repo.find_all()
        insurances = self.basic_insurances_repo.find_all()
        insurances.sort(key=lambda i: i.deadline())

        for insurance in insurances:
            deadlines_insurances_cars[insurance.car_id].extend([insurance.deadline(), insurance])

        for car in cars:
            deadlines_insurances_cars[car.id].append(car)

        return list(deadlines_insurances_cars.values())

    def cars_with_mots_by_deadline(self) -> list[datetime.date, Mot, Car]:
        """
        List of elements that have structure of: [mot_deadline, BasicMot object, Car object]
        in ascending order. Handy when user want to generate list of mots that needs to be renewed
        :return: list of lists that have deadline, mot and car
        """
        deadlines_mots_cars = defaultdict(list)
        cars = self.cars_repo.find_all()
        mots = self.basic_mots_repo.find_all()
        mots.sort(key=lambda i: i.deadline())

        for mot in mots:
            deadlines_mots_cars[mot.car_id].extend([mot.deadline(), mot])

        for car in cars:
            deadlines_mots_cars[car.id].append(car)

        return list(deadlines_mots_cars.values())

    def cars_with_insurances_and_mots_by_deadline(self) -> list[datetime.date, Insurance | Mot, Car]:
        """
        List of elements that have structure of:
            [mot_deadline or insurance_deadline, BasicMot or BasicInsurance object, Car object]
        in ascending order. Handy when user want to generate list of mots that needs to be renewed
        :return: list of lists that have deadline, mot or insurance and car
        """

        all_mots_and_insurances = self.cars_with_insurances_by_deadline()
        all_mots_and_insurances.extend(self.cars_with_mots_by_deadline())
        all_mots_and_insurances.sort(key=lambda data: data[0])  # data[0] is deadline

        return all_mots_and_insurances
