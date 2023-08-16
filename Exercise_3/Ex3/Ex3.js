import {Octokit} from "@octokit/rest";
import fs from 'fs';
import {createObjectCsvWriter} from 'csv-writer'


/*Create an Octokit object and authenticate using a personal token in order to make the RESTfull API call */
const Ex3 = new Octokit ({
    auth: '__MyPersonalAccessToken__',
});

/*Create the csv file */  
const csvfile =  createObjectCsvWriter({
    path : "Ex3.csv",
    header: [
        {id : 'name', title: 'Name'},
        {id : 'full_name', title: 'Full_name'},
        {id : 'id', title: 'Id'}
    ],
})

/* Search for all repos of a Github account (in this instance, my own) */
const data = await Ex3.rest.search.repos ({
    q : 'user:FotisFarm'
})  

/* Get the name, full name and id of each repository */
const items = data.data.items;
var write = [ ];
for (var i of items){
    

    write.push( {name : i.name ,full_name : i.full_name, id : i.id} ); 
   
}

csvfile.writeRecords(write)

