import unittest
import main


class TestMain(unittest.TestCase):

    # Requests outside our planning period are declined (Size=1)
    def test_requests_out_of_range(self):
        hotel = main.create_hotel(1)
        self.assertEqual(len(hotel), 1)

        result = main.booking_room(hotel, -4, 2)
        self.assertEqual(result, 'Declined')
        result = main.booking_room(hotel, 200, 400)
        self.assertEqual(result, 'Declined')

    # Requests are accepted (Size=3)
    def test_requests_accepted(self):
        hotel = main.create_hotel(3)
        self.assertEqual(len(hotel), 3)

        result = main.booking_room(hotel, 0, 5)
        self.assertEqual(result, 'Accepted')
        result = main.booking_room(hotel, 7, 13)
        self.assertEqual(result, 'Accepted')
        result = main.booking_room(hotel, 3, 9)
        self.assertEqual(result, 'Accepted')
        result = main.booking_room(hotel, 5, 7)
        self.assertEqual(result, 'Accepted')
        result = main.booking_room(hotel, 6, 6)
        self.assertEqual(result, 'Accepted')
        result = main.booking_room(hotel, 0, 4)
        self.assertEqual(result, 'Accepted')

    # Requests are declined (Size=3)
    def test_requests_declined_after_accept(self):
        hotel = main.create_hotel(3)
        self.assertEqual(len(hotel), 3)

        result = main.booking_room(hotel, 1, 3)
        self.assertEqual(result, 'Accepted')
        result = main.booking_room(hotel, 2, 5)
        self.assertEqual(result, 'Accepted')
        result = main.booking_room(hotel, 1, 9)
        self.assertEqual(result, 'Accepted')
        result = main.booking_room(hotel, 0, 15)
        self.assertEqual(result, 'Declined')

    # Requests can be accepted after a decline (Size=3)
    def test_requests_accepted_after_decline(self):
        hotel = main.create_hotel(3)
        self.assertEqual(len(hotel), 3)

        result = main.booking_room(hotel, 1, 3)
        self.assertEqual(result, 'Accepted')
        result = main.booking_room(hotel, 0, 15)
        self.assertEqual(result, 'Accepted')
        result = main.booking_room(hotel, 1, 9)
        self.assertEqual(result, 'Accepted')
        result = main.booking_room(hotel, 2, 5)
        self.assertEqual(result, 'Declined')
        result = main.booking_room(hotel, 4, 9)
        self.assertEqual(result, 'Accepted')

    # Complex Requests (Size=2)
    def test_complex_requests(self):
        hotel = main.create_hotel(2)
        self.assertEqual(len(hotel), 2)

        result = main.booking_room(hotel, 1, 3)
        self.assertEqual(result, 'Accepted')
        result = main.booking_room(hotel, 0, 4)
        self.assertEqual(result, 'Accepted')
        result = main.booking_room(hotel, 2, 3)
        self.assertEqual(result, 'Declined')
        result = main.booking_room(hotel, 5, 5)
        self.assertEqual(result, 'Accepted')
        result = main.booking_room(hotel, 4, 10)
        self.assertEqual(result, 'Accepted')
        result = main.booking_room(hotel, 10, 10)
        self.assertEqual(result, 'Accepted')
        result = main.booking_room(hotel, 6, 7)
        self.assertEqual(result, 'Accepted')
        result = main.booking_room(hotel, 8, 10)
        self.assertEqual(result, 'Declined')
        result = main.booking_room(hotel, 8, 9)
        self.assertEqual(result, 'Accepted')


if __name__ == '__main__':
    unittest.main()
