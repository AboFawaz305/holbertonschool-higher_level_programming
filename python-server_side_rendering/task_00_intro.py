import os


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and a list of attendees.

    Args:
        template (str): The template string with placeholders.
        attendees (list): A list of dictionaries, each representing an attendee.
    """
    # 1. Check for invalid input types
    if not isinstance(template, str):
        print("Error: template is not a string.")
        return

    if not isinstance(attendees, list) or not all(
        isinstance(a, dict) for a in attendees
    ):
        print("Error: attendees is not a list of dictionaries.")
        return

    # 2. Check for empty inputs
    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. Process each attendee and generate files
    for i, attendee in enumerate(attendees):
        # Create a copy of the template for this attendee
        personalized_template = template

        # Define the placeholders to look for
        placeholders = ["{name}", "{event_title}", "{event_date}", "{event_location}"]

        # Process each placeholder
        for placeholder in placeholders:
            key = placeholder.strip("{}")  # Extract the key name (e.g., "name")
            value = attendee.get(key)  # Get the value from the dictionary

            # 4. Handle missing data
            if value is None or value == "":
                replacement = "N/A"
            else:
                replacement = str(value)

            personalized_template = personalized_template.replace(
                placeholder, replacement
            )

        # 5. Write the personalized content to a file
        output_filename = f"output_{i + 1}.txt"
        try:
            with open(output_filename, "w") as file:
                file.write(personalized_template)
            print(f"Generated {output_filename}")
        except IOError as e:
            print(f"Error writing to file {output_filename}: {e}")


# Example Main File to Test the Program:
if __name__ == "__main__":
    # Create a dummy template file for testing
    template_content = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team
"""
    with open("template.txt", "w") as file:
        file.write(template_content)

    # List of attendees
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

    # Call the function with the template and attendees list
    generate_invitations(template_content, attendees)
