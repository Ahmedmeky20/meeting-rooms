import unittest
from main import minimum_meeting_rooms


class TestMeetingRooms(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(minimum_meeting_rooms([]), 0)

    def test_one_meeting(self):
        self.assertEqual(minimum_meeting_rooms([("09:00", "10:00")]), 1)

    def test_no_overlap(self):
        meetings = [("09:00", "10:00"), ("10:00", "11:00")]
        self.assertEqual(minimum_meeting_rooms(meetings), 1)

    def test_all_overlap(self):
        meetings = [("09:00", "11:00"), ("09:30", "10:30"), ("10:00", "12:00")]
        self.assertEqual(minimum_meeting_rooms(meetings), 3)

    def test_sample_data(self):
        meetings = [
            ("09:00", "10:00"), ("09:30", "11:00"),
            ("10:00", "11:30"), ("11:00", "12:00"),
            ("11:15", "12:15")
        ]
        self.assertEqual(minimum_meeting_rooms(meetings), 2)

    def test_unsorted_input(self):
        meetings = [("11:00", "12:00"), ("09:00", "10:00"), ("09:30", "11:30")]
        self.assertEqual(minimum_meeting_rooms(meetings), 2)

    def test_touching_endpoints(self):
        meetings = [("09:00", "10:00"), ("10:00", "11:00"), ("11:00", "12:00")]
        self.assertEqual(minimum_meeting_rooms(meetings), 1)

    def test_multiple_overlaps(self):
        meetings = [
            ("09:00", "12:00"), ("09:30", "10:30"),
            ("10:00", "11:00"), ("11:00", "13:00")
        ]
        self.assertEqual(minimum_meeting_rooms(meetings), 3)

    def test_same_start_time(self):
        meetings = [("09:00", "10:00"), ("09:00", "11:00")]
        self.assertEqual(minimum_meeting_rooms(meetings), 2)


if __name__ == "__main__":
    unittest.main()