// import libraries, express for http server, marked for markdown parser, and spawn for calling python backend
import express from "express";
const app = express();

import { marked } from "marked";

import { spawn } from "child_process";

// link to python executable
const nasa_api_key = process.env.NASA_API_KEY;
const pyPath = process.env.PY_PATH || "../backend-python/env/bin/python";

// call the python process with the required variables
const callPyProcess = async (res, args) => {

    // spawn the process
    const pythProcess = spawn("../backend-python/env/bin/python", ["../backend-python/main.py", ...args]);
    
    // parse and send the data base
    pythProcess.stdout.on("data", async (dat) => {

        // parse data properly
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

        // render page
        res.render("info", { output: { survivability: survivability, final: marked.parse(final) } });
    });

    // send error in case of error
    pythProcess.stderr.on("data", async (dat) => {
        res.render("info", { output: "Error", final: "No Output" });
    });
}

// Use ejs engine
app.set("view engine", "ejs");

// Render webpages
app.get("/", (req, res) => {
    res.render("landing");
});
app.get("/test", (req, res) => {
    res.render("index");
});

// Allow express library to parse form data
app.use(express.urlencoded({ extended: true }));

// Accept a POST request which parses the form values and calls the python openai script
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
    //console.log(vals)
    await callPyProcess(res, vals);
});

// serve static files
app.use(express.static("public"));

// render 404 error
app.use((_, res) => {
    res.status(404).render("error");
});

// listen on port 8080
app.listen(8080, () => {
    console.log("Listening at http://localhost:8080");
});