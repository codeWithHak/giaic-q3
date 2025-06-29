def create_dat(total_students,present_students):
    dat = [None] * total_students
    
    for i in range(len(present_students)):
        dat[i] = present_students[i]
         
    print(dat)

present_students = [
    "Huzair", "Huzaifa", "Areeba", "Zayan", "Laiba",
    "Fahad", "Zara", "Talha", "Iqra", "Hamza",
    "Noor", "Ahmed", "Amna", "Bilal", "Fatima"
]
create_dat(total_students=20, present_students=present_students)