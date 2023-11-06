import json
from typing import List, Dict, Union

class Person:
    def __init__(self, name: str):
        """Initialisiert eine Person mit einem Namen."""
        self.name = name

    def introduce(self) -> str:
        """Gibt eine Begrüßungsnachricht zurück."""
        return f"Hallo, mein Name ist {self.name}"

class Student(Person):
    def __init__(self, name: str, reason_to_attend: str):
        """
        Initialisiert einen Studenten mit einem Namen und einem Grund zur Teilnahme.

        Args:
            name (str): Der Name des Studenten.
            reason_to_attend (str): Der Grund zur Teilnahme.
        """
        super().__init__(name)
        self.reason_to_attend = reason_to_attend

class Dozent(Person):
    def __init__(self, name: str, biography: str):
        """
        Initialisiert einen Dozenten mit einem Namen und einer Biografie.

        Args:
            name (str): Der Name des Dozenten.
            biography (str): Die Biografie des Dozenten.
        """
        super().__init__(name)
        self.biography = biography
        self.skills: List[str] = []  # Liste der Fertigkeiten des Dozenten

    def add_skill(self, *skill: str):
        """
        Fügt eine Fertigkeit zur Liste der Fertigkeiten des Dozenten hinzu.

        Args:
            skill (str): Die hinzuzufügende Fertigkeit.
        """
        self.skills.append(skill)

class Workshop:
    def __init__(self, start_date: str, end_date: str, theme: str):
        """
        Initialisiert einen Workshop mit Start- und Enddatum sowie einem Thema.

        Args:
            start_date (str): Das Startdatum des Workshops.
            end_date (str): Das Enddatum des Workshops.
            theme (str): Das Thema des Workshops.
        """
        self.start_date = start_date
        self.end_date = end_date
        self.theme = theme
        self.dozents: List[Dozent] = []  # Liste der Dozenten des Workshops
        self.students: List[Student] = []  # Liste der Studenten des Workshops

    def add_participants(self, *people: Union[Dozent, Student]):
        """
        Fügt Personen (Dozenten oder Studenten) zum Workshop hinzu.

        Args:
            people (Union[Dozent, Student]): Die hinzuzufügenden Personen.
        """
        for person in people:
            if isinstance(person, Dozent):
                self.dozents.append(person)
            elif isinstance(person, Student):
                self.students.append(person)
            
    def get_participant_data(self):
        """
        Gibt Informationen über die Teilnehmer des Workshops zurück.

        Returns:
            Dict: Informationen über die Teilnehmer des Workshops.
        """
        participants = {
            "Students": [student.__dict__ for student in self.students],
            "Dozents": [dozent.__dict__ for dozent in self.dozents]
        }
        return participants
    
def print_members(students: List[Student], dozents: List[Dozent], filename: str):
    """
    Speichert Informationen über Studenten und Dozenten in einer JSON-Datei.

    Args:
        students (List[Student]): Liste der Studenten.
        dozents (List[Dozent]): Liste der Dozenten.
        filename (str): Der Name der Ausgabedatei.
    """
    members = {
        "Students": [student.__dict__ for student in students],
        "Dozents": [dozent.__dict__ for dozent in dozents]
    }
    with open(filename, 'w') as file:
        json.dump(members, file, indent=4)

def print_workshops(workshops: List[Workshop], filename: str):
    """
    Speichert Informationen über Workshops in einer JSON-Datei.

    Args:
        workshops (List[Workshop]): Liste der Workshops.
        filename (str): Der Name der Ausgabedatei.
    """
    workshop_data = []
    for workshop in workshops:
        workshop_info = {
            "Start Date": workshop.start_date,
            "End Date": workshop.end_date,
            "Theme": workshop.theme,
            "Participants": workshop.get_participant_data()
        }
        workshop_data.append(workshop_info)

    with open(filename, 'w') as file:
        json.dump(workshop_data, file, indent=4)

def print_details(students: List[Student], dozents: List[Dozent], workshops: List[Workshop],
                  students_filename: str, dozents_filename: str, workshops_filename: str):
    """
    Speichert Informationen über Studenten, Dozenten und Workshops in JSON-Dateien.

    Args:
        students (List[Student]): Liste der Studenten.
        dozents (List[Dozent]): Liste der Dozenten.
        workshops (List[Workshop]): Liste der Workshops.
        students_filename (str): Der Name der Studenten-JSON-Datei.
        dozents_filename (str): Der Name der Dozenten-JSON-Datei.
        workshops_filename (str): Der Name der Workshops-JSON-Datei.
    """
    print_members(students, dozents, students_filename)
    print_workshops(workshops, workshops_filename)

# Beispiel Verwendung
pascal = Student("Pascal", "Ich will coden lernen")
anna = Dozent("Anna", "Ich codiere mit R und Python und liebe die Lehre")
anna.add_skill("Python", "R", "Data Science", "Statistik", "Machine Learning")

workshop1 = Workshop("2023-10-15", "2023-10-17", "Python fuer Anfaenger")
workshop2 = Workshop("2023-11-05", "2023-11-07", "Data Science mit Python")

workshop1.add_participants(pascal, anna)
workshop2.add_participants(anna, pascal)

students = [pascal]
dozents = [anna]
workshops = [workshop1, workshop2]

print_details(students, dozents, workshops, "students.json", "dozents.json", "workshops.json")
