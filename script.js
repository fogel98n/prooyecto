// Clave API de ThingSpeak y Channel ID
const API_KEY = 'F3JXY98XMVNZEU9S'; // Reemplaza con tu API Key
const CHANNEL_ID = '2867183'; // Reemplaza con tu Channel ID

// URL para obtener datos del campo 1 (puedes cambiar el número del campo si es necesario)
const url = `https://api.thingspeak.com/channels/${CHANNEL_ID}/feeds.json?api_key=${API_KEY}&results=1`;

// Función para obtener datos de ThingSpeak
async function obtenerDatos() {
    try {
        const response = await fetch(url);
        const data = await response.json();

        if (data.feeds && data.feeds.length > 0) {
            const ultimoDato = data.feeds[0];
            document.getElementById('data').innerHTML = `
                <p><strong>Último valor recibido: </strong> ${ultimoDato.field1}</p>
                <p><strong>Fecha de actualización: </strong> ${ultimoDato.created_at}</p>
            `;
        } else {
            document.getElementById('data').innerHTML = '<p>No se encontraron datos.</p>';
        }
    } catch (error) {
        console.error('Error al obtener los datos:', error);
        document.getElementById('data').innerHTML = '<p>Error al obtener los datos.</p>';
    }
}

// Llamar a la función para obtener los datos cuando se carga la página
window.onload = obtenerDatos;

