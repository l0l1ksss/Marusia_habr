from parsing import *
registred_states = {}

develop_url="https://habr.com/ru/flows/develop/"#разработка
admin_url="https://habr.com/ru/flows/admin/"#администрирование
design_url="https://habr.com/ru/flows/design/"#дизайн
management_url="https://habr.com/ru/flows/management/"#менеджмент
marketing_url="https://habr.com/ru/flows/marketing/"#маркетинг
popsci_url="https://habr.com/ru/flows/popsci/"#научпоп

def get_state(state_id):
    return registred_states[state_id]

def get_root_state():
    global root_state_id
    return registred_states[root_state_id]


class Transition:

    def __init__(self, to_id, synonims):
        self.to_id = to_id
        self.synonims = synonims

    def must_go(self, user_text):
        return user_text in self.synonims

    def get_dest_id(self):
        return self.to_id

class State:

    def __init__(self, id, text, transitions, default_transition, is_end=False):
        self.id = id
        self.text = text
        self.transitions = transitions
        self.default_transition = default_transition
        self.is_end=is_end

    def get_next_state(self, user_input):
        for transition in self.transitions:
            if transition.must_go(user_input):
                return get_state(transition.to_id)

        return get_state(self.default_transition)

    def register(self):
        global registred_states
        registred_states[self.id] = self

    def get_text(self):
        return self.text

    def get_id(self):
        return self.id

    def is_end_state(self):
        return self.is_end

