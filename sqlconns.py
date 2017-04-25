#To get this to work you will need to download python 3.x to your computer
#you will need to install it if you are on a pc - if win10 enable bash makes it easy
#I use Pycharm as my editor for python - free
#I use arvixe as a easy host for sql db - unlimted for 90 a year
#you can use pythonanywhere for this if you pay - sql conn is not free
#digital oceans droplets are cheaper and way better for constant running
#applications like a bot - 512 MB Memory / 20 GB Disk / NYC3 - Ubuntu LAMP on 16.04
#like 10 a month and super easy to get python set up
#i learned all this from team treamhouse and playing alot
#learn virtual enviroments - they will make your life easier -http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/
#learn git - i never used it as a sql guy but love it now
#indentions and caps matter in python - alot



import pymssql, random  #you will have to pip install this library

wordlist=['love','dog','blonde','smile','hunt','priest']

def connection(contype, spname, spparams='qq'):  # which server, whats the sp, what are the parameters needed
    #import pdb; pdb.set_trace() # awesome debugger that walks line by line
    host = ''  #initializing varibles not needed really but helps with errors
    username = ''
    password = ''
    database=''
    if contype ==3:  #if the connections paramter(variable) contype =3 use this
        host = 'sunflower.arvixe.com'
        username = 'sqlslack'
        password = 'sqlslack!'
        database = 'sqlslack'
    if contype == 1:  #example of how you would add multiple - you would actually use a config file
        host = 'xxx.xxx.xxx.xxx'   #very easy to point to your own db
        username = 'whatever'
        password = 'unsecure'
        database = 'probably a stupid name'




    conn = pymssql.connect(host, username, password, database) #creating the connection object using pymsql lib

    cursor = conn.cursor(as_dict=True) #creates a object that can connect to the db

    cursor.execute(spname)   #passing the stored proc from the call as a text string - cursor catches results

    #print('Inside SQL CALL FUNCTION: ',spname,'\n') #debugging code


    rawresults = cursor.fetchall()  #grabs what the SP returned and puts them into a variable of rawresults
    #print('RawResults:',rawresults)
    conn.commit()       #this commits changes
    return rawresults   #return the results to the caller
    conn.close()        #closes the connection to the db

if __name__ == '__main__':  #because you can call this from other programs this line only works when it calls itself


    c=connection(3,'select top 1 * from [sqlslack].[dbo].[Jokes] order by newid()') #fires off a direct sql statement returning results to c
    print(c) #prints all of c -
    for item in c:
        print(item['Joke'],'\n') #prints just the joke

    sql ='dbo.SqlSlack_lottery_random'  #stored proc to variable
    lotteryresults=connection(3,sql)    #passing into the connection funtion
    print(lotteryresults)               #prints overall lottery results

    for numbers in lotteryresults: #you create the variable that will hold the individual items from the result set from sql. its aweosme. so numbers is declared and assigned at this point.
        print(numbers)                  #returns a dictionary - that you access like shown below
        print('Position #1: ',numbers['Pos1']) #these could be nested but this is how you access the keys in the dict - row headers to us
        print('Position #2: ',numbers['Pos2'])
        print('Position #3: ',numbers['Pos3'])
        print('Position #4: ',numbers['Pos4'])
        print('Position #5: ',numbers['Pos5'])
        print('Position #6: ',numbers['Pos6'])


    randomword=random.choice(wordlist)  #chooses one of the words randomly in the list to use as search criteria for the joke - to illustrate how i do params in sql

    sql="SqlSlack_jokes_per_word @word='{}'".format(randomword)  #note the double qoutes and the single inside qoutes - the {} is a placeholder in python .format will send in what ya want

    jokes=connection(3,sql)
    print(jokes) #this prints the list of dictionaries of jokes.
    for count, joke in enumerate(jokes): #enumerate is awesome - makes what ever count in this case the counter variable
        print(joke)     #this will print the current entire dictionary that has been peeled out of the list
        print('\nJoke number: ',count)   #this prints your counter
        print('\nJoke: ', joke['JokeCategory'])
        print('*'*100,'Joke: ',joke['Joke'],'*'*100,'\n\n')


