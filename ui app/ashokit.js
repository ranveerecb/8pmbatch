function checkRegFormData(){
    var userid = regform.name1.value
    if (userid == "") {
        alert('Please inter userid')
        return false
    }
    else {
        alert('Valid Data')
        return true
    }
}
function clearRegFormData(){
    var v=confirm('Are you sure to delete ?')
    if(v==true){
        return true
    }
}
function checkLoginFormData() {
    //1.Get userid & data from html form
    var userid = loginform.name1.value
    var pswd = loginform.name2.value
    //2.Check userid & pswd data is empty or not & send alart msg
    if (userid == "") {
        //alert('Please inter userid')
        document.getElementById('s1').innerHTML='* Please enter userid'
        return false
    }
    if (pswd == "") {
        //alert('Please inter password')
        document.getElementById('s2').innerHTML='* Please enter password'
        return false
    }
    else {
        alert('Valid Data')
        return true
    }
}
function clearLoginFormData() {
    var v=confirm('Are you sure to delete ?')
    if(v==true){
        return true
    }
}