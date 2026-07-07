export default getStudentIdsSum(studentArray){
    let total = 0;
    return studentArray.reduce(student => student.id + total);
}
