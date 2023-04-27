#!/usr/bin/env pybricks-micropython
# coding=utf-8

# Legger til mappene i søkestien for imports bare når programmet kjører
import os
import sys
p_root = os.getcwd() #root of project
sys.path.append(p_root)
sys.path.append(p_root+"/"+"HovedFiler")
sys.path.append(p_root+"/"+"moduler")
#_______________________________________________________
from pybricks.hubs import EV3Brick
from funksjoner import Bunch
import socket
import struct
import uselect
import config
import _thread

# Set up socket for joystick inputs
def InputSocket(robot,Configs):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    robot.inputSock = sock
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("", 8080))
    sock.listen(1)

    if not Configs.livePlot:
        print("Waiting for joystick connection from computer (Run the file called 'Run_2_PC.py')")
        robot.brick.speaker.beep()

    # Motta koblingen og send tilbake "acknowledgment" som byte
    connection, _ = sock.accept()
    connection.setblocking(False)
    connection.send(b"ack")

    if not Configs.livePlot:
        print("Acknowlegment sent to joystick on computer.")
    robot.JoystickConnection = connection


def Initialize(Configs):
    
    # inneholder all info om roboten
    robot = Bunch()
    robot.brick = EV3Brick()

    # joystick inneholder all info om joysticken.
    robot.joystick = infoJoystick()

    if Configs.ConnectJoystickToPC and robot.joystick["id"] != None:
        print('____ FEIL VED KOBLING AV STYRESTIKK ____')
        print("To use a joystick on robot, you must specify Configs.ConnectJoystickToPC=False")
        print("To use a joystick on PC/Mac, you must specify Configs.ConnectJoystickToPC=True")
        print("You have specified Configs.ConnectJoystickToPC=True, but the joystick is connected to the robot.")
        print('________________________________________')
        print()
        raise Exception()


    if Configs.ConnectJoystickToPC:
        print('__ PLEASE CONNECT JOYSTICK TO PC/MAC! __')
        print('Configs.ConnectJoystickToPC = True')
        print("You have chosen to connect the joystick to the PC/Mac.")
        print("______________________________________________________")
        print()

    
    if Configs.ConnectJoystickToPC:
        _thread.start_new_thread(InputSocket, (robot,Configs)) 

    if Configs.livePlot:
        # Sett opp socketobjektet, og hør etter for "connection"
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        robot.sock = sock
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("", 8070))
        sock.listen(1)

        # Gi et pip fra robotten samt print i terminal
        # for å vise at den er klar for socketkobling fra PC
        print("Waiting for connection from computer.")
        robot.brick.speaker.beep()

        # Motta koblingen og send tilbake "acknowledgment" som byte
        connection, _ = sock.accept()
        connection.send(b"ack")
        print("Acknowlegment sent to computer.")
        robot.connection = connection

    if Configs.ConnectJoystickToPC:
        while not "JoystickConnection" in robot.__dict__:
            pass
        print('Ready to read joystick inputs from PC/Mac')

   
    # Fila hvor alle dataene dine lagres
    robot.dataToFile = open(Configs.filename, "w")
    return robot



def identifyJoystick():
    """
    Identifiserer hvilken styrestikk som er koblet til;
    enten logitech eller dacota (eventuelt en annen styrestikk)
    Denne funksjonen skal ikke endres.
    """

    for i in range(2, 1000):
        path = ("/dev/bus/usb/001/{:03d}".format(i))
        try:
            with open(path, "rb") as f:
                joy = f.read()
                if joy[2] == 16:
                    return "logitech"
                elif joy[2] == 0:
                    return "dacota"
                else:
                    return "Ukjent styrestikk."
        except:
            # print("Feil i identifyJoystick!")
            pass



def infoJoystick():
    """
    Fyller ut og returnerer en "joystick"-dictionary som inneholder all info om styrestikk.
    Nøkler i dictionaryen er som følger:
    "id" - retur fra identifyJoystick()
    "scale" - skaleringsverdi, avhengig av hvilken styrestikk som brukes
    "FORMAT" - long int x2, unsigned short x2, unsigned int
    "EVENT_SIZE" - struct.calcsize av "FORMAT"
    "in_file" - hvor bevegelsene til styrestikken lagres på EV3en
    """

    joystick = {}
    joystick["id"] = identifyJoystick()
    
    joyScale = 0
    if joystick["id"] == "logitech":
        joyScale = 1024

    elif joystick["id"] == "dacota":
        joyScale = 255


    joystick["scale"] = joyScale
    joystick["FORMAT"] = 'llHHI'
    joystick["EVENT_SIZE"] = struct.calcsize(joystick["FORMAT"])
    try:
        joystick["in_file"] = open("/dev/input/event2", "rb")
    except OSError:  # hvis ingen joystick er koblet til
        joystick["in_file"] = None
    return joystick

