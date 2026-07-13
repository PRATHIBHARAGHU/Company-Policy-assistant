import React,{useState} from "react";
import {sendMessage} from "../services/ChatService";


function ChatWindow(){

    const [question,setQuestion]=useState("");
    const [answer,setAnswer]=useState("");



    const handleSend=async()=>{

        if(!question)
            return;


        try{

            const data=await sendMessage(question);

            setAnswer(
                data.answer || JSON.stringify(data)
            );

        }
        catch(error){

            console.log(error);

            setAnswer(
                "Backend connection failed"
            );
        }

    };


    return(

        <div>

            <h2>
                Chat
            </h2>


            <p>
            Ask questions about company policies...
            </p>


            <input
            style={{width:"80%"}}
            value={question}
            onChange={
                e=>setQuestion(e.target.value)
            }
            placeholder="Ask your question..."
            />


            <button onClick={handleSend}>
                Send
            </button>



            <div>

                <h3>
                    Answer
                </h3>

                <p>
                    {answer}
                </p>

            </div>


        </div>

    )

}


export default ChatWindow;