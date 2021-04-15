#"I hereby certify that this program is solely the result of my own work 
import Draw

#canvas' width, canvas' height
canvasWidth = 1000

#prompt area's X coordinate, Y coordinate and height
#the prompt's width is equal to the canvas's width 
promptX = 0
promptY = 650
promptHeight = 150

#home page, when the user clicks on the "button", the program starts prompting
#for information
def homePage():
    Draw.clear()
    display = True
    
    #until the user clicks on the button area, display the home page
    while display:
        #draw the home page
        Draw.setFontSize(35)
        Draw.setFontBold(False)
        Draw.setColor(Draw.DARK_BLUE)
        centerAlignedStr("Welcome to:", 50)
        centerAlignedStr("Create Your Own Income Statement", 90)
        #draw the button to get to the "next page" --> prompt areas
        Draw.filledRect(375, 450, 250, 100)
        Draw.setColor(Draw.WHITE)
        Draw.setFontBold(True)
        Draw.setFontSize(20)
        Draw.string("Click here to get started", 387, 490)
        
        #when the user clicks on the button, stop displaying the home page
        if Draw.mousePressed():
            if Draw.mouseX() >375 and Draw.mouseX() < 375 + 250 and\
               Draw.mouseY() >450 and Draw.mouseY() < 450 + 100:
                display = False 
                
        Draw.show()
    
#create the prompt area where the user will be typing
def createPromptArea(t, x, y, wide, promptHeight):
    Draw.setFontSize(20)
    Draw.setColor(Draw.GRAY) 
    Draw.setFontBold(False)
    Draw.string("Press Enter to proceed", 0, y-30)
    Draw.setColor(Draw.GRAY)            
    Draw.filledRect(x, y, wide, promptHeight)
    Draw.setColor(Draw.WHITE)
    Draw.setFontBold(True)
    centerAlignedStr(t, y + 50)
    
    Draw.show()       

#create a string that contains whatever the user has typed in
#parameters: the len of what the user can type in (num), if the user can type in nums/letters (string) 
#            if the user can type in other keys (True/False), if the user can type in commas (True/False)
def getString(lenLimit, disableNumsOrLets, enableSpecialChrs, enableComma, x, y, wide, promptHeight):
    #empty string for what the user will type in the future
    ans = ""
    done = False
    
    #while the user has not finished typing (did not press Return)
    while not done:
        
        #if the user clicks on a key
        if Draw.hasNextKeyTyped():
            newKey = Draw.nextKeyTyped()
            
            #if the key clicked is acceptable (not in disableNumsOrLets)
            # and if ans is not longer than the limit, add the key to the string (ans)
            if len(ans) < lenLimit and\
               newKey in "abcdefghijklmnopqrstuvwxyz\
               ABCDEFGHIJKLMNOPQRSTUVWXYZ1234587890" and (newKey not in disableNumsOrLets):
                ans += newKey 
                
            # if the user clicks on return stop the while loop    
            elif newKey == "Return":
                done = True
            
            #if the user clicks on BackSpace, delete the last character of ans     
            elif len(ans) <= lenLimit and newKey == "BackSpace":
                if len(ans) > 0:
                    ans = ans[0:len(ans)-1]  
            
            #if the user clicks on comma and commas are acceptable, add comma to ans
            elif len(ans) < lenLimit and newKey == "comma" and enableComma == True:
                ans += ","                
            
            #if "special characters" are acceptable, add the character 
            #(that the user clicked on) to the string
            if enableSpecialChrs == True:
    
                if len(ans) < lenLimit and newKey == "period":
                    ans += "."
                elif len(ans) < lenLimit and newKey == "space":
                    ans += " "   
                elif len(ans) < lenLimit and newKey == "exclam":
                    ans += "!" 
                elif len(ans) < lenLimit and newKey == "at":
                    ans += "@"
                elif len(ans) < lenLimit and newKey == "numbersign":
                    ans += "#"
                elif len(ans) < lenLimit and newKey == "dollar":
                    ans += "$"
                elif len(ans) < lenLimit and newKey == "percent":
                    ans += "%"
                elif len(ans) < lenLimit and newKey == "asciicircum":
                    ans += "^"
                elif len(ans) < lenLimit and newKey == "ampersand":
                    ans += "&"
                elif len(ans) < lenLimit and newKey == "asterisk":
                    ans += "*"
                elif len(ans) < lenLimit and newKey == "parenleft":
                    ans += "("
                elif len(ans) < lenLimit and newKey == "parenright":
                    ans += ")"  
                elif len(ans) < lenLimit and newKey == "quoteright":
                    ans += "'"     
                elif len(ans) < lenLimit and newKey == "quotedbl":
                    ans += '"'                
                elif len(ans) < lenLimit and newKey == "semicolon":
                    ans += ";"           
                elif len(ans) < lenLimit and newKey == "colon":
                    ans += ":"   
                elif len(ans) < lenLimit and newKey == "slash":
                    ans += "/"                            
             
            #display what the user is inputting in the prompt area
            Draw.clear()
            Draw.setFontSize(20)
            Draw.setColor(Draw.GRAY)
            Draw.setFontBold(False)
            Draw.string("Press Enter to proceed", 0, y-30)                      
            Draw.filledRect(x, y, wide, promptHeight)
            Draw.setColor(Draw.WHITE)
            Draw.string(ans, x, y+50)   
        Draw.show()
        
    #return the user's input   
    return ans

