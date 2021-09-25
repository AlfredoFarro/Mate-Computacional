const encriptar__content = document.querySelector(".encriptar__content");
const encriptar__boton = document.querySelector("#encriptar");
const desencriptar__content = document.querySelector(".desencriptar__content");
const desencriptar__boton = document.querySelector("#desencriptar");



const encriptar=document.querySelector(".encriptar");
const header=document.querySelector(".header");
const desencriptar=document.querySelector(".desencriptar");

encriptar__boton.addEventListener("click", (e)=>{
    console.log("GAAS")
    const overlay = document.createElement("DIV");
    overlay.classList.add("overlay");
    overlay.innerHTML = `<form class="encriptar__content form" action="handle_encrypt" method="post">
    <label for="p_value">Valor de P:</label><br>
    <input type="number" id="P" name="p_value" min="0" required><br>

    <label for="q_value">Valor de Q:</label><br>
    <input type="number" id="Q" name="q_value" min="0" required> <br> 

    <label for="d_value">Valor de D:</label><br>
    <input type="number" id="D" name="d_value" min="0"> <br> 


    <label for="text_value">Texto a encriptar:</label><br>
    <input type="text" id="Text" name="text_value" min="0" required> <br> <br>

    <input type="submit" value="Descargar encriptado">
    <a class="btn-cerrar">X</a>
  </form>`;
  header.appendChild(overlay);
  const cerrarImagen = document.querySelector(".btn-cerrar");

    /* Cuando se presiona se cierra la imagen */
    cerrarImagen.onclick = function () {
        overlay.remove();
    }

  

})
desencriptar__boton.addEventListener("click", (e)=>{
    const overlay = document.createElement("DIV");
    overlay.classList.add("overlay");
    overlay.innerHTML = `<form class="desencriptar__content form" action="handle_decrypt" method="post" enctype=multipart/form-data> 
    <label for="key">Clave privada: </label>
    <input type="number" id="c1" name="C1" min="0" required>
    <input type="number" id="c2" name="C2" min="0" required> <br> <br>
    
    <input type="file" id="archivo" name="filename" required>  <br> <br>
    <input type="submit" value="Mostrar desencriptado">
    <a class="btn-cerrar">X</a>
  </form>
  </form>`;
  header.appendChild(overlay);
  const cerrarImagen = document.querySelector(".btn-cerrar");

    /* Cuando se presiona se cierra la imagen */
    cerrarImagen.onclick = function () {
        overlay.remove();
    }
})
