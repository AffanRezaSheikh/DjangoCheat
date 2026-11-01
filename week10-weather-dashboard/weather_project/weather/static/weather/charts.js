// weather/static/weather/charts.js
// changed: the manual put an HTML demo here (see weather_trends_demo.html).
// A .js file can only hold JavaScript, so this script reads the data that
// dashboard.html outputs with json_script and draws the four charts.

const forecast = JSON.parse(document.getElementById("forecast-data").textContent);
const historical = JSON.parse(document.getElementById("historical-data").textContent);

function drawLineChart(canvasId, labels, label, data, color) {
  const canvas = document.getElementById(canvasId);
  if (!canvas || data.length === 0) return;   // nothing to draw yet

  new Chart(canvas, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [{
        label: label,
        data: data,
        borderColor: color,
        backgroundColor: color,
        fill: false,
        tension: 0.3
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { position: 'top' },
        tooltip: { enabled: true }
      },
      scales: {
        x: { title: { display: true, text: 'Timestamp' } },
        y: { title: { display: true, text: label } }
      }
    }
  });
}

// 5-day forecast
drawLineChart("forecastTempChart",
  forecast.map(p => p.dt_txt), "Temperature (°C)", forecast.map(p => p.temp_c), "red");
drawLineChart("forecastHumidityChart",
  forecast.map(p => p.dt_txt), "Humidity (%)", forecast.map(p => p.humidity), "blue");

// Saved snapshots (history)
drawLineChart("historicalTempChart",
  historical.map(p => p.time), "Temperature (°C)", historical.map(p => p.temp_c), "red");
drawLineChart("historicalWindChart",
  historical.map(p => p.time), "Wind Speed (m/s)", historical.map(p => p.wind_speed), "green");
