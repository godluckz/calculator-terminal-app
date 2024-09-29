from art import logo
import os

def clear() -> None:
  # Clearing the Screen
  os.system('cls') 
   
def add(p_num1 : float, p_num2 : float) -> float:
    return p_num1 + p_num2


def subtract(p_num1 : float, p_num2 : float) -> float:
    return p_num1 - p_num2


def multiply(p_num1 : float, p_num2 : float) -> float:
    return p_num1 * p_num2


def divide(p_num1 : float, p_num2 : float) -> float:
    return p_num1 / p_num2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
    print(logo)
    w_recalc =  False
    
    while True:
        try:
          w_num1 = input("What's the first number (Exit to stop): ").strip()
          if w_num1.lower().strip("") == "exit":
            break 
          if w_num1.replace(".","").isnumeric():             
            w_num1 = float(w_num1)
            w_recalc = True
            break
          else:
             raise ValueError("Please enter a valid number.")
        except Exception as e:
           print(e)


    while w_recalc:
        for op in operations:
          print(op)

        while True:
            try:
              w_opp = input("Pick an operation: ")

              if w_opp not in operations:
                raise ValueError("Only operations in the list are supported")
              else:
                break 
            except Exception as e:
              print(e)   


        while True:
            try:
              w_num2 = input("What's the next number: (Exit to stop): ").strip()
              if w_num2.lower().strip("") == "exit":
                break 
              if w_num2.replace(".","").isnumeric():             
                w_num2 = float(w_num2)
                break
              else:
                raise ValueError("Please enter a valid number.")
            except Exception as e:
              print(e)        
        
        calculation_function = operations[w_opp]
        print(calculation_function)
        w_answer = calculation_function(w_num1,w_num2)

        print(f"{w_num1} {w_opp} {w_num2} = {w_answer}\n")

        w_continue = input(f"Type 'y' to continue with  {w_answer}, or type 'n' to start a new calculation (Exit to Stop): ").strip().lower()
        if w_continue.lower().strip("") == "exit":
          break 
        elif w_continue in ("y","yes"):
          w_num1 = w_answer
          w_answer = 0
        else:
          clear()
          w_recalc = False
          calculator()

if __name__ == "__main__":    
  calculator()