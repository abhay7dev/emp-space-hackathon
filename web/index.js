import express from "express";
const app = express();

import { marked } from "marked";

import { spawn } from "child_process";

const nasa_api_key = process.env.NASA_API_KEY;
const pyPath = process.env.PY_PATH || "../backend-python/env/bin/python";

const callPyProcess = async (res, args) => {
    const pythProcess = spawn("../backend-python/env/bin/python", ["../backend-python/main.py", ...args]);
    pythProcess.stdout.on("data", async (dat) => {
        
        let final = "";
        let survivability = "";
        let loops = 0;
        for(let tok of (dat + "").split("\n")) {
            if(loops == 0) {
                survivability += tok;
            } else {
                if(tok.startsWith("##")) tok += "\n";
                final += tok + "<br>";
            }
            loops++;
        }
        const pic = await getPic();
        res.render("info", { output: { survivability: survivability, final: marked.parse(final) }, pic });
    });

    pythProcess.stderr.on("data", async (dat) => {
        const pic = await getPic();
        res.render("info", { output: "Error", pic });
    });
}

const getPic = async() => {
    try {
        const val = (await (await fetch("https://api.nasa.gov/planetary/apod?api_key=" + nasa_api_key)).json());
        return val.hdurl;
    } catch(err) {
        return "";
    }
}

app.set("view engine", "ejs");

app.get("/", (req, res) => {
    res.render("index");
});

app.use(express.urlencoded({ extended: true }));

app.post("/get-planet-score", async (req, res) => {
    const vals = [
        req.body["water-ignore"] == "on" ? "-1" : req.body["water-avail"],
        req.body["atmo-ignore"] == "on" ? "-1" : req.body["atmo"],
        req.body["temp-ignore"] == "on" ? "-1" : req.body["temp-range"],
        req.body["geo-ignore"] == "on" ? "-1" : req.body["geo-activity"],
        req.body["mag-field-ignore"] == "on" ? "-1" : req.body["mag-field"],
        req.body["star-stabl-ignore"] == "on" ? "-1" : req.body["star-stabl"],
        req.body["orbit-stabl-ignore"] == "on" ? "-1" : req.body["orbit-stabl"],
    ];
    console.log(vals)
    await callPyProcess(res, vals);
});

app.use(express.static("public"));

app.use((_, res) => {
    res.status(404).render("error");
});

app.listen(8080, () => {
    console.log("Listening at http://localhost:8080");
});