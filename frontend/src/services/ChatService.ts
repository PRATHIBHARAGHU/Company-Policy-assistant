import axios from "axios";

const API_URL="http://localhost:8000";


export async function sendMessage(question:string){

    const response = await axios.post(
        `${API_URL}/chat`,
        {
            question: question
        }
    );

    return response.data;
}