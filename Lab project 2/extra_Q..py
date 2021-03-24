'''
  Building the car game ::
  CAR GAME:
        > help
          start - to start the car
          stop - to stop the car
          quit - to exit

        > asd
          I don't understand this
        > start
          Car started... Ready to go!!
        > stop
          Car stopped..
        > quit
'''
# Uses while condition until the user writes quit.

#solution
command = ""
started = False
while True:
    command = input("> ").lower()
    if command =="start":
        if started:
            print("Car is already started.")
        else:
            started = True
            print("Car started.")
    elif command == "stop":
        if not started:
            print("Car is already stopped!!")
        else:
            started = False
            print("Car stopped!!")
    elif command == "help":
        print("start : To start the car.")
        print("stop : To stop the car.")
        print("quit : To exit.")
    elif command == "quit":
        print("I can't understand. Error! Error!")
    else:
        print('The program is over')
print("The end!!!!!!!")

