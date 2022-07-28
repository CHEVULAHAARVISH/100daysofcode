def get_data():
    student_data=dict()
    n=int(input())
    if n>=2 and n<=100:
        for i in range(n):
            name,marks=input().split()
            
            if float(marks)<=100:
                student_data[name]=float(marks)
                
    #print(student_data)
    highest_marks=max(student_data.values())
    #print(highest_marks)
    n = [k for k, v in student_data.items() if v == highest_marks]
    for i in range(len(n)):
        print(n[i])

if __name__ == '__main__':
    try:
        test_case=int(input())
        for i in range(test_case):
            get_data()
    except EOFError as e:
        pass