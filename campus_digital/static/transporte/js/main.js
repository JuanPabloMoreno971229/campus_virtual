function buscarDatos() {
	document.getElementById('buscarBtn').addEventListener('click', buscarDatos);
	let url = `http://localhost:8000/api/mi-modelo/?nombre=${nombre}`;
	fetch(url)
		.then(response => response.json())
		.then(data => {
			let resultados = document.getElementById("resultados");
			resultados.innerHTML = "";
			data.forEach(objeto => {
				let elemento = document.createElement("div");
				elemento.innerHTML = `<p>Nombre: ${objeto.nombre}</p><p>Descripción: ${objeto.descripcion}</p>`;
				resultados.appendChild(elemento);
			});
		})
		.catch(error => console.error(error));
}

function buscarDatos() {
    fetch('/api/horarios/')
      .then(response => response.json())
      .then(data => {
        // Agrega los datos al contenedor de resultados
      });
  }
  function buscarDatos() {
    fetch('/api/horarios/')
      .then(response => response.json())
      .then(data => {
        const resultados = document.getElementById('resultados');
        resultados.innerHTML = '';
  
        data.forEach(horario => {
          const li = document.createElement('li');
          li.innerHTML = `${horario.dia}: ${horario.hora_inicio} - ${horario.hora_fin}`;
          resultados.appendChild(li);
        });
      });
  }
    