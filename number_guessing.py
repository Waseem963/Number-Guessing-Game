import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
#class that hold BoxLayout which means it behave now as BoxLayout but i add my own features to it 
# (inheriting all the features of BoxLayout from Kivy) this is how class inhertince in python is class (parent)
class GuessGame(Screen):

    # __init__ means this function is constructor, self means this object, **kwargs means key word arguments: accept any number of keyword arguments, and pack them into a dicitonary
    # \**kwargs معناها المعاملات التي يتم تمريهيا بالاسم والنجمتين معناها خد كل المعاملات التي يتم تمريرها بالاسم وحطها في قاموس
    # هي تعمل مثل ارراي تجمع المعلومات يلي ستضاف بالفانكشن لاحقا functon (**kwargs), function( bla = true, bla ="lol", bla = 2) **kwargs = {la = true, bla ="lol", bla = 2}
    #“This is my custom layout, but please Kivy — run your built-in layout setup too, and use all the options you might need.” that purpose of this functions.
    def __init__(self, **kwargs):

        # call the parent class's method, not your own. Because Boxlayout has its own __init__() so 
        # we call it using super(), **kwargs pass it for t.ex. orientation = "vetrical", spacing = 10
        super().__init__(**kwargs)

        #some variables:
        self.level = "medium"
        self.random_number = random.randint(0, 99)
        self.used_hints = []
        self.used_numbers = []
        self.guess_left = 4
        self.guess_used = 1
        self.hint_left = 4
        self.end_game = True
        self.levels = ""

    def setup_game(self):
        if self.level == "easy":
            self.random_number = random.randint(0, 99)
        elif self.level == "medium":
            self.random_number = random.randint(100, 999)
        elif self.level == "hard":
            self.random_number = random.randint(1000, 9999)
        else:
            self.random_number = random.randint(100, 999)  # default

    # Check the answer of the user
    def check_the_result(self, user_guess_number):
        is_answer_correct = False
        # Check if the user answer is wrong
        if(user_guess_number != self.random_number):
            self.guess_left-=1
            self.guess_used+=1
            is_answer_correct = False
            self.end_game = False
            
            return is_answer_correct, self.guess_left, self.guess_used
        
        # Check if the user answer is correct
        if(user_guess_number == self.random_number):
            is_answer_correct = True
            self.end_game = True
            return is_answer_correct, self.guess_left, self.guess_used
        
    #function for hints
    def hints(self):
        digit_split = [int(d) for d in str(self.random_number)]
        sum_total = sum(digit_split)

        sum_last_two = digit_split[len(digit_split) -1] + digit_split[len(digit_split) -2]

        rest_of_digits_not_used = [n for n in digit_split if n not in self.used_numbers]

        if rest_of_digits_not_used:
            random_numbers = random.choice(rest_of_digits_not_used)
            self.used_hints.append(random_numbers)

        random_digit = random.choice(rest_of_digits_not_used)

        list_of_hints = [
            "Total sum of all digits in the number is: " + str(sum_total),
            "Digit number " + str(rest_of_digits_not_used.index(random_digit) + 1) + " is " + str(random_digit),
            "The sum of digit number " + str(rest_of_digits_not_used.index(random_digit) + 1) + " with itself is: " + str(random_digit * 2),
            "Total sum of last two digits in the number is: " + str(sum_last_two),
        ]

        rest_of_hints_not_used = [h for h in list_of_hints if h not in self.used_hints]

        if rest_of_hints_not_used:
            random_hint = random.choice(rest_of_hints_not_used)
            self.used_hints.append(random_hint)
            return random_hint
        
    #end game function to end the game if the user lost all his attempts or win the game.
    def disable_buttons(self):
        self.ids.submit_button.disabled = True
        self.ids.hint_button.disabled = True
        self.ids.restart_button.disabled = False

    def end_game_logic(self):
        
        if(self.end_game == False):
            msg = f"You don't have any attempts left!\n"  
            msg +=   f"Game over!\n" 
            msg +=  f"The number is: {self.random_number} "
            self.ids.result_label.text = msg
        else:
            self.ids.result_label.text =("Congratulation! you win the game from your " + 
                                         str(self.guess_used) + " attempts")
    
    # the main function.
    def check_guess(self): 
        # make the user write an input
        user_input = self.ids.guess_input.text

    #Check if the user write hint and his/her hint attempts are enough
        if not user_input.isdigit(): 
            self.ids.result_label.text = ("Please write only numbers!")
        elif user_input.isdigit():
        # convert the input to integer
            user_guess_number = int(user_input) 
            # return the results from the function CheckTheResult into variables
            is_answer_correct, self.guess_left, self.guess_used = self.check_the_result(user_guess_number)
            
            #Check if the answer that user give is correct
            if not is_answer_correct and self.guess_left >0:
            # here we put f to be able to use directly the variables inside the string using {}
                msg =  f"Not correct, try again!\n" 
                msg +=  f"Attempts left:  {self.guess_left} \n"
                if(user_guess_number < self.random_number): msg += ("low number!")
                elif(user_guess_number > self.random_number): msg +=("High number!")
                self.ids.result_label.text = msg
            #If the player lost the game
            elif self.guess_left <= 0: 
                self.end_game_logic()
                self.disable_buttons()
                self.end_game = True

            else: 
                self.end_game_logic()
                self.disable_buttons()
                self.end_game = False
                
    #function for the button of hints, when user click on the button this functions shows hints.            
    def use_hints(self):
        if self.hint_left > 0:
            self.hint_left -= 1
            show_a_hint = self.hints()
            self.ids.hint_label.text += f"\nHint: {show_a_hint}"
            if self.hint_left == 0:
                self.ids.result_label.text  = "You have no hints left!\n"
            else:
                self.ids.result_label.text  = f"You have {self.hint_left} hints left!\n"
                
 
    

