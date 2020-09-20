from mycroft import MycroftSkill, intent_file_handler


class DeveloperAssistant(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('assistant.developer.intent')
    def handle_assistant_developer(self, message):
        self.speak_dialog('assistant.developer')


def create_skill():
    return DeveloperAssistant()