#create an error message
#parameter: the string that will appear as error message
def createErrorMessage(e):
    Draw.setColor(Draw.RED)
    Draw.setFontSize(18)
    Draw.setFontBold(True)
    centerAlignedStr("Error Message:", 0)
    centerAlignedStr(e, 20)
    
    Draw.show()
    
#string prompt (used to getName of the company)
#continue prompting the user for the name, until he/she doesn't type anything
#parameter: text of the prompt
def stringPrompt(t):
    Draw.clear()
    createPromptArea(t, promptX, promptY, canvasWidth, promptHeight)
    string = ""
    
    #don't proceed to next prompt until user types in a name
    while string.strip(" ") == "":
        #get the string the user typed
        #the user can type in "special characters", numbers, letters and commas
        string = getString(100, "", True, True, promptX, promptY, canvasWidth, promptHeight)
    return string

#list prompt (used to getPeriod and getMonth)
#continue prompting the user until something is typed in
#if the input is not part of the list (of valid answers), display error message
#   and prompt again
#parameters: text of the prompt, list of valid answers, len admissible to user, 
#            error message
def listPrompt(t, l, lenLimit, e):
    createPromptArea(t, promptX, promptY, canvasWidth, promptHeight)
    count = 0
    string = ""
    
    #while string is empty or input is not valid, continue prompting the user
    while string == "" or count == 1:
        count = 0
       
        createPromptArea(t, promptX, promptY, canvasWidth, promptHeight)
        
        #get the string the user typed
        #the user can type in only letters
        string = getString(lenLimit,"1234567890", False, False, promptX, promptY, canvasWidth, promptHeight)
        
        #the answer is not case sensitive (user can type in lower or upper cases)
        newStr = string.lower().strip()
        #if the user's input is part of the list of acceptable answers, return the input
        if newStr in l:
            Draw.clear()
            return newStr.capitalize().strip()
        #if it is not part of the answers list, display error message
        else:
            count = 1
            createErrorMessage(e)


