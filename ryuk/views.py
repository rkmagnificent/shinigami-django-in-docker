from django.http import HttpResponse


def index(request):
    return HttpResponse("""
Ryuk (リューク Ryūku?) is a bored Shinigami that drops a Death Note, a notebook that allows you to kill anyone simply by knowing their name and face, into the human world in order to have fun. It is picked up by Light Yagami, a young genius who uses it in an attempt to create and rule a world "cleansed of evil" as "God".
    """)
