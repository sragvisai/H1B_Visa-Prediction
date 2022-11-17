
import fetch from "node-fetch";
import express from 'express';

const app = express();
const port = 9000;

//cors
import cors from 'cors';
app.use(cors());
// routes will go here

app.get('/server', function(req, response) {
    console.log(JSON.stringify(req.query.inputData));
    const paramss = JSON.stringify(req.query.inputData);
    var url = new URL("http://127.0.0.1:8000");
    url.search = new URLSearchParams({input_data : paramss});
    url = url.toString();
    console.log("The URL trying to connect"+url);
    fetch(url, {
        method : 'POST',
        //body : paramss,  
    })
        .then((res) => {
            console.log("Response " +JSON.stringify(res));
            response.send(res);
        });
  });

app.listen(port);
console.log('Server started at http://localhost:' + port);