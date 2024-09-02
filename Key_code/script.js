const container = document.getElementById("keyContainer");

window.addEventListener("keydown",(e)=>{
    container.innerHTML=generateHTML(e.key,e.code,e.key.charCodeAt(0));


});

function generateHTML(key){

    return
    
    <div class="key-container" >
        <h4>Key</h4>
        <div class="key-content">${key ==" " ? "Space":key}</div> 
    </div> 
;}

function generateHTML(code){

    <div class="key-container" >
       <h4>code</h4>
        <div class="key-content">${code}
        </div> 
   </div> 
;
}

function generateHTML(keyCode){

    <div class="key-container" >
    <h4>keyCode</h4>
    <div class="key-content">${keyCode} </div> 
    </div> 




    ;

}