from datetime import datetime

class Event():
    def __init__(self, title, start_time, end_time, participants, location, description):
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.participants = [participants]
        self.location = location
        self.description = description

    def duration(self):
        return f'Продолжительность меропириятия: {datetime.strptime(self.end_time) - datetime.strptime(self.start_time)}'

    def add_participant(self, name):
        self.participants.append(name)
        return f'Участник {name} добавлен в список участников'

    def conflicts_with(self, other_event):
        latest_start = max(self.start_time, other_event.start_time)
        earlieast_end = min(self.end_time, other_event.end_time)
        overlap = (earlieast_end - latest_start).total_seconds()
        return overlap > 0


    def __str__(self):
        return f'Название мероприятия: {self.title}.\nМесто проведения: {self.location}.\nОписание события: {self.description}.\nВремя начала мероприятия: {self.start_time}.\nВремя окончания мероприятия: {self.end_time}.\nУчастники: {self.participants}'

class Meeting(Event):
    def __init__(self, title, start_time, end_time, participants, location, description, agenda):
        super.__init__(self, title, start_time, end_time, participants, location, description)
        self.agenda = [agenda]
    
    def add_agenda_item(self, item):
        self.agenda.append(item)
        return f'Пункт {item} добавлен к повестке'

    def send_invites(self):
        while participant in self.participants:
        return f'Вы приглашены на событие {self.title}, начало мероприятия {self.start_time}, продолжительность мероприятия {datetime.strptime(self.end_time) - datetime.strptime(self.start_time)}, место проведения {self.location}'

class Call(Event):
    def __init__(self, title, start_time, end_time, participants, location, description, call_link):
        super.__init__(self, title, start_time, end_time, participants, location, description)
        self.call_link = str(call_link)
        self.recording = False

    def start_recording(self):
        self.recording = True
        return f'Запись звонка начата'
    
    def end_recording(self):
        self.recording = False
        return f'Запись звонка остановлена'

def schedule_events(events_list):
    pass