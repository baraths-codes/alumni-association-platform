const Role = prompt("Student / Alumini ?");

function Alumini() {
    document.getElementById("UserTitle").textContent = "Alumini";
    document.getElementById("CollegeLable").textContent = "Studied College:";
    document.getElementById("CurrentStatus").textContent= "Working at Tata Consultancy Services, Chennai";
    document.getElementById("Profession").textContent = "Full-Stack Web Developer";
} 

if (Role == "Alumini" ) {
    console.log("Alumini")
    Alumini();
}
else {
    console.log("Student");
}