var menu1 = document.getElementById("principal")
var menu2 = document.getElementById("agregar")
var menu3 = document.getElementById("registrar")
var volver1 = document.getElementById("volver1")
var volver2 = document.getElementById("volver2")
var boton_registar = document.getElementById("boton_registrar")
var boton_agregar = document.getElementById("boton_agregar")

function mostrar(a,b){
    a.style.display = "none"
    b.style.display = "flex"
}

boton_agregar.onclick = ()=>{mostrar(menu1,menu2)}
boton_registar.onclick = ()=>{mostrar(menu1, menu3)}
volver1.onclick = ()=>{mostrar(menu2, menu1) }
volver2.onclick = ()=>{mostrar(menu3, menu1) }