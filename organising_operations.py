# variabila globala
this_text = "Salut, acesta este textul global!"

def log_into_terminal():
    print(this_text)

log_into_terminal()

# functie ce contine var globala + var locala
def log_into_terminal_2():
    local_text = "Acesta este textul local!"
    print(this_text)
    print(local_text)

log_into_terminal_2()

# functii multiple
def another_function():
    log_into_terminal()

another_function()


def log_into_terminal_3():
    local_text = "Acesta este textul local!"

    def fourth_function():
        print("Salut din fourth_function.")

    print(this_text)
    print(local_text)
    fourth_function()  # apelam functia interna


def log_into_terminal_3(message):
    print(f"Mesaj primit: {message}")

def another_function():
    log_into_terminal_3("Salut din another_function!")

another_function()
log_into_terminal_3("Acesta este un mesaj transmis.")


# argumente multiple

def log_into_terminal_4(msg1, msg2):
    print(f"Primul mesaj: {msg1}")
    print(f"Al doilea mesaj: {msg2}")

primul = "Salut"
al_doilea = "Ce faci?"
log_into_terminal_4(primul,al_doilea)

def greetings(name):
    return f"Salut, {name}!"

print(greetings("Ana"))
print(greetings("Ion"))
print(greetings("George"))












