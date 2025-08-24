try :
    f = open("ToDolist.txt", encoding='utf-8')     
except:
    print("An Error acoured finding the file creating an file instead all saved data will be lost")
    with open("ToDolist.txt", "x", encoding='utf-8') as f:
        print("done!")

def format_completed(task):# ads stripe this is in testing
    strikethrough_text = ''.join([char + '\u0336' for char in task.strip()])
    return f"✓ {strikethrough_text}\n"
   


while True :
    print("====== To DO List ======\n 1 to add sumthing new \n 2 to view list \n 3 to check a task off \n 4 to remove task\n 5 to stop")
    answ = input(": ")
    

    if answ == "1":#add a new todo
        content= input("what needs to be done :  ")
        print(content+"\n")
        try:
            with open("ToDolist.txt", "a", encoding='utf-8') as f:
                f.write(content+"\n")
            print("Content added\nremember todo",content)
        except:
            print("An error acourded while trying to write content")
    elif answ =="2":#see the file /task
        try:
            with open("ToDolist.txt", "r", encoding='utf-8') as f:
                print(f.read())
        except:
            print("An error acourded while trying to read content")

    elif answ == "3":#check sumthing ooff
        newfile=''
        try:
             with open("ToDolist.txt", "r", encoding='utf-8') as f:
               count=0
               num =''
               for i in f:
                   count=count+1
                   print(str(count)+":  "+i)
      
        except:
             print("An error acourded while trying to check the task off")

        num = input("use the list number to choose what to mark as complete :   ")
        count = 0
        with open("ToDolist.txt", "r", encoding='utf-8') as f:  
            for i in f:
                 count+=1
                 if count ==(int(num)) :
                    print(str(count)+":  "+format_completed(i))
                    newfile=newfile+format_completed(i)
                 else: 
                     print(str(count)+":  "+(i))
                     newfile=newfile+i
                
        with open("ToDolist.txt", "w", encoding='utf-8') as f:
            f.write(newfile)

    elif answ == "4":#remove a task
        newfile=''
        try:
             with open("ToDolist.txt", "r", encoding='utf-8') as f:
               count=0
               num =''
               for i in f:
                   count=count+1
                   print(str(count)+":  "+i)
      
        except:
             print("An error acourded while trying to check the task off")
        num = input("use the list number to choose what to mark as complete :   ")
        count = 0
        newcount =0
        with open("ToDolist.txt", "r", encoding='utf-8') as f:  
            for i in f:
                 count+=1
                 
                 if count ==(int(num)) :
                    print("Deleted")
                    newcount=count-1
                 else: 
                     newcount=newcount+1
                     print(str(count)+":  "+(i))
                     newfile=newfile+i
                
        with open("ToDolist.txt", "w", encoding='utf-8') as f:
            f.write(newfile)

    elif answ == "5":#remove a task
        break
