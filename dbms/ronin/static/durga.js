function validate(){
    var uname=document.getElementById("uname");
    var pass=document.getElementById("password");
  
    if (uname.value.trim()=="")
    {
      alert("Empty username");
      return false;
    }
    else if(pass.value.trim()=="")
    {
      alert("Empty password");
      return false;
    }
    else if(uname.value.trim().length!==8)
    {
      alert("incorrect username");
      return false;
    }
    else if(pass.value.trim().length!==8)
    {
      alert("incorrect password");
      return false;
    }
    else if(pass.value!==uname.value)
    {
      alert("incorrect  ");
      return false;
    }
  }