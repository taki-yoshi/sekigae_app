from fastapi import FastAPI
import random

import schemas
import DA_matching


app = FastAPI()

@app.get('/')
async def read_root():
    return {'message': '席替え'}

@app.post('/seats_changed/', response_model=schemas.Response)
async def sekigae(request: schemas.Request):
    students = request.students
    for student in students:
        students=[DA_matching.Student(name,preference) for name,preference in student.items()]
        student_list=[name for name in student.keys()]#席側の選好順序をランダムで決める

    # print(student_list)
    seats_sum=request.seats_sum
    seats_preference=random.sample(student_list,len(student_list))
    # print(seats_preference)
    seats=[DA_matching.Seki(str(name),seats_preference) for name in range(1,seats_sum+1)]

    return schemas.Response(changed_seats=DA_matching.matching(students,seats))
