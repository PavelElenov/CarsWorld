function validate_password(){
        let pass = document.getElementById('password').value;
        let confirm_pass = document.getElementById('confirm-password').value;

        if (pass !== confirm_pass) {
            document.getElementById('wrong-password').style.color = 'red';
            document.getElementById('wrong-password').innerHTML
              = '☒ Use same password';
            document.getElementById('register').disabled = true;
            document.getElementById('register').style.opacity = (0.4);
        } else {
            document.getElementById('wrong-password').style.color = 'green';
            document.getElementById('wrong-password').innerHTML =
                '🗹 Password Matched';
            document.getElementById('register').disabled = false;
            document.getElementById('register').style.opacity = (1);
        }
}