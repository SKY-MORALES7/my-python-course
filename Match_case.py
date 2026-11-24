# Match-case statement(switch): An alternative to using many 'elif' statements
#                               Execute some code if a value matches a 'case'
#                               Benefits: cleaner and syntax is more readable
# 

def day_of_week(day):
    match day:
        case 1:
            return 'It is sunday'
        case 2:
            return 'It is Monday'
        case 3:
            return 'It is Tuesday'
        case 4:
            return 'It is Wednesday'
        case 5:
            return 'It is Thursday'
        case 6:
            return 'It is Friday'
        case 7:
            return 'It is Saturday'
        case _:
            return 'Not valid'
        
print(day_of_week(2))


def is_not_weekend(day):
    match day:
        case 'Sunday':
            return False
        case 'Monday':
            return True
        case 'Tuesday':
            return True
        case 'Wednesday':
            return True
        case 'Thursday':
            return True
        case 'Friday':
            return True
        case 'Saturday':
            return False
        case _:
            return 'False man'
        
print(is_not_weekend('Sunda'))


# using the or (|) 
def is_weekend(day):
    match day:
        case 'Sunday' | 'Saturday':
            return True
        case 'Monday' | 'Tuesday' | 'Wednesday' | 'Thursday' | 'Friday' :
            return False
        case _:
            return 'False man'
        
print(is_weekend('Saturday'))



def bmi(weight, height):

    bmi =  weight/ height ** 2

    match bmi:

        case _ if bmi <= 18.5:
            return "Underweight"
        case _ if bmi <= 25.0:
            return "Normal"
        case _ if bmi <= 30.0:
            return "Overweight"
        case _:
            return "Obese"

# In Python, _ is commonly called a wildcard pattern when used in match/case