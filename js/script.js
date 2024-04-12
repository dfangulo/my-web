document.addEventListener('DOMContentLoaded', function() {
    const formulario = document.getElementById('formulario');
    const listaNombres = document.getElementById('lista-nombres');
    let registros = { data: [] };
    
    formulario.addEventListener('submit', function(event) {
      event.preventDefault();
      
      const nombreInput = document.getElementById('nombre');
      const name = nombreInput.value.trim();

      const celularInput = document.getElementById('celular');
      const celular = celularInput.value.trim();

      const referenciaInput = document.getElementById('referencia');
      const reference = referenciaInput.value.trim();
      
      if (name !== '' && celular !== '' && reference !== '') {
        const registro = {
          nombre: name,
          celular: enmascararCelular(celular),
          referencia: reference
        };
        registros.data.push(registro);
        guardarRegistros(registros);
        agregarNombre(registro);
        nombreInput.value = '';
        celularInput.value = '';
        referenciaInput.value = '';
      }
    });
    
    function agregarNombre(registro) {
      const li = document.createElement('li');
      li.innerHTML = `<span>${registro.nombre}</span> | <span>${registro.celular}</span> | <span>${registro.referencia}</span>`;
      listaNombres.appendChild(li);
    }

    function enmascararCelular(celular) {
      // Mostrar solo los últimos 3 dígitos del celular
      const enmascarado = '*'.repeat(celular.length - 3) + celular.slice(-3);
      return enmascarado;
    }

    async function guardarRegistros(registros) {
      const jsonData = JSON.stringify(registros);
      try {
        await fetch('js/json/data.json', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: jsonData
        });
        console.log('Registros guardados correctamente.');
      } catch (error) {
        console.error('Error al guardar los registros:', error);
      }
    }
  });
