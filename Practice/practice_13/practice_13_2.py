from datetime import datetime

class Event():
    def __init__(self, title, start_time: datetime, end_time: datetime, participants, location, description):
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.participants = participants
        self.location = location
        self.description = description

    def duration(self):
        delta = self.end_time - self.start_time
        return f'Продолжительность мероприятия: {int(delta.total_seconds() // 60)}.\n'
    
    def add_participant(self, name):
        self.participants.append(name)
        return f'\nУчастник {name} добавлен.\nНовый список участников мероприятия "{self.title}": {", ".join(self.participants)}.\n'

    def conflicts_with(self, other_event):
        latest_start = max(self.start_time, other_event.start_time)
        earlieast_end = min(self.end_time, other_event.end_time)
        overlap = (earlieast_end - latest_start).total_seconds()
        if overlap > 0:
            return f'Внимание! Мероприятия "{self.title}" и "{other_event.title}" пересекаются по времени!\n'

    def __str__(self):
        return (f'Мероприятие: {self.title}.\n'
                f'Описание: {self.description}.\n'
                f'Начало в {self.start_time}.\n'
                f'Окончание в {self.end_time}.\n'
                f'{self.duration()}')

class Meeting(Event):
    def __init__(self, agenda, title, start_time, end_time, participants, location, description):
        super().__init__(title, start_time, end_time, participants, location, description)
        self.agenda = agenda
    
    def add_agenda_item(self, topic):
        self.agenda.append(topic)
        return f'Пункт "{topic}" добавлен к повестке.\nНовый список повестки мероприятия "{self.title}": {"\n\t\t\t\t\t\t\t".join(self.agenda)}\n'

    def send_invites(self):
        info_for_invites = (f'Мероприятие: {self.title}.\n'
                            f'Описание: {self.description}.\n'
                            f'Место проведения: {self.location}\n'
                            f'Начало в {self.start_time}.\n'
                            f'Окончание в {self.end_time}.\n'
                            f'{self.duration()}')
        return '\n'.join(f'{participant}, вы приглашены на встречу!{info_for_invites}'  
                         for participant in self.participants)
    
    def __str__(self):
        meeting_str = super().__str__()
        meeting_info = (f'Повестка: {"\n\t  ".join(self.agenda)}\n'
                        f'Участники: {", ".join(self.participants)}\n')
        return meeting_str + meeting_info

class Call(Event):
    def __init__(self, call_link, title, start_time, end_time, participants, location, description, recording=False, start_recording_flag=False):
        super().__init__(title, start_time, end_time, participants, location, description)
        self.call_link = str(call_link)
        self.recording = recording
        self.start_recording_flag = start_recording_flag

    def start_recording(self, start_recording_flag=False):
        if not self.recording:
            return f'Запись на мероприятии "{self.title}" не предполагается\n'
        else:
            if self.start_recording_flag == False:
                self.start_recording_flag = True
                return f'Запись звонка "{self.title}" начата\n'
            else:
                return f'Запись звонка "{self.title}" и так уже ведется\n'
    
    def end_recording(self):
        if self.start_recording_flag:
            self.start_recording_flag = False
            return f'Запись звонка "{self.title}" остановлена\n'
        return f'Запись не велась\n'
    
    def __str__(self):
        call_str = super().__str__()
        call_info = (f'Мероприятие: {self.title}.\n'
                     f'Описание: {self.description}.\n'
                     f'Начало в {self.start_time}.\n'
                     f'Окончание в {self.end_time}.\n'
                     f'{self.duration()}'
                     f'Участники: {", ".join(self.participants)}\n'
                     f'Ссылка на созвон: {self.call_link}\n')
        if self.recording:
            call_info += f'Будет вестись запись мероприятия "{self.title}"\n'
        else:
            call_info += f'Запись мероприятия "{self.title}" не предполагается\n'
        return call_info

def schedule_events(events_list):
    sorted_events = sorted(events_list, key=lambda value: value.start_time)
    n = len(sorted_events)
    for i in range(n):
        for j in range(i+1, n):
            conflict = sorted_events[i].conflicts_with(sorted_events[j])
            if conflict:
                print(conflict)
    print(f'Итоговое расписание на день:\n')
    for event in sorted_events:
        print(event)            

event_1 = Meeting(agenda=['План продаж на следующий год','Увеличение маркетинговых расходов', 'Увеличение конверсии'],
                  title="Совещание", start_time=datetime(2025, 6, 5, 10, 40),
                  end_time=datetime(2025, 6, 5, 11, 40),
                  participants=['Константин', 'Елена', 'Мария'],
                  location="Офис, конференцзал",
                  description="Обсуждение годового отчёта")

event_2 = Meeting(agenda=['Обсуждение сметы', 'Обсуждение условий оплаты'],
                  title="Встреча с клиентом", start_time=datetime(2025, 6, 5, 10, 0),
                  end_time=datetime(2025, 6, 5, 11, 0),
                  participants=['Акакий', 'Венера', 'Сейлор Мун'],
                  location="Офис, переговорная",
                  description="Обсуждение деталей договора")

event_3 = Call(call_link='wwww.call.link',
               title="Созвон с коллегами",
               start_time=datetime(2025, 6, 5, 15, 50),
               end_time=datetime(2025, 6, 5, 16, 50),
               participants=['Алексей', 'Анастасия', 'Георгий'],
               location=None, description="Согласования по проекту",
               recording=True)


print(event_2.add_participant('Губка Боб'))
print()
print(event_2.add_agenda_item('Какие прекрасные имена у людей на этой встрече'))
print()
print(event_1.conflicts_with(event_2))
print()
print(event_3.start_recording())
print()
print(event_3.end_recording())
print()
schedule_events([event_1, event_2, event_3])
