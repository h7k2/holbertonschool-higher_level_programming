#!/usr/bin/python3
import os

def generate_invitations(template, attendees):

    if type(template) != str:
        print("bad template")
        return

    if type(attendees) != list:
        print("bad attendees")
        return

    if template == "" or template == " ":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for i in range(len(attendees)):
        t = template

        if type(attendees[i]) != dict:
            print("bad attendee")
            return

        try:
            n = attendees[i].get("name")
            if not n:
                n = "N/A"
        except:
            n = "N/A"

        try:
            e = attendees[i].get("event_title")
            if not e:
                e = "N/A"
        except:
            e = "N/A"

        try:
            d = attendees[i].get("event_date")
            if not d:
                d = "N/A"
        except:
            d = "N/A"

        try:
            l = attendees[i].get("event_location")
            if not l:
                l = "N/A"
        except:
            l = "N/A"

        try:
            t = t.replace("{name}", str(n))
            t = t.replace("{event_title}", str(e))
            t = t.replace("{event_date}", str(d))
            t = t.replace("{event_location}", str(l))
        except:
            pass

        file = "output_" + str(i+1) + ".txt"

        try:
            f = open(file, "w")
            f.write(t)
            f.close()
        except:
            print("cant write file")
