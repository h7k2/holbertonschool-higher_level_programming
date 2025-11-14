#!/usr/bin/python3
import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print(f"Invalid template type: expected str, got {type(template).__name__}")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Invalid attendees type: expected list of dictionaries.")
        return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    fields = ["name", "event_title", "event_date", "event_location"]

    for index, person in enumerate(attendees, start=1):
        text = template

        for field in fields:
            value = person.get(field)
            if value is None:
                value = "N/A"
            text = text.replace("{" + field + "}", str(value))

        filename = f"output_{index}.txt"

        try:
            if os.path.exists(filename):
                print(f"{filename} already exists, overwriting.")

            with open(filename, "w", encoding="utf-8") as f:
                f.write(text)
        except OSError as e:
            print(f"Error writing to {filename}: {e}")
