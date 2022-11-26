
import fetch from "node-fetch";
import express from 'express';

//mongoDB realted stuff
import { MongoClient, ServerApiVersion } from 'mongodb';
//import { MongoClient } from 'mongodb';
const uri = "mongodb+srv://admin:Admin@cluster0.20rd07g.mongodb.net/?retryWrites=true&w=majority";
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true, serverApi: ServerApiVersion.v1 });


const app = express();
// View engine setup
app.set('view engine', 'ejs');
app.use(express.static('resources'));

const port = 9000;

//cors
import cors from 'cors';
app.use(cors());

// routes will go here

app.get('/server', function(req, response) {
    //console.log(JSON.stringify(req.query.inputData));
    const paramss = JSON.stringify(req.query.inputData);
    var url = new URL("http://127.0.0.1:8000");
    url.search = new URLSearchParams({input_data : paramss});
    url = url.toString();
    fetch(url, {})
    .then((res) => res.json())
    .then((data) =>{
            //const result = convert.xml2js(data);
            console.log("Data "+data);
            response.json(data);
    });
  });

  app.get('/validateUser',function(req,response){
    let params = req.query.inputData;
    params = params.split(',');
    let userName = params[0];
    let password = params[1];
    let existingUsers = [];
    console.log("Inside the validateUser server "+JSON.stringify(params));
    client.connect(err => {
        const collection = client.db("LoginCreds").collection("Users");
        
        //check if user exists
        collection.distinct('userName').then((data) => {
            if(data.includes(userName)){
                collection.findOne({userName : userName})
            .then((data) =>{
                console.log("Found");
                console.log("ERROR "+JSON.stringify(data));
                console.log("Password "+JSON.stringify(data.password));
                if(data.password != password){
                    response.json("Invalid");
                }
                else
                    response.json("Valid");
                })
            }
            else
                response.json("Invalid");
        });        
        setTimeout(() => {client.close()}, 1500)
      });
  });

  app.get('/addUser',function(req,response){

        let params = req.query.inputData;
        params = params.split(',');
        let userName = params[0];
        let password = params[1];
        console.log("Inside the addUser server "+userName+" "+password);
        client.connect(err => {
            const connection = client.db("LoginCreds").collection("Users");

            //check if user already exists
            connection.distinct('userName')
            .then((data)=>{

                if(data.includes(userName)){
                    response.json("alreadyExists");
                }
                else{
                    connection.insertOne({ userName: userName, password: password }).then( (res) => {
                        console.log("Added user successfully");
                        response.json("succ");
                    });
                }
            })

            setTimeout(() => {client.close()}, 1500);
        })
  });

  //get the employee form
  app.get('/employeeForm' , function(req,response){

        response.render('employeeForm');
  })

  //get the employer form
  app.get('/agentForm',function(req,response){

        response.render('agentForm')
  });

  //login page
  app.get('/',function(req,response){
    response.render('login');
  })

  app.get('/selection',function(req,response){
    response.render('selection');
  })

  app.get('/register',function(req,response){
    response.render('register');
  });

  

app.listen(port);
console.log('Server started at http://localhost:' + port);