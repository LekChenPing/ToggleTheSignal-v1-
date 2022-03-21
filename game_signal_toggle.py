# state (-1) = False, state (1) = True
from random import choice

#All class are defined here! 
class signal:
    def __init__(self,state,name):
        self.state = state
        self.name = name
    def readstate(self):
        if self.state == 1:
            #("Current state of "+self.name+": Positive\n")
            return("O")
        elif self.state == -1:
            #("Current state of "+self.name+": Negative\n")
            return("X")
    def toggle(self):
        self.state *= (-1)
        return self.state



#All definition are here!
#All default variables, with value, are here!
all_status = [1,-1]

#define all signals 1 to 9
s1 = signal(choice(all_status), "Signal 1")
s2 = signal(choice(all_status), "Signal 2")
s3 = signal(choice(all_status), "Signal 3")
s4 = signal(choice(all_status), "Signal 4")
s5 = signal(choice(all_status), "Signal 5")
s6 = signal(choice(all_status), "Signal 6")
s7 = signal(choice(all_status), "Signal 7")
s8 = signal(choice(all_status), "Signal 8")
s9 = signal(choice(all_status), "Signal 9")

all_signals_listed = [s1,s2,s3,s4,s5,s6,s7,s8,s9]
all_signalstates_listed = [s1.state,s2.state,s3.state,s4.state,s5.state,s6.state,s7.state,s8.state,s9.state]
targeted_list = [1,1,1,1,1,1,1,1,1]

print("This is the puzzle. Solve it!\n")

def game_map():
    for i in range(0,9,3):
        print(str(all_signals_listed[i].readstate()) + " "+str(all_signals_listed[i+1].readstate()) + " "+str(all_signals_listed[i+2].readstate()) + "\n")


#game mechanism
while(1):
    while(1):
        print(all_signalstates_listed)
        game_map()
        if all_signalstates_listed == targeted_list:
            break
        
        signal_number = int(input())
        if (signal_number<0) or (signal_number>9):
            print("\nAbnormal detected! Game over!\n")
            break
        else:
            number = int(signal_number)-int(1)
            selected_signal = all_signals_listed[number]
            all_signalstates_listed[number] = selected_signal.toggle()
            
            if signal_number == 1:
                selected_signal = all_signals_listed[1]
                all_signalstates_listed[1] = selected_signal.toggle()
                selected_signal = all_signals_listed[3]
                all_signalstates_listed[3] = selected_signal.toggle()

            elif signal_number == 2:
                selected_signal = all_signals_listed[0]
                all_signalstates_listed[0] = selected_signal.toggle()
                selected_signal = all_signals_listed[2]
                all_signalstates_listed[2] = selected_signal.toggle()
                selected_signal = all_signals_listed[4]
                all_signalstates_listed[4] = selected_signal.toggle()
            
            elif signal_number == 3:
                selected_signal = all_signals_listed[1]
                all_signalstates_listed[1] = selected_signal.toggle()
                selected_signal = all_signals_listed[5]
                all_signalstates_listed[5] = selected_signal.toggle()
            
            elif signal_number == 4:
                selected_signal = all_signals_listed[0]
                all_signalstates_listed[0] = selected_signal.toggle()
                selected_signal = all_signals_listed[4]
                all_signalstates_listed[4] = selected_signal.toggle()
                selected_signal = all_signals_listed[6]
                all_signalstates_listed[6] = selected_signal.toggle()
            
            elif signal_number == 5:
                selected_signal = all_signals_listed[1]
                all_signalstates_listed[1] = selected_signal.toggle()
                selected_signal = all_signals_listed[3]
                all_signalstates_listed[3] = selected_signal.toggle()
                selected_signal = all_signals_listed[5]
                all_signalstates_listed[5] = selected_signal.toggle()
                selected_signal = all_signals_listed[7]
                all_signalstates_listed[7] = selected_signal.toggle()
            
            elif signal_number == 6:
                selected_signal = all_signals_listed[2]
                all_signalstates_listed[2] = selected_signal.toggle()
                selected_signal = all_signals_listed[4]
                all_signalstates_listed[4] = selected_signal.toggle()
                selected_signal = all_signals_listed[8]
                all_signalstates_listed[8] = selected_signal.toggle()
            
            elif signal_number == 7:
                selected_signal = all_signals_listed[3]
                all_signalstates_listed[3] = selected_signal.toggle()
                selected_signal = all_signals_listed[7]
                all_signalstates_listed[7] = selected_signal.toggle()
            
            elif signal_number == 8:
                selected_signal = all_signals_listed[4]
                all_signalstates_listed[4] = selected_signal.toggle()
                selected_signal = all_signals_listed[6]
                all_signalstates_listed[6] = selected_signal.toggle()
                selected_signal = all_signals_listed[8]
                all_signalstates_listed[8] = selected_signal.toggle()
            
            elif signal_number == 9:
                selected_signal = all_signals_listed[5]
                all_signalstates_listed[5] = selected_signal.toggle()
                selected_signal = all_signals_listed[7]
                all_signalstates_listed[7] = selected_signal.toggle()
    print("Game over!~")
    break
