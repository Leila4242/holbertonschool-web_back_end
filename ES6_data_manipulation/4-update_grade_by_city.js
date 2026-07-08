export default function updateStudentGradeByCity(studentArray, city, newGrades){
    let spesificArray = studentArray.filter(student => student.location === city)
    spesificArray = spesificArray.reduce((student) => student.grade = 'N/A')
    let ultraspesificArray = spesificArray.filter(student => student.id === newGrades.studentId)
    return ultraspesificArray.reduce((student) => student.grade = newGrades.grade)
}
