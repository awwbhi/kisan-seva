// run `node index.js` in the terminal

// console.log(`Hello Node.js v${process.versions.node}!`);


const fetchSoilAnalysis = async () => {
    const state = document.getElementById("state").value;
    const color = document.getElementById("color").value;
    const texture = document.getElementById("texture").value;
    const waterRetention = document.getElementById("waterRetention").value;

    const response = await fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            state: state,
            color: color,
            texture: texture,
            water_retention: waterRetention,
        }),
    });

    const data = await response.json();
    console.log(data);
    // Use data to update your frontend UI
};