def init():
    global root_state_id
    global admin_url
    State("100", "Привет! Хотите услышать самые интересные и свежие новости из мира технологий?", [Transition("900",["нет","Нет"])], "101").register()

    State("101", "Что вам по душе ? Разработка, администрирование, дизайн, менеджмент, маркетинг, а может научпоп ? ", [
        Transition("900",["нет","Нет", "Не хочу", "не хочу", "Неа","неа"]),
        Transition("200", ["1","Разработка","разработка","первое","Первое"]),
        Transition("300", ["2","Администрирование","администрирование","Второе","второе"]),
        Transition("400", ["3","Дизайн","дизайн","Третье","третье"]),
        Transition("500", ["4","Менеджмент","менеджмент","Четвертое","Четвёртое","четвертое","четвёртое"]),
        Transition("600", ["5","Маркетинг","маркетинг","Пятое","пятое", "Предпоследнее", "предпоследнее"]),
        Transition("700", ["6","последнее","Научпоп","научпоп","Последнее"])
    ], None).register()

    State("200", f"Вот что я могу предложить 👾 : {spisok(develop_url)} Назовите номер выбранной вами новости",
          [
              Transition("210", ["1", "первое", "Первое"]),
              Transition("211", ["2", "Второе", "второе"]),
              Transition("212", ["3", "Третье", "третье"]),
              Transition("213", ["4", "Четвертое", "Четвёртое", "четвертое", "четвёртое"]),
              Transition("214", ["5", "Пятое", "пятое", "Последнее", "последнее"])
          ], None).register()

    State("210", f"{tekst(ret_ssilka(develop_url,1))}",
          [Transition("900", [])], "900").register()

    State("211", f"{tekst(ret_ssilka(develop_url,2))}",
          [Transition("900", [])], "900").register()

    State("212", f"{tekst(ret_ssilka(develop_url,3))}",
          [Transition("900", [])], "900").register()

    State("213", f"{tekst(ret_ssilka(develop_url,4))}",
          [Transition("900", [])], "900").register()

    State("214", f"{tekst(ret_ssilka(develop_url,5))}",
          [Transition("900", [])], "900").register()

    State("300", f"Вот что я могу предложить 👨‍🚀 : {spisok(admin_url)} Назовите номер выбранной вами новости",
          [
              Transition("310", ["1", "первое", "Первое"]),
              Transition("311", ["2", "Второе", "второе"]),
              Transition("312", ["3", "Третье", "третье"]),
              Transition("313", ["4", "Четвертое", "Четвёртое", "четвертое", "четвёртое"]),
              Transition("314", ["5", "Пятое", "пятое", "Последнее", "последнее"])], "900").register()

    State("310", f"{tekst(ret_ssilka(admin_url,1))}",
          [Transition("900", [])], "900").register()

    State("311", f"{tekst(ret_ssilka(admin_url,2))}",
          [Transition("900", [])], "900").register()

    State("312", f"{tekst(ret_ssilka(admin_url,3))}",
          [Transition("900", [])], "900").register()

    State("313", f"{tekst(ret_ssilka(admin_url,4))}",
          [Transition("900", [])], "900").register()

    State("314", f"{tekst(ret_ssilka(admin_url,5))}",
          [Transition("900", [])], "900").register()

    State("400", f"Вот что я могу предложить 🎨 : {spisok(design_url)} Назовите номер выбранной вами новости",
          [
              Transition("410", ["1", "первое", "Первое"]),
              Transition("411", ["2", "Второе", "второе"]),
              Transition("412", ["3", "Третье", "третье"]),
              Transition("413", ["4", "Четвертое", "Четвёртое", "четвертое", "четвёртое"]),
              Transition("414", ["5", "Пятое", "пятое", "Последнее", "последнее"])], "900").register()

    State("410", f"{tekst(ret_ssilka(design_url,1))}",
          [Transition("900", [])], "900").register()

    State("411", f"{tekst(ret_ssilka(design_url,2))}",
          [Transition("900", [])], "900").register()

    State("412", f"{tekst(ret_ssilka(design_url,3))}",
          [Transition("900", [])], "900").register()

    State("413", f"{tekst(ret_ssilka(design_url,4))}",
          [Transition("900", [])], "900").register()

    State("414", f"{tekst(ret_ssilka(design_url,5))}",
          [Transition("900", [])], "900").register()

    State("500", f"Вот что я могу предложить 👔 : {spisok(management_url)} Назовите номер выбранной вами новости",
          [
              Transition("510", ["1", "первое", "Первое"]),
              Transition("511", ["2", "Второе", "второе"]),
              Transition("512", ["3", "Третье", "третье"]),
              Transition("513", ["4", "Четвертое", "Четвёртое", "четвертое", "четвёртое"]),
              Transition("514", ["5", "Пятое", "пятое", "Последнее", "последнее"])], "900").register()

    State("510", f"{tekst(ret_ssilka(management_url,1))}",
          [Transition("900", [])], "900").register()

    State("511", f"{tekst(ret_ssilka(management_url,2))}",
          [Transition("900", [])], "900").register()

    State("512", f"{tekst(ret_ssilka(management_url,3))}",
          [Transition("900", [])], "900").register()

    State("513", f"{tekst(ret_ssilka(management_url,4))}",
          [Transition("900", [])], "900").register()

    State("514", f"{tekst(ret_ssilka(management_url,5))}",
          [Transition("900", [])], "900").register()

    State("600", f"Вот что я могу предложить 🛒 : {spisok(marketing_url)} Назовите номер выбранной вами новости",
          [
              Transition("610", ["1", "первое", "Первое"]),
              Transition("611", ["2", "Второе", "второе"]),
              Transition("612", ["3", "Третье", "третье"]),
              Transition("613", ["4", "Четвертое", "Четвёртое", "четвертое", "четвёртое"]),
              Transition("614", ["5", "Пятое", "пятое", "Последнее", "последнее"])], "900").register()

    State("610", f"{tekst(ret_ssilka(marketing_url,1))}",
          [Transition("900", [])], "900").register()

    State("611", f"{tekst(ret_ssilka(marketing_url,2))}",
          [Transition("900", [])], "900").register()

    State("612", f"{tekst(ret_ssilka(marketing_url,3))}",
          [Transition("900", [])], "900").register()

    State("613", f"{tekst(ret_ssilka(marketing_url,4))}",
          [Transition("900", [])], "900").register()

    State("614", f"{tekst(ret_ssilka(marketing_url ,5))}",
          [Transition("900", [])], "900").register()

    State("700", f"Вот что я могу предложить 👓 : {spisok(popsci_url)} Назовите номер выбранной вами новости",
          [
              Transition("710", ["1", "первое", "Первое"]),
              Transition("711", ["2", "Второе", "второе"]),
              Transition("712", ["3", "Третье", "третье"]),
              Transition("713", ["4", "Четвертое", "Четвёртое", "четвертое", "четвёртое"]),
              Transition("714", ["5", "Пятое", "пятое", "Последнее", "последнее"])], "900").register()

    State("710", f"{tekst(ret_ssilka(popsci_url, 1))}",
          [Transition("900", [])], "900").register()

    State("711", f"{tekst(ret_ssilka(popsci_url, 2))}",
          [Transition("900", [])], "900").register()

    State("712", f"{tekst(ret_ssilka(popsci_url, 3))}",
          [Transition("900", [])], "900").register()

    State("713", f"{tekst(ret_ssilka(popsci_url, 4))}",
          [Transition("900", [])], "900").register()

    State("714", f"{tekst(ret_ssilka(popsci_url, 5))}",
          [Transition("900", [])], "900").register()


    State("900", "Пока, удачи!", [], None, True).register()

    root_state_id="100"

init()


    #Храм технологий