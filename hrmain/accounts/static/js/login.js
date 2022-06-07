document.addEventListener("DOMContentLoaded",()=>{
    const userLoginForm=document.querySelector("#user-login");
    const adminLoginForm=document.querySelector("#admin-login");

    document.querySelector("#linkUserLogin").addEventListener("click", (e)=>{
        e.preventDefault();
        userLoginForm.classList.remove("form-hidden");
        adminLoginForm.classList.add("form-hidden");
    });

    document.querySelector("#linkAdminLogin").addEventListener("click",(e)=>{
        e.preventDefault();
        userLoginForm.classList.add("form-hidden");
        adminLoginForm.classList.remove("form-hidden");
        adminLoginForm.style.backgroundColor = "rgba(124, 154, 189,0.8)";
        document.getElementById("submit-btn").style.backgroundColor = "rgb(110, 166, 239);";

        

    });
});

