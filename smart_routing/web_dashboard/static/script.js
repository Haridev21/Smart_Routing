// Initialize map after DOM is loaded
window.onload = function() {
    let map = L.map("map").setView([10.0, 76.0], 13);

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19
    }).addTo(map);

    let nodes = [];
    let markers = [];
    let trafficLines = [];

    map.on("click", function(e) {
        let marker = L.marker(e.latlng).addTo(map);
        markers.push(marker);
        nodes.push([e.latlng.lat, e.latlng.lng]);
    });

    function randomTrafficLevel() {
        return Math.random();
    }

    function trafficColor(level) {
        if (level < 0.33) return "green";
        if (level < 0.66) return "yellow";
        return "red";
    }

    async function drawTrafficHeatmap() {
        trafficLines.forEach(line => map.removeLayer(line));
        trafficLines = [];

        if (nodes.length < 2) return;

        for (let i = 0; i < nodes.length - 1; i++) {
            let start = nodes[i];
            let end = nodes[i + 1];

            try {
                let url = `https://router.project-osrm.org/route/v1/driving/${start[1]},${start[0]};${end[1]},${end[0]}?overview=full&geometries=geojson`;
                let res = await fetch(url);
                let data = await res.json();

                let coords = data.routes[0].geometry.coordinates.map(c => [c[1], c[0]]);
                let congestion = randomTrafficLevel();

                let line = L.polyline(coords, {
                    color: trafficColor(congestion),
                    weight: 6,
                    opacity: 0.8
                }).addTo(map);

                trafficLines.push(line);
            } catch (err) {
                console.error("OSRM fetch error:", err);
            }
        }
    }

    document.getElementById("startBtn").onclick = function() {
        if (nodes.length < 2) {
            alert("Add at least 2 nodes");
            return;
        }
        drawTrafficHeatmap();
    };
};
