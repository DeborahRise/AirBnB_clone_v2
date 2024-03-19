#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBaseModel
from models.place import Place
from models.city import City


class TestPlace(TestBaseModel):
    """ """

    data = {
        "Place.1f420db8-4b0c-4d05-9023-6b18e51b3124": {
            "__class__": "Place",
            "city_id": "4b457e66-c7c8-4f63-910f-fd91c3b7140b",
            "created_at": "2024-03-19T09:05:35.960466",
            "id": "1f420db8-4b0c-4d05-9023-6b18e51b3124",
            "latitude": 37.773972,
            "longitude": -122.431297,
            "max_guest": 6,
            "name": "Lovely place",
            "number_bathrooms": 1,
            "number_rooms": 3,
            "price_by_night": 120,
            "updated_at": "2024-03-19T09:05:35.960927",
            "user_id": "4f3f4b42-a4c3-4c20-a492-efff10d00c0b",
            "description": "This is a lovely place in San Francisco",
        }
    }

    def setUp(self):
        self.new = Place(
            **self.data["Place.1f420db8-4b0c-4d05-9023-6b18e51b3124"]
        )

    def test_city_id(self):
        """ """
        self.assertEqual(type(self.new.city_id), str)

    def test_user_id(self):
        """ """
        self.assertEqual(type(self.new.user_id), str)

    def test_name(self):
        """ """
        self.assertEqual(type(self.new.name), str)

    def test_description(self):
        """ """
        self.assertEqual(type(self.new.description), str)

    def test_number_rooms(self):
        """ """
        self.assertEqual(type(self.new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        self.assertEqual(type(self.new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        self.assertEqual(type(self.new.max_guest), int)

    def test_price_by_night(self):
        """ """
        self.assertEqual(type(self.new.price_by_night), int)

    def test_latitude(self):
        """ """
        self.assertEqual(type(self.new.latitude), float)

    def test_longitude(self):
        """ """
        self.assertEqual(type(self.new.latitude), float)

    # def test_amenity_ids(self):
    #     """ """
    #
    #     self.assertEqual(type(self.new.amenity_ids), list)