def getJoystickValues(robot):
    print("Joystick thread started")

    event_poll = uselect.poll()
    if robot.joystick["in_file"] is not None:
        event_poll.register(robot.joystick["in_file"], uselect.POLLIN)
    else:
        return
    while True:
        events = event_poll.poll(0)
        if len(events) > 0 and events[0][1] & uselect.POLLIN:
            try:
                (_, _, ev_type, code, value) = struct.unpack(
                    robot.joystick["FORMAT"],
                    robot.joystick["in_file"].read(
                        robot.joystick["EVENT_SIZE"]))
            except Exception as e:
                sys.print_exception(e)
            if ev_type == 1:

                # Når man slipper knappene så skal 
                # state falle tilbake på 0. Konverterer også False/True til tall-verdier
                # som skrives til fil og kan dermed konverteres i matlab.
                if value == 0:
                    state = 0
                else:
                    state = 1
                #_______________________________________
                
                if code == 288:
                    config.joy1Instance = state
                    config.joyMainSwitch = state
                elif code == 289:
                    config.joy2Instance = state
                elif code == 290:
                    config.joy3Instance = state
                elif code == 291:
                    config.joy4Instance = state
                elif code == 292:
                    config.joy5Instance = state
                elif code == 293:
                    config.joy6Instance = state
                elif code == 294:
                    config.joy7Instance = state
                elif code == 295:
                    config.joy8Instance = state  
                elif code == 296:
                    config.joy9Instance = state
                elif code == 297:
                    config.joy10Instance = state
                elif code == 298:
                    config.joy11Instance = state
                elif code == 299:
                    config.joy12Instance = state
                else:
                    # indikasjon på at jeg har glemt å ta med en knapp; legg til i koden
                    print("--------------------------------------")
                    print("Unknown code!")
                    print("ev_type: " + str(ev_type) + ". code: " + str(code) + ". value: " + str(value) + ".")
                    print("--------------------------------------")

            elif ev_type == 3:
                # all dacota-relatert informasjon (kode 2 og kode 5 for dacota) er usikkert, test?
                if code == 0:
                    config.joySideInstance = scale(
                        value,
                        (robot.joystick["scale"], 0),
                        (100, -100))
                elif code == 1:
                    config.joyForwardInstance = scale(
                        value,
                        (0, robot.joystick["scale"]),
                        (100, -100))
                elif code == 2 and robot.joystick["id"] == "dacota":
                    #POTENSIOMETER - dacota - USIKKERT
                    config.joyPotMeterInstance = scale(
                        value,
                        (255, 0),
                        (-100, +100))
                elif code == 5:
                    #TORSION - dacota og logitech
                    config.joyTwistInstance = scale(
                        value,
                        (255, 0),
                        (+100, -100))
                elif code == 6 and robot.joystick["id"] == "logitech":
                    #POTENSIOMETER - logitech
                    config.joyPotMeterInstance = scale(
                        value,
                        (255, 0),
                        (-100, +100))

                # LOGITECH/DACOTA POV/HAT
                elif code == 16:
                    # POV/hat switch - hoyre - venstre, 1 - 4294967295
                    if value == 0:
                        state = 0
                    else:
                        state = scale(value,(4294967295, 1),(-1,+1))
                    config.joyPOVSideInstance = state
                elif code == 17:
                    # POW/hat switch - ned - opp, 1 - 4294967295
                    if value == 0:
                        state = 0
                    else:
                        state = scale(value,(1, 4294967295),(-1,+1))
                    config.joyPOVForwardInstance = state


def CloseFile(robot):
    if  robot.joystick["in_file"] != None:
        try:
            robot.joystick["in_file"].close()
        except ValueError: # file already closed
            pass

    try:
        robot.dataToFile.close()
    except ValueError: # file already closed
        pass
        


def CloseJoystick(robot,Configs): 
    if "JoystickConnection" in robot.__dict__:
        try:
            robot.JoystickConnection.send(b"end?")
        except OSError:
            pass
        robot.JoystickConnection.close()
        
    if Configs.livePlot:
        try:
            robot.connection.send(b"end?")
        except OSError:
            pass
        robot.connection.close()

    if "sock" in robot.__dict__:
        robot.sock.close()



def scale(value, src, dst):
    return ((float(value - src[0])
            / (src[1] - src[0])) * (dst[1] - dst[0])
            + dst[0])