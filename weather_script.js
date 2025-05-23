const fetch = require('node-fetch');

const API_KEY = 'cf5a0745aafecfc67917ab4cb6c5df77; // Replace with your OpenWeatherMap API key
const CITY = 'London';
const URL = `https://api.openweathermap.org/data/2.5/weather?q=${CITY}&appid=${API_KEY}&units=metric`;

async function getWeather() {
    try {
        const response = await fetch(URL);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(`Weather in ${CITY}: ${data.weather[0].description}, Temperature: ${data.main.temp}°C`);
    } catch (error) {
        console.error('Error fetching weather data:', error.message);
    }
}

getWeather();