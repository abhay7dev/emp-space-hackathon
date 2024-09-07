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
            zero:"No Atmosphere or toxic",
            one: "",
            two: "",
            three: "",
        },
    },
    "temp": {
        slider: document.getElementById("temp-range"),
        desc: document.getElementById("temp-desc"),
        disabler: document.getElementById("temp-ignore"),
        title: "Temperature Score",
        descs: {
            zero:"Extreme cold or heat (200+°C or -50°C and below)",
            one: "",
            two: "",
            three: "",
        },
    },
    "geo": {
        slider: document.getElementById("geo-activity"),
        desc: document.getElementById("geo-desc"),
        disabler: document.getElementById("geo-ignore"),
        title: "Geological Score",
        descs: {
            zero:"No geological activity",
            one: "",
            two: "",
            three: "",
        },
    },
    "mag": {
        slider: document.getElementById("mag-field"),
        desc: document.getElementById("field-desc"),
        disabler: document.getElementById("mag-field-ignore"),
        title: "Magnetic Score",
        descs: {
            zero:"No magnetic field",
            one: "",
            two: "",
            three: "",
        },
    },
    "star": {
        slider: document.getElementById("star-stabl"),
        desc: document.getElementById("star-desc"),
        disabler: document.getElementById("star-stabl-ignore"),
        title: "Star Score",
        descs: {
            zero:"Unstable star",
            one: "",
            two: "",
            three: "",
        },
    },
    "orbit": {
        slider: document.getElementById("orbit-stabl"),
        desc: document.getElementById("orbit-desc"),
        disabler: document.getElementById("orbit-stabl-ignore"),
        title: "Orbit Score",
        descs: {
            zero:"Unstable orbit",
            one: "",
            two: "",
            three: "",
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