#int prompt (used to getDay and getYear)
#continue prompting the user until something is typed in
#if the input is not in the range validLow/validpromptHeight, display error message
#   and prompt again
#parameters: text of the prompt, len admissible to user, min valid num, max valid num,
#            error message    
def intPrompt(t, lenLimit, validLow, validHigh, e):
    createPromptArea(t, promptX, promptY, canvasWidth, promptHeight)
    count = 0
    string = ""
    
    #while string is empty or input is not valid, continue prompting the user
    while string == "" or count == 1:
        count = 0

        Draw.setFontSize(15)    
        createPromptArea(t, promptX, promptY, canvasWidth, promptHeight)
        
        #get the string the user typed
        #the user can type in only numbers
        string = getString(lenLimit, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", False, False, promptX, promptY, canvasWidth, promptHeight)
        
        #if the user's input is at least 1 digit long  
        #and is in the range of validLow and validHigh, return the answer
        if len(string) >= 1:
            if int(string) >= int(validLow) and int(string) <= int(validHigh):
                Draw.clear()
                return string    
            #if the user's input is not in the range validLow/validHigh display error message
            else:
                count = 1
                createErrorMessage(e)
        #if the user's input is not at least 1 digit long, display error message        
        else:
            count = 1
            createErrorMessage(e)        

#dollar prompt (used to getRevenues and getExpenses)
#continue prompting the user until something is typed in
#the user can type in balances with or without commas (program will automatically put in
#                                                      commas later in the code)
#when the input is checked by dollarString, if it is not valid, display error message (e.g, 2,00,000)
#   and prompt again
#parameters: text of the prompt, len admissible to user, error message      
def dollarPrompt(t, lenLimit, e):
    Draw.clear()
    createPromptArea(t, promptX, promptY, canvasWidth, promptHeight)
    count = 0
    string = ""
    
    #while string is empty or input is not valid, continue prompting the user
    while string == "" or count == 1:
        count = 0

        Draw.setFontSize(15)    
        createPromptArea(t, promptX, promptY, canvasWidth, promptHeight)
        
        #get the string the user typed
        #user can only type in numbers and commas
        string = getString(lenLimit, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", False, True, promptX, promptY, canvasWidth, promptHeight)
        
        #if the user's input is at least 1 digit long  
        #and if after being passed into dollarString, the function returns True 
        #return the input string          
        if len(string) >= 1:
            dollarStr = dollarString(string)
            if dollarStr == True:
                Draw.clear()
                return string        
            #if the dollarString function returns False, display error msg
            else:
                count = 1
                createErrorMessage(e)
        #if the user's input is not at least 1 digit long, display error message          
        else:
            count = 1
            createErrorMessage(e)        

#checks if dollarPrompt input is a valid number or not
# e.g. valid: 1,234,567 - 234,567 - 34,567 - 4,567 - 567 - 67 - 7
#      not valid: 1,23,4567 - 234,56 - 45,67
# fyi: the user can input a number with or without commas
#      if the user does not put them, the program will add the commas itself further in the code
def dollarString(s):
    
    #splits the dollar string by ',' and creats a list that contains each section of the number
    new = s.split(",")
    
    # if there are two commas, e.g.: 1,234,567
    if len(new) == 3:
        if len(new[0]) == 1 and len(new[1]) == 3 and len(new[2]) == 3 or\
           len(new[0]) == 2 and len(new[1]) == 3 and len(new[2]) == 3 or\
           len(new[0]) == 3 and len(new[1]) == 3 and len(new[2]) == 3:
            return True
        
    # if there is one comma, e.g.: 1,234    
    elif len(new) == 2:
        if len(new[0]) == 1 and len(new[1]) == 3 or\
           len(new[0]) == 2 and len(new[1]) == 3 or\
           len(new[0]) == 3 and len(new[1]) == 3:
            return True
    
    # no commas 
    elif len(new) == 1:
        if len(new[0]) == 1 or len(new[0]) == 2 or len(new[0]) == 3:
            return True
        
    #accept number if the user does not type in commas    
    if "," not in s:
        return True
    
    return False

#take out commas from str and transform into int
def dollarStringToInt(s):
    return int(s.replace(',','')) 

#get heading information
# Prompt the user for their company's name
def getName():
    #prompt text
    promptName = "Please insert your company's name"
    name = stringPrompt(promptName)
    return name

# Prompt the user for the length of their company's accounting period
def getPeriod():
    #prompt text
    promptPeriod = "Please insert the length of your company's accounting period\nChose between: \"Quarter\", \"Month\" or \"Year\""
    #prompt's list (acceptable answers)
    periods = ["quarter", "month", "year"]
    #maximum num of characters the user can enter in the prompt
    maxLen = len("quarter")
    #error text
    errorPeriod = "Invalid length, please reinsert the correct length of your accounting period"
    period = listPrompt(promptPeriod, periods, maxLen, errorPeriod)
    return period

# Prompt the user for the month their company's accounting period ends
def getMonth():
    #prompt text
    promptMonth = "Please insert the month your accounting period ends (E.g. January, may, December)"
    #prompt's list (acceptable answers)
    months = ["january", "february", "march", "april", "may", "june", \
              "july", "august", "september", "october", "november", "december"]
    #maximum num of characters the user can enter in the prompt
    maxLen = len("september")
    #error text
    errorMonth = "Invalid month, please reinsert the correct month your accounting period ends"
    month = listPrompt(promptMonth, months, maxLen, errorMonth)
    return month

# Prompt the user for the day their company's accounting period ends
def getDay():
    #prompt text
    promptDay = "Please insert the day your accounting period ends (E.g. 24, 1, 05)"
    #maximum num of digits the user can enter in the prompt
    maxLen = 2
    #min acceptable value
    validLow = 1
    #max acceptable value
    validpromptHeight = 31
    #error text
    errorDay = "Invalid day, please reinsert the correct day your accounting period ends\n(Check that the day is a valid number between 1 and 31, inclusive)"
    day = intPrompt(promptDay, maxLen, validLow, validpromptHeight, errorDay)    
    return day

#check if month and day inserted by user are valid 
#(e.g April 30 valid, April 31 not valid)
#parameters: month and day
def checkDate(m, d):
    Draw.clear()
    months30 = ["November", "April", "June", "September"]
    if m in months30 and int(d) == 31 or m == "February" and int(d) > 29:
        return False
    return True    

# Prompt the user for the year their company's accounting period ends  
def getYear():
    #prompt text
    promptYear = "Please insert the year your accounting period ends (E.g. 2019)"
    #maximum num of digits the user can enter in the prompt
    maxLen = 4
    #min acceptable value
    validLow = 1800
    #max acceptable value
    validpromptHeight = 2021
    #error text
    errorYear = "Invalid year, please reinsert the correct year your accounting period ends\n(Check that the year is a valid number, it should not be greater than \"2021\")"
    year = intPrompt(promptYear, maxLen, validLow, validpromptHeight, errorYear)    
    return year

#get info for body of income statement
#Prompt the user for their company's total Revenues & Gains
def getRevenues():
    #prompt text
    promptRevenues = "Please insert your company's total Revenues & Gains"
    #maximum num of digits (and commas) the user can enter in the prompt (999,999,999 = 11)
    maxLen = 11
    #error text
    errorRevenues = "Invalid balance, please reinsert the correct balance"
    revenues = dollarPrompt(promptRevenues, maxLen, errorRevenues)    
    return revenues

#Prompt the user for their company's total Expenses & Losses
def getExpenses():
    #prompt text
    promptExpenses = "Please insert your company's total Expenses & Losses"
    #maximum num of digits (and commas) the user can enter in the prompt (999,999,999 = 11)
    maxLen = 11
    #error text
    errorExpenses = "Invalid balance, please reinsert the correct balance"
    expenses = dollarPrompt(promptExpenses, maxLen, errorExpenses)    
    return expenses

#add commas to a number (e. g. when user does not type any commas for rev and exp)
#parameter: num
def addCommasToInt(i):
    return "{:,}".format(i)

#calculate the width of a string (in pixels)
#parameter: string you want to draw
def getStringWidth(s):
    box = Draw.bbox(Draw.string(s, -100, -100))
    width = box[2] - box[0]   
    return width

#draw a center algined string
#parameter: string you want to draw
def centerAlignedStr(s, y):
    width = getStringWidth(s)
    Draw.string(s, (canvasWidth//2 - width//2), y)

#draw a right algined string
#parameter: string you want to draw  
def rightAlignedStr(s, y):
    width = getStringWidth(s)
    Draw.string(s, (canvasWidth - 100) - width, y)    

#display the heading information of the income statement
#parameters: information for income statement that the user inserted
#            name, period, month, day, year
def displayHeading(name, period, month, day, year):
    Draw.clear()
    
    Draw.setColor(Draw.DARK_BLUE)
    Draw.filledRect(0, 0, canvasWidth, 110)
    
    Draw.setColor(Draw.WHITE)
    Draw.setFontBold(True)
    Draw.setFontSize(25)

    #company's name
    centerAlignedStr(name, 10)

    #second line of heading: income statement
    centerAlignedStr("Income Statement", 40)

    #third line of heading: "For the (length of accounitng period) ended month day, year"
    if len(day) == 2 and int(day[0]) == 0:
        day = day[1]
        
    line3 = "For the " + str(period) + " Ended " + str(month) + " " + str(day) + ", " + str(year)
    centerAlignedStr(line3, 70)  
    
#display the body information of the income statement
#parameters: information for income statement that the user inserted
#            revenues and expenses
def displayBody(revenues, expenses):
    
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(25)
    Draw.setFontBold(False)
    
    #convert the balance inserted by user to an int
    revenuesInt = dollarStringToInt(revenues)
    expensesInt = dollarStringToInt(expenses)
    
    #Revenues & Gains
    Draw.string("Revenues & Gains", 100, 350)
    revenuesCommas = addCommasToInt(revenuesInt)
      #Total 
    rightAlignedStr("$" + revenuesCommas, 350)
    #width of rev string
    revWidth = getStringWidth("$" + revenuesCommas)

    #Expenses & Losses
    Draw.string("Expenses & Losses", 100, 390)
    expensesCommas = addCommasToInt(expensesInt)
      #Total
    rightAlignedStr(expensesCommas, 390) 
    
    #Net Income/Loss
      #Computing Net Income/Loss
    netIncome = abs(revenuesInt - expensesInt)
      #Add commas to the net income balance
    netIncomeCommas = addCommasToInt(netIncome)
    
      #Net Income
      #if revs >= exps
    if revenuesInt >= expensesInt:
        Draw.string("Net Income", 120, 430)
        Draw.setColor(Draw.DARK_GREEN)
        Draw.string("$", (canvasWidth -100) - revWidth, 430)
        rightAlignedStr(netIncomeCommas, 430)
        
        Draw.setColor(Draw.BLACK)
        #underline total expenses
        Draw.line((canvasWidth-100) - revWidth, 418, (canvasWidth-100), 418)   
                  
        #double underline net income        
        Draw.line((canvasWidth-100) - revWidth, 458, (canvasWidth-100), 458)
        Draw.line((canvasWidth-100) - revWidth, 461, (canvasWidth-100), 461)              

      #Net Loss  
      #if revs < exps
    elif revenuesInt < expensesInt:
        Draw.string("Net Loss", 120, 430)
        Draw.setColor(Draw.DARK_RED)
        
        #if net is longer or equal to revenues
        if len(netIncomeCommas) >= len(revenuesCommas):
            netLossWidth = getStringWidth("$" + "(" + netIncomeCommas)
            Draw.string( "$" + "(" + netIncomeCommas + ")", (canvasWidth-100) - netLossWidth, 430)
            
            Draw.setColor(Draw.BLACK)
            #underline total expenses
            Draw.line((canvasWidth -100) - netLossWidth , 418, (canvasWidth-100), 418)
            
            #double underline net loss        
            Draw.line((canvasWidth-100) - netLossWidth, 458, (canvasWidth-100), 458)
            Draw.line((canvasWidth-100) - netLossWidth, 461, (canvasWidth-100), 461)                
        
        #if net is shorter than revenues    
        elif len(netIncomeCommas) < len(revenuesCommas):
            Draw.string("$", (canvasWidth-100) -  revWidth, 430)
            netLossWidth = getStringWidth("(" + netIncomeCommas)
            Draw.string("(" + netIncomeCommas + ")", (canvasWidth-100) - netLossWidth, 430)
            
            Draw.setColor(Draw.BLACK)
            #underline total expenses
            Draw.line((canvasWidth - 100) - revWidth, 418, (canvasWidth - 100), 418)                

            #double underline net loss        
            Draw.line((canvasWidth - 100) - revWidth, 458, (canvasWidth - 100), 458)
            Draw.line((canvasWidth - 100) - revWidth, 461, (canvasWidth - 100), 461) 
                       
        
def IncomeStatement():
    count = 0
    while count == 0:
        count = 1
        Draw.clear()
        
        #display homePage
        homePage()
        #prompt for name
        name = getName()
        #prompt for period
        period = getPeriod()
        
        month = ""   
        day = ""
        #while we don't have a valid date (e.g. April 30)
        while (month == "" and day == ""):

            #prompt for month
            month = getMonth()
            #prompt for day
            day = getDay()
            #check that it's a valid date
            check = checkDate(month, day)
            
            #if it's not valid, display error message and prompt for month again
            if check == False:
                month = ""
                day = ""
                createErrorMessage("Invalid Date: you inserted a date that does not exist (E.g. April 31)\nPlease reinsert the correct month and day your accounting period ends") 
        
        #prompt for year        
        year = getYear()
        #prompt for revenues
        revenues = getRevenues()
        #prompt for expenses
        expenses = getExpenses()
        
        #while the "start over" button hasn't been clicked, display heading and 
        #body of the income statement
        while count == 1:
            Draw.clear()
            
            displayHeading(name, period, month, day, year)
            displayBody(revenues, expenses)
            
            #draw "start over" button
            Draw.setColor(Draw.DARK_BLUE)
            Draw.filledRect(840, 700, 130, 50)
            Draw.setFontSize(15)
            Draw.setColor(Draw.WHITE)
            Draw.setFontBold(True)
            Draw.string("Click here\nto start over", 860, 708)
           
            Draw.show()      
            
            #when user clicks on "start over button", go back to homePage (start over)
            if Draw.mousePressed():
                if Draw.mouseX() >840 and Draw.mouseX() < 840 + 130 and\
                   Draw.mouseY() >700 and Draw.mouseY() < 700 + 50:
                    count = 0

def main():
    canvasHeight = 1000
    Draw.setCanvasSize(canvasWidth, canvasHeight)
    Draw.setBackground(Draw.WHITE)  
    Draw.setFontSize(15)
    Draw.setColor(Draw.BLACK)    
    IncomeStatement()   
main()   

    
