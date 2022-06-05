var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var productoId = this.dataset.producto
        var action = this.dataset.action
        console.log('productoId: ', productoId, 'Action: ', action)

        console.log('USER:', user)
        if(user === 'AnonymousUser'){
            console.log("No estas conectado")
        }
        else{
            actualizarCompraUsuario(productoId, action)
        }
    })
}

function actualizarCompraUsuario(productoId, action){
    console.log("El usuario esta conectado, enviando data..")

    var url = '/actualizar_producto/'
    
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productoId': productoId, 'action':action})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })
}