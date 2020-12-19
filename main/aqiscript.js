const aqi = document.getElementById("aqi_int").innerHTML

if (aqi > 300) {
    document.getElementById("b1").style.background = "#510255";
    document.getElementById("aqi_text").innerHTML = "The air quality is hazardous.";
} else if (aqi > 200) {
    document.getElementById("b1").style.background = "#ad72e4";
    document.getElementById("aqi_text").innerHTML = "The air quality is very unhealthy.";
} else if (aqi > 150) {
    document.getElementById("b1").style.background = "#b53838";
    document.getElementById("aqi_text").innerHTML = "The air quality is unhealthy.";
} else if (aqi > 100) {
    document.getElementById("b1").style.background = "#e4a772";
    document.getElementById("aqi_text").innerHTML =
    "The air quality is unhealthy for sensitive groups.";
} else if (aqi > 50) {
    document.getElementById("b1").style.background = "#e4e172";
    document.getElementById("aqi_text").innerHTML = "The air quality is moderate.";
} else if (aqi > 0) {
    document.getElementById("b1").style.background = "#a9e296";
    document.getElementById("aqi_text").innerHTML = "The air quality is good.";
};