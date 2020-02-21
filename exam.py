from tkinter import*

root=Tk()
root.title('Exam')
root.configure(background='Light blue')

frame=LabelFrame(root,text='',padx=5,pady=5)
frame.pack(padx=10,pady=10)

#write the questions
question1=Label(frame,text='1. What is the color of an apple?',bg='Yellow')
question1.grid(row=0,column=0)
question2=Label(frame,text='2. What is the color of a banana?',bg='light green')
question2.grid(row=3,column=0)
question3=Label(frame,text='3. What is the color of an orange?',padx=30,bg='light green')
question3.grid(row=0,column=1)
question4=Label(frame,text='4. What is the color of gold?',bg='Yellow')
question4.grid(row=3,column=1)
#put the questions in a list
questionlist=[question1,question2,question3,question4]

#this function tells the result
def final_result():
    s = var1.get()
    s2 = var2.get()
    s3 = var3.get()
    s4 = var4.get()
    
    if s == 1:
        count = 1
    else:
        count=0
    if s2==1:
        count +=1
    if s3 == 1:
        count += 1
    if s4 == 1:
        count += 1

    label2 = Label(frame, text='You got ' + str(count) + ' out of ' + str(len(questionlist)) + ' questions correct!',bg='Red')
    label2.grid(row=9, column=0,columnspan=2)

#create the checkboxes for question 1
var1=IntVar()
checkbox1=Checkbutton(frame,text='Red',variable=var1)
checkbox1.grid(row=1,column=0)
checkbox2=Checkbutton(frame,text='Green')
checkbox2.grid(row=2,column=0)

#create the checkboxes for question 2
var2=IntVar()
checkbox3=Checkbutton(frame,text='Purple')
checkbox3.grid(row=4,column=0)
checkbox4=Checkbutton(frame,text='Yellow',var=var2)
checkbox4.grid(row=5,column=0)

#create the checkboxes for question 3
var3=IntVar()
checkbox4=Checkbutton(frame,text='Blue')
checkbox4.grid(row=1,column=1)
checkbox5=Checkbutton(frame,text='Orange',var=var3)
checkbox5.grid(row=2,column=1)

#create the checkboxes for question 4
var4=IntVar()
checkbox6=Checkbutton(frame,text='Gold',var=var4)
checkbox6.grid(row=4,column=1)
checkbox7=Checkbutton(frame,text='Silver')
checkbox7.grid(row=5,column=1)

#create the submit button
btn3=Button(frame,text='Submit Exam',command=final_result)
btn3.grid(row=8,column=0,columnspan=3)


root.mainloop()