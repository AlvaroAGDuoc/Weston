$(document).ready(function () {

	

	/* Validaciones registro*/
	$('#form_reg').submit(function (e) {
		
		var nombre = $('#nombre_reg').val();
		var clave = $('#pass_reg').val();
		var clave2 = $('#pass_reg2').val();
		var dir = $('#dir_reg').val();
		var com = $('#comuna').val();
		var celu = $('#celular').val();
		var correo = $('#email_reg').val();
		var mensaje = '';

		let regexEmail = /^\w+([.-]?\w+)@\w+([.-]?\w+)(.\w{2,4})+$/;
		let entrar = false;

		//VALIDACIONES NOMBRE
		if (nombre.trim().length < 3 || nombre.trim().length > 25) {
			
			mensaje += 'El nombre no es valido. <br>';
			entrar = true;
			e.preventDefault();

		}

		if(/[0-9]/.test(nombre)){
			
            mensaje += "El nombre no puede tener digitos. <br>"
            entrar = true;
			e.preventDefault();
        }

		//NO ESTOY MUY SEGURO DE ESTA VALIDACION PERO POR LO QUE EH PROBADO SIRVE
		if(nombre.charAt(0) === (nombre.charAt(0).toUpperCase())){

		}else{
			
			mensaje += "El nombre debe tener la primera letra Mayuscula. <br>"
            entrar = true;
			e.preventDefault();
		}
		//FIN VALIDACIONES NOMBRE

		//-----------------------//

		//VALIDACIONES CLAVE
		if (clave.trim().length < 6) {
			mensaje += 'La clave debe tener un largo minimo de 6. <br>';
			entrar = true;
			e.preventDefault();
		}

		if (clave != clave2) {
			mensaje += "Las claves no coinciden. <br>"
            entrar = true;
			e.preventDefault();
			
			if(!/[A-Z]/.test(clave)){
        }
		mensaje += "La clave no contiene una mayuscula. <br>"
		entrar = true;
		e.preventDefault();
        }

		if(!/[0-9]/.test(clave)){
			mensaje += "La clave no contiene un digito. <br>"
            entrar = true;
			e.preventDefault();
        }
		//FIN VALIDACIONES CLAVE

		//-----------------------//

		//VALIDACIONES EMAIL
		if (!regexEmail.test(correo)) {
			mensaje += 'El email no es valido. <br>';
			entrar = true;
			e.preventDefault();
		}
		//FIN VALIDACIONES EMAIL

		//-----------------------//

		//VALIDACIONES DIRECCION
		if (dir.trim().length < 8 || dir.trim().length > 30) {
			mensaje += 'El pasaje debe tener un largo minimo de 8 y maximo de 30.<br>';
			entrar = true;
			e.preventDefault();
		}

		if(!/[a-z]/.test(dir) && (!/[A-Z]/.test(dir))){
			mensaje += "La direccion no contiene caracteres. <br>"
            entrar = true;
            e.preventDefault();
        }
		//FIN VALIDACIONES DIRECCION

		//-----------------------//		

		//-----------------------//

		//VALIDACIONES CONTACTO
		if (celu.trim().length != 9) {
			mensaje += 'El celular debe tener un largo de 9. <br>';
			entrar = true;
			e.preventDefault();
		}
		//FIN VALIDACIONES CELULAR

		//-----------------------//
		if (entrar) {
			
			$('#warnings').html(mensaje);
			Swal.fire({
				titleText: "Hola",
				text: "Mensaje de prueba",
				icon: "success",
				confirmButtonText: "OK",
			});
		} else {
			$('#warnings').html('Registrado correctamente');
		}
	});

	/*Validacion formulario contacto usuario no logeado */
	$('#form-cont').submit(function (e) {
		
		var nombre = $('#nombre_cont').val();
		var correo = $('#correo_cont').val();
		var asunto = $('#msj_cont').val();
		var mensaje = '';

		let regexEmail = /^\w+([.-]?\w+)@\w+([.-]?\w+)(.\w{2,4})+$/;
		let entrar = false;

		//VALIDACIONES NOMBRE
		if (nombre.trim().length < 3 || nombre.trim().length > 25) {
			mensaje += 'El nombre no es valido. <br>';
			entrar = true;
			e.preventDefault();
		}

		if(/[0-9]/.test(nombre)){
            mensaje += "El nombre no puede tener digitos. <br>"
            entrar = true;
			e.preventDefault();
        }

		//NO ESTOY MUY SEGURO DE ESTA VALIDACION PERO POR LO QUE EH PROBADO SIRVE
		if(nombre.charAt(0) === (nombre.charAt(0).toUpperCase())){

		}else{
			mensaje += "El nombre debe tener la primera letra Mayuscula. <br>"
            entrar = true;
		}
		//FIN VALIDACIONES NOMBRE

		//-----------------------//

		//VALIDACIONES EMAIL
		if (!regexEmail.test(correo)) {
			mensaje += 'El email no es valido. <br>';
			entrar = true;
		}
		//FIN VALIDACIONES EMAIL

		//-----------------------//

		//VALIDACIONES ASUNTO
		if (asunto.trim().length < 10 || asunto.trim().length > 100) {
			mensaje += 'El mensaje debe tener un largo minimo de 10 y maximo de 100 caracteres.<br>';
			entrar = true;
		}
		//FIN VALIDACIONES ASUNTO

		//-----------------------//
		if (entrar) {
			$('#warnings').html(mensaje);
		} else {
			$('#warnings').html('Mensaje enviado correctamente');
		}
	});

	/* Validaciones de editar usuario */
	// $('#form-edit').submit(function (e) {
	// 	e.preventDefault();
	// 	var dir = $('#dir_edit').val();
	// 	var com = $('#com_edit').val();
	// 	var celu = $('#celu_edit').val();
	// 	var mensaje = '';

	// 	let entrar = false;

	// 	//VALIDACIONES DIRECCION
	// 	if (dir.trim().length < 8 || dir.trim().length > 30) {
	// 		mensaje += 'El pasaje debe tener un largo minimo de 8 y maximo de 30.<br>';
	// 		entrar = true;
	// 	}

	// 	if(!/[a-z]/.test(dir) && (!/[A-Z]/.test(dir))){
    //         mensaje += "la direccion no contiene caracteres. <br>"
    //         entrar = true;
    //     }
	// 	//FIN VALIDACIONES DIRECCION

	// 	//-----------------------//

	// 	//VALIDACIONES COMUNA
	// 	if (com.trim().length <= 5 || com.trim().length > 20) {
	// 		mensaje += 'La comuna debe tener un largo minimo de 5 y maximo de 20.<br>';
	// 		entrar = true;
	// 	}
	// 	if(!/[a-z]/.test(com) && (!/[A-Z]/.test(com))){
    //         mensaje += "La comuna no contiene caracteres. <br>"
    //         entrar = true;
    //     }
	// 	if(/[0-9]/.test(com)){
    //         mensaje += "La comuna no puede tener digitos. <br>"
    //         entrar = true;
    //     }
	// 	//FIN VALIDACIONES COMUNA

	// 	//-----------------------//

	// 	//VALIDACIONES CONTACTO
	// 	if (celu.trim().length != 9) {
	// 		mensaje += 'El celular debe tener un largo de 9. <br>';
	// 		entrar = true;
	// 	}
	// 	//FIN VALIDACIONES CELULAR

	// 	//-----------------------//

	// 	if (entrar) {
	// 		$('#warnings').html(mensaje);
	// 	} else {
	// 		$('#warnings').html('Cambios aplicados correctamente.');
	// 	}
	// });

	/* Validaciones de cambiar contrasena */

	$('#form-camb').submit(function (e) {
		e.preventDefault();
		var clave = $('#nueva_pass').val();
		var clave2 = $('#nueva_pass2').val();

		var mensaje = '';

		let entrar = false;

		//VALIDACIONES CLAVE
		if (clave.trim().length < 6) {
			mensaje += 'La clave debe tener un largo minimo de 6. <br>';
			entrar = true;
		}

		if (clave != clave2) {
            mensaje += "Las claves no coinciden. <br>"
            entrar = true;
        }

		if(!/[A-Z]/.test(clave)){
            mensaje += "La clave no contiene una mayuscula. <br>"
            entrar = true;
        }

		if(!/[0-9]/.test(clave)){
            mensaje += "La clave no contiene un digito. <br>"
            entrar = true;
        }
		//FIN VALIDACIONES CLAVE

		//-----------------------//

		if (entrar) {
			$('#warnings').html(mensaje);
		} else {
			$('#warnings').html('Cambios aplicados correctamente');
		}
	});

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
