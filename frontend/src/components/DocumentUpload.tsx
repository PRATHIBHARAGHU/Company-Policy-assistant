import React,{useState} from "react";
import {uploadDocument} from "../services/DocumentService";


function DocumentUpload(){

const [file,setFile]=useState<File|null>(null);

const [message,setMessage]=useState("");



const upload=async()=>{


if(!file)
return;


try{

const res=await uploadDocument(file);

setMessage(
"Uploaded successfully"
);

console.log(res);


}
catch(err){

console.log(err);

setMessage(
"Upload failed"
);

}


};



return(

<div>

<h2>
Upload Document
</h2>


<input

type="file"

onChange={
e=>setFile(
e.target.files?.[0] || null
)
}

/>


<button onClick={upload}>
Upload
</button>


<p>
{message}
</p>


</div>


)


}


export default DocumentUpload;