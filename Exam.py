from tkinter import*

root=Tk()
root.title('Exam')

#write the questions
question1=Label(root,text='1. What is the color of an apple?')
question1.grid(row=0,column=0)
question2=Label(root,text='2. What is the color of a banana?')
question2.grid(row=5,column=0)
question3=Label(root,text='3. What is the color of an orange?',padx=30)
question3.grid(row=0,column=1)
question4=Label(root,text='4. What is the color of gold?')
question4.grid(row=5,column=1)
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

    label2 = Label(root, text='You got ' + str(count) + ' out of ' + str(len(questionlist)) + ' questions correct!')
    label2.grid(row=11, column=0)

#create the checkboxes for question 1
var1=IntVar()
checkbox1=Checkbutton(root,text='Red',variable=var1)
checkbox1.grid(row=1,column=0)
checkbox2=Checkbutton(root,text='Green')
checkbox2.grid(row=2,column=0)

#create the checkboxes for question 2
var2=IntVar()
checkbox3=Checkbutton(root,text='Purple')
checkbox3.grid(row=6,column=0)
checkbox4=Checkbutton(root,text='Yellow',var=var2)
checkbox4.grid(row=7,column=0)

#create the checkboxes for question 3
var3=IntVar()
checkbox4=Checkbutton(root,text='Blue')
checkbox4.grid(row=1,column=1)
checkbox5=Checkbutton(root,text='Orange',var=var3)
checkbox5.grid(row=2,column=1)

#create the checkboxes for question 4
var4=IntVar()
checkbox6=Checkbutton(root,text='Gold',var=var4)
checkbox6.grid(row=6,column=1)
checkbox7=Checkbutton(root,text='Silver')
checkbox7.grid(row=7,column=1)

#create the submit button
btn3=Button(root,text='Submit Exam',command=final_result)
btn3.grid(row=10,column=0,columnspan=3)


root.mainloop()
