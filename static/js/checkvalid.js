function checkvalid(){
	var password = document.getElementById('password').value;
	var confirm = document.getElementById('confirm').value;
	var email = document.getElementById('email').value;
	var reg = /^([a-z0-9_\-]+\.)*[a-z0-9_\-]+@([a-z0-9][a-z0-9\-]*[a-z0-9]\.)+[a-z]{2,6}$/i;
	if (password == confirm && reg.test(email)){
		return true;
		alert("OK");	
	}else{
		if (password != confirm){
			document.getElementById('password').value = "";
			document.getElementById('confirm').value = "";
		}
		if (!reg.test(email)){
			document.getElementById('email').value = "";
		}
		return false;		
	}
	
}
