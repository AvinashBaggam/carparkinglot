import pytest

from keyelements.src.allcars import Car
from keyelements.src.commands import commands
from keyelements.src.carparking import Parking



class TestClass:
    def test_parking_creation(self):
        
        parking = Parking()
        assert isinstance(parking, Parking)

    def test_invalid_commands(self):

        parking_lot = Parking()
        invalid_command = 'this is invalid command'
        assert commands(invalid_command, parking_lot) == 'invalid command'

    def test_add_car(self):
      
        num_plate = 'aa-aa-11'
        color = 'white'
        car = Car(num_plate, color)
        assert isinstance(car, Car)

    def test_parking_lot_creation(self):
        
        parking_lot = Parking()
        user_command = 'create_parking_lot 4'
        x = commands(user_command, parking_lot)
        assert x == 'Created a parking lot with 4 slots'

    def test_adding_car_to_parking_lot(self):
        
        parking_lot = Parking()
        user_commands = ['create_parking_lot 2', 'park mh-01-01 white', 'park ho']
        assert commands(user_commands[0], parking_lot) == 'Created a parking lot with 2 slots'
        assert commands(user_commands[1], parking_lot) == 'Allocated Slot Number: 1'
        assert commands(user_commands[2], parking_lot) == 'invalid arguments'

    def test_checking_status_of_parking_lot(self):
       
        parking_lot = Parking()
        user_commands = ['create_parking_lot 2', 'park mh-01-01 white', 'status', 'status kjs']
        assert commands(user_commands[0], parking_lot) == 'Created a parking lot with 2 slots'
        assert commands(user_commands[1], parking_lot) == 'Allocated Slot Number: 1'
        assert len(commands(user_commands[2], parking_lot)) > 0
        assert commands(user_commands[3], parking_lot) == 'please enter the right command'

    def test_check_leave_of_parking_lot(self):
        
        parking_lot = Parking()
        user_commands = ['create_parking_lot 2', 'park mh-01-01 white', 'park  a1-01-01 blue', 'leave 1', 'leave 101']
        assert commands(user_commands[0], parking_lot) == 'Created a parking lot with 2 slots'
        assert commands(user_commands[1], parking_lot) == 'Allocated Slot Number: 1'
        assert commands(user_commands[2], parking_lot) == 'Allocated Slot Number: 2'
        assert commands(user_commands[3], parking_lot) == 'slot number 1 is free'
        assert commands(user_commands[4], parking_lot) == 'invalid slot number: either empty or does not exit.'

    def test_check_registration_numbers_for_cars_with_colour(self):
       
        parking_lot = Parking()
        user_commands = ['create_parking_lot 5', 'park mh-01-01 white', 'park  a1-01-01 blue', 'park aa-bb-cc blue',
                         'park aa-ff-01 red', 'registration_numbers_for_cars_with_colour blue',
                         'registration_numbers_for_cars_with_colour purple']

        assert commands(user_commands[0], parking_lot) == 'Created a parking lot with 5 slots'
        assert commands(user_commands[1], parking_lot) == 'Allocated Slot Number: 1'
        assert commands(user_commands[2], parking_lot) == 'Allocated Slot Number: 2'
        assert commands(user_commands[3], parking_lot) == 'Allocated Slot Number: 3'
        assert commands(user_commands[4], parking_lot) == 'Allocated Slot Number: 4'
        assert commands(user_commands[5], parking_lot) == 'a1-01-01, aa-bb-cc'
        assert commands(user_commands[6], parking_lot) == 'Not Found'

    def test_slot_numbers_for_cars_with_colour(self):
       :
       
        parking_lot = Parking()
        user_commands = ['create_parking_lot 5', 'park mh-01-01 white', 'park  a1-01-01 blue', 'park aa-bb-cc blue',
                         'park aa-ff-01 red', 'slot_numbers_for_cars_with_colour blue',
                         'slot_numbers_for_cars_with_colour purple']
        assert commands(user_commands[0], parking_lot) == 'Created a parking lot with 5 slots'
        assert commands(user_commands[1], parking_lot) == 'Allocated Slot Number: 1'
        assert commands(user_commands[2], parking_lot) == 'Allocated Slot Number: 2'
        assert commands(user_commands[3], parking_lot) == 'Allocated Slot Number: 3'
        assert commands(user_commands[4], parking_lot) == 'Allocated Slot Number: 4'
        assert commands(user_commands[5], parking_lot) == '2, 3'
        assert commands(user_commands[6], parking_lot) == 'Not Found'

    def test_slot_number_for_registration_number(self):
        """ test the slot no of registration number"""

        parking_lot = Parking()
        user_commands = ['create_parking_lot 5', 'park mh-01-01 white', 'park  a1-01-01 blue', 'park aa-bb-cc blue',
                         'park aa-ff-01 red', 'slot_number_for_registration_number mh-01-01',
                         'slot_number_for_registration_number a-a-a']
        assert commands(user_commands[0], parking_lot) == 'Created a parking lot with 5 slots'
        assert commands(user_commands[1], parking_lot) == 'Allocated Slot Number: 1'
        assert commands(user_commands[2], parking_lot) == 'Allocated Slot Number: 2'
        assert commands(user_commands[3], parking_lot) == 'Allocated Slot Number: 3'
        assert commands(user_commands[4], parking_lot) == 'Allocated Slot Number: 4'
        assert commands(user_commands[5], parking_lot) == '1'
        assert commands(user_commands[6], parking_lot) == 'Not Found'

    def test_exit_condition(self):
        
        parking_lot = Parking()
        user_command = 'exit'

        with pytest.raises(SystemExit) as pytest_wrapped_e:
            commands(user_command, parking_lot)
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == 0
