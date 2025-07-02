document.getElementById("clienteForm").addEventListener("submit", async function(e) {
  e.preventDefault();

  const id = document.getElementById("id").value;
  const nombre = document.getElementById("nombre").value;
  const telefono = document.getElementById("telefono").value;
  const correo = document.getElementById("correo").value;
  const direccion = document.getElementById("direccion").value;

  let errores = [];

  if (id <= 0) {
    errores.push("El ID debe ser mayor a 0.");
  }

  if (nombre.length === 0 || nombre.length > 50) {
    errores.push("El nombre es obligatorio y debe tener máximo 50 caracteres.");
  }

  if (!/^[0-9]{8,20}$/.test(telefono)) {
    errores.push("El teléfono debe tener entre 8 y 20 dígitos numéricos.");
  }

  if (!correo.includes("@")) {
    errores.push("El correo debe ser válido.");
  }

  if (errores.length > 0) {
    alert(errores.join("\n"));
    return;
  }

  const datos = {
    id,
    nombre,
    telefono,
    correo,
    direccion
  };

  const respuesta = await fetch("http://localhost:5000/guardar_cliente", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(datos)
  });

  const resultado = await respuesta.json();
  alert(resultado.mensaje);
});
