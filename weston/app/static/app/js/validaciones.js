$(document).ready(function () {

	

	/* Validaciones registro*/
	$('#form_reg').submit(function (e) {
		
		var nombre = $('#nombre').val();
		var celu = $('#telefono').val();
		var clave = $('#clave1').val();
		var clave2 = $('#clave2').val();



		let msjClaves = '';
		let entrar = false;

		$("#msjNom").html("");
        $("#msjCorreo").html("")
        $("#msjTel").html("");
        $("#msjClave").html("");


		//VALIDACIONES NOMBRE
		if (nombre.trim().length < 3 || nombre.trim().length > 25) {
			
			$("#msjNom").html("El nombre no tiene la longitud válida <br>");
			entrar = true;
			

		}

		if(/[0-9]/.test(nombre)){
			
            $("#msjNom").html("El nombre no puede contener digitos <br>");
            entrar = true;
			
        }

		//NO ESTOY MUY SEGURO DE ESTA VALIDACION PERO POR LO QUE EH PROBADO SIRVE
		if(nombre.charAt(0) === (nombre.charAt(0).toUpperCase())){
			$("#msjNom").html("La primera letra debe tener su inicial mayuscula <br>");
            entrar = true;
		}else{
			
			
			
		}
		//FIN VALIDACIONES NOMBRE

		//-----------------------//

		//VALIDACIONES CLAVE
		if (clave.trim().length < 6) {
			msjClaves += "La contraseña de tener al menos 6 caracteres <br>";
			entrar = true;
			
		}

		if (clave != clave2) {
			msjClaves += "Las contraseñas deben ser iguales <br>";
            entrar = true;
			
			
        }
		if(!/[A-Z]/.test(clave)){
		msjClaves += "La contraseña de tener al menos 1 mayúscula <br>";
		entrar = true;
		
        }

		if(!/[0-9]/.test(clave)){
			msjClaves += "La contraseña de tener al menos 1 número <br>";
            entrar = true;
			
        }
		//FIN VALIDACIONES CLAVE

		//-----------------------//

		//VALIDACIONES CONTACTO
		if (celu.trim().length != 9) {
			$("#msjTel").html("Número de teléfono debe ser de 9 dígitos");
			entrar = true;
			
		}
		//FIN VALIDACIONES CELULAR

		//-----------------------//
		if (entrar) {
			$('#msjClave').html(msjClaves);
			e.preventDefault();
		} else {
			
		}
	});

	
	/* Validaciones de editar usuario */
	$('#form-edit').submit(function (e) {
		
		var dir = $('#direccion').val();
		var celu = $('#contacto').val();
		var mensaje = '';

		let entrar = false;

		$("#msjDir").html("");
        $("#msjTel").html("");

		//VALIDACIONES DIRECCION
		if (dir.trim().length < 8 || dir.trim().length > 30) {
			$("#msjDir").html("El pasaje debe tener un largo minimo de 8 y maximo de 30.<br>");
			entrar = true;
			e.preventDefault();
		}

		if(!/[a-z]/.test(dir) && (!/[A-Z]/.test(dir))){
            $("#msjDir").html("la direccion no contiene caracteres. <br>");
            entrar = true;
			e.preventDefault();
        }

		//FIN VALIDACIONES DIRECCION

		//-----------------------//

		//VALIDACIONES CONTACTO
		if (celu.trim().length != 9) {
			$("#msjTel").html("Número de teléfono debe ser de 9 dígitos. <br>")
			entrar = true;
		}
		//FIN VALIDACIONES CELULAR

		//-----------------------//

		if (entrar) {
			$('#msjClave').html(msjClaves);
			e.preventDefault();
		} else {			
		}
	});

	 // FORMULARIO CAMBIAR CONTRASEÑA
	 $("#cambiarClave").submit(function (e) {

        var clave = $("#claveActual").val();
        var claveNu1 = $("#claveNueva1").val();
        var claveNu2 = $("#claveNueva2").val();

        let msj = "";
        let entrar = false;

        $("#mensajes").css({ 'color': 'red' });
        $("#mensajes").html("");

        if (claveNu1.trim().length < 6) {
            msj += "La contraseña nueva de tener al menos 6 caracteres <br>";
            entrar = true;
        } if (!/[A-Z]/.test(claveNu1)) {
            msj += "La contraseña nueva de tener al menos 1 mayúscula <br>";
            entrar = true;
        } if (!/[0-9]/.test(claveNu1)) {
            msj += "La contraseña nueva de tener al menos 1 número <br>";
            entrar = true;
        } if (/[ ]/.test(claveNu1)) {
            msj += "La contraseña nueva no debe tener espacios <br>";
            entrar = true;
        } if (claveNu1 == clave) {
            msj += "Las contraseñas nuevas deben ser distinta a la contraseña antigua <br>"
            entrar = true;
        } if (claveNu1 != claveNu2) {
            msj += "Las contraseñas nuevas deben ser iguales <br>"
            entrar = true;
        }

        if (entrar) {
            $("#warnings").html(msj);
            e.preventDefault();
        } else {
        }
    })

	/* Validaciones agregar producto */
	$('#form_agregar').submit(function (e) {
		
		var nombre = $('#nombre_prod').val();
		var precio = $('#precio_prod').val();
		var descripcion = $('#descripcion').val();
		var descripcionCorta = $('#descripcionCorta').val();
		var categoria = $('#categoria').val();
		var mensaje = '';

		let entrar = false;

		//VALIDACIONES NOMBRE
		if (nombre.trim().length < 4 || nombre.trim().length > 25) {
			mensaje += 'El nombre del producto debe tener 4 caracteres como mínimo y máximo 25. <br>';
			entrar = true;
			e.preventDefault();
		}

		if(/[0-9]/.test(nombre)){
            mensaje += "El nombre del producto no puede tener digitos. <br>"
            entrar = true;
			e.preventDefault();
        }

		//NO ESTOY MUY SEGURO DE ESTA VALIDACION PERO POR LO QUE EH PROBADO SIRVE
		if(nombre.charAt(0) === (nombre.charAt(0).toUpperCase())){

		}else{
			mensaje += "El nombre del producto debe tener la primera letra Mayuscula. <br>"
            entrar = true;
			e.preventDefault();
		}
		//FIN VALIDACIONES NOMBRE

		//-----------------------//

		//VALIDACIONES PRECIO
		if (precio <= 0) {
			mensaje += 'El precio debe ser mayor a 0.<br>';
			entrar = true;
			e.preventDefault();
		}
		//FIN VALIDACIONES PRECIO

		//-----------------------//
		
		//VALIDACIONES DESCRIPCION
		if (descripcion.length < 10 || descripcion.length > 120) {
			mensaje += 'La descripción debe ser mayor a 10 y menor a 120 caracteres.<br>';
			entrar = true;
			e.preventDefault();
		}

		//NO ESTOY MUY SEGURO DE ESTA VALIDACION PERO POR LO QUE EH PROBADO SIRVE
		if(descripcion.charAt(0) === (descripcion.charAt(0).toUpperCase())){

		}else{
			mensaje += "La descripción del producto debe tener la primera letra Mayuscula. <br>"
            entrar = true;
			e.preventDefault();
		}
		//FIN VALIDACIONES DESCRIPCION

		//-----------------------//
		
		//VALIDACIONES DESCRIPCION CORTA
		if (descripcionCorta.length < 10 || descripcionCorta.length > 20) {
			mensaje += 'La descripción corta debe ser mayor a 10 y menor a 20 caracteres.<br>';
			entrar = true;
			e.preventDefault();
		}

		//NO ESTOY MUY SEGURO DE ESTA VALIDACION PERO POR LO QUE EH PROBADO SIRVE
		if(descripcionCorta.charAt(0) === (descripcionCorta.charAt(0).toUpperCase())){

		}else{
			mensaje += "La descripción corta del producto debe tener la primera letra Mayuscula. <br>"
            entrar = true;
			e.preventDefault();
		}
		//FIN VALIDACIONES descripcionCorta

		//-----------------------//

		if (entrar) {
			$('#warnings').html(mensaje);
		} else {
			$('#warnings').html('Producto agregado correctamente');
		}
	});

	/* Validaciones modificar producto */

	$('#form_modprod').submit(function (e) {
		
		var nombre = $('#nombre').val();
		var precio = $('#precio').val();
		var descripcion = $('#descripcion').val();
		var descripcionCorta = $('#descripcionCorta').val();
		var mensaje = '';

		let entrar = false;

		//VALIDACIONES NOMBRE
		if (nombre.trim().length < 4 || nombre.trim().length > 25) {
			mensaje += 'El nombre del producto debe tener 4 caracteres como mínimo y máximo 25. <br>';
			entrar = true;
			e.preventDefault();
		}

		if(/[0-9]/.test(nombre)){
            mensaje += "El nombre del producto no puede tener digitos. <br>"
            entrar = true;
			e.preventDefault();
        }

		//NO ESTOY MUY SEGURO DE ESTA VALIDACION PERO POR LO QUE EH PROBADO SIRVE
		if(nombre.charAt(0) === (nombre.charAt(0).toUpperCase())){

		}else{
			mensaje += "El nombre del producto debe tener la primera letra Mayuscula. <br>"
            entrar = true;
			e.preventDefault();
		}
		//FIN VALIDACIONES NOMBRE

		//-----------------------//

		//VALIDACIONES PRECIO
		if (precio <= 0) {
			mensaje += 'El precio debe ser mayor a 0.<br>';
			entrar = true;
			e.preventDefault();
		}
		//FIN VALIDACIONES PRECIO

		//-----------------------//

		//VALIDACIONES DESCRIPCION
		if (descripcion.length < 10 || descripcion.length > 120) {
			mensaje += 'La descripción debe ser mayor a 10 y menor a 120 caracteres.<br>';
			entrar = true;
			e.preventDefault();
		}

		//NO ESTOY MUY SEGURO DE ESTA VALIDACION PERO POR LO QUE EH PROBADO SIRVE
		if(descripcion.charAt(0) === (descripcion.charAt(0).toUpperCase())){

		}else{
			mensaje += "La descripción del producto debe tener la primera letra Mayuscula. <br>"
            entrar = true;
			e.preventDefault();
		}
		//FIN VALIDACIONES DESCRIPCION

		//VALIDACIONES DESCRIPCION CORTA
		if (descripcionCorta.length < 10 || descripcionCorta.length > 20) {
			mensaje += 'La descripción corta debe ser mayor a 10 y menor a 20 caracteres.<br>';
			entrar = true;
			e.preventDefault();
		}

		//NO ESTOY MUY SEGURO DE ESTA VALIDACION PERO POR LO QUE EH PROBADO SIRVE
		if(descripcionCorta.charAt(0) === (descripcionCorta.charAt(0).toUpperCase())){

		}else{
			mensaje += "La descripción corta del producto debe tener la primera letra Mayuscula. <br>"
            entrar = true;
			e.preventDefault();
		}
		//FIN VALIDACIONES descripcionCorta

		//-----------------------//

		if (entrar) {
			$('#warnings').html(mensaje);
		} else {
			$('#warnings').html('Producto agregado correctamente');
		}
	});




	
});
