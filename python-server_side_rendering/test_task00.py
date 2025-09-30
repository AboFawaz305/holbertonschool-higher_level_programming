import unittest

generate_invitations = __import__("task_00_intro").generate_invitations


class TestGenerateInvitations(unittest.TestCase):
    def test_it_works(self):
        template = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team"""
        attendees = [
            {
                "name": "Alice",
                "event_title": "Python Conference",
                "event_date": "2023-07-15",
                "event_location": "New York",
            },
            {
                "name": "Bob",
                "event_title": "Data Science Workshop",
                "event_date": "2023-08-20",
                "event_location": "San Francisco",
            },
            {
                "name": "Charlie",
                "event_title": "AI Summit",
                "event_date": None,
                "event_location": "Boston",
            },
        ]
        print(generate_invitations(template, attendees))
