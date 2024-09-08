const fields = {
    "water": {
        slider: document.getElementById("water-avail"),
        desc: document.getElementById("water-desc"),
        disabler: document.getElementById("water-ignore"),
        title: "Water Score",
        descs: {
            zero:"No water available",
            one: "Potential for water",
            two: "Water in non-liquid form",
            three: "Liquid water available",
        },
    },
    "atmo": {
        slider: document.getElementById("atmo"),
        desc: document.getElementById("atmo-desc"),
        disabler: document.getElementById("atmo-ignore"),
        title: "Atmosphere Score",
        descs: {
            zero:"No atmosphere or toxic to life",
            one: "Thin atmosphere lacking pressure or composition",
            two: "Atmosphere present but not Earthlike",
            three: "Earthlike Atmosphere",
        },
    },
    "temp": {
        slider: document.getElementById("temp-range"),
        desc: document.getElementById("temp-desc"),
        disabler: document.getElementById("temp-ignore"),
        title: "Temperature Score",
        descs: {
            zero:"Extreme cold or heat (200+°C or -50°C and below)",
            one: "Very high heat or cold (100°C to 200°C and -50°C to -25°C)",
            two: "Marginally suitable temperature (50°C to 100°C and 0°C to -25°C",
            three: "Optimal temperature (0°C to 50°C)",
        },
    },
    "geo": {
        slider: document.getElementById("geo-activity"),
        desc: document.getElementById("geo-desc"),
        disabler: document.getElementById("geo-ignore"),
        title: "Geological Score",
        descs: {
            zero:"No geological activity",
            one: "Low geological activity",
            two: "Moderate geological activity",
            three: "High geological activity",
        },
    },
    "mag": {
        slider: document.getElementById("mag-field"),
        desc: document.getElementById("field-desc"),
        disabler: document.getElementById("mag-field-ignore"),
        title: "Magnetic Score",
        descs: {
            zero:"No magnetic field",
            one: "Low strength magnetic field",
            two: "Moderate strength magnetic field",
            three: "Strong magnetic field",
        },
    },
    "star": {
        slider: document.getElementById("star-stabl"),
        desc: document.getElementById("star-desc"),
        disabler: document.getElementById("star-stabl-ignore"),
        title: "Star Score",
        descs: {
            zero:"Highly variable or end-of-life star",
            one: "Unstable star with significance variance",
            two: "Stable with slight variance (may be slight off main sequence)",
            three: "Main sequence star with stable output",
        },
    },
    "orbit": {
        slider: document.getElementById("orbit-stabl"),
        desc: document.getElementById("orbit-desc"),
        disabler: document.getElementById("orbit-stabl-ignore"),
        title: "Orbit Score",
        descs: {
            zero:"Highly variable and unstable orbit",
            one: "Variable and eccentric orbit",
            two: "Elliptical but stable orbit",
            three: "Near-Circular orbit",
        },
    }
}

for(const key of Object.keys(fields)) {
    let currVal = fields[key].slider.value;
    fields[key].slider.addEventListener("input", () => {
        fields[key].desc.innerText = fields[key].title + ": " + fields[key].slider.value + getDescription(fields[key].slider.value, fields[key].descs);
        currVal = fields[key].slider.value;
    });
    fields[key].disabler.addEventListener("change", (e) => {
        if (e.currentTarget.checked) {
            fields[key].slider.value = -1;
            fields[key].slider.disabled = true;
        } else {
            fields[key].slider.value = currVal;
            fields[key].slider.disabled = false;
        }
    });
}

function getDescription(val, descs) {
    let base = " - ";
    if(val == 0) base += descs.zero;
    else if(val == 1) base += descs.one;
    else if(val == 2) base += descs.two;
    else if(val == 3) base += descs.three;
    return base;
}

let submitted = false;

document.getElementById("submit").addEventListener("click", (e) => {
    document.getElementById("loading-text").innerText = "Loading! Might take a little bit...";
    // if(!submitted) {
    //     e.preventDefault();
    //     for(const key of Object.keys(fields)) {
    //         if(fields[key].slider.disabled == true) {
    //             fields[key].slider.disabled = false;
    //             fields[key].slider.value = -1;
    //         }
    //     }
    //     submitted = true;
    //     document.getElementById("submit").click();
    // }
